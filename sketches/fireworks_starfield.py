#!/usr/bin/env python3
"""Fireworks → Starfield. Ctrl+C to skip to next, twice to quit."""

import math, os, random, sys, time, signal, threading

# ── Terminal setup ──────────────────────────────────────────────
os.system("setterm -cursor off 2>/dev/null")
try:
    cols, rows = os.get_terminal_size()
except OSError:
    cols, rows = 80, 24

quit_flag = threading.Event()
signal.signal(signal.SIGINT, lambda s, f: quit_flag.set())


def reset():
    print("\033[?25h\033[0m", end="", flush=True)
    os.system("stty echo 2>/dev/null")


atexit = reset

# ── Helpers ─────────────────────────────────────────────────────
def goto(x, y, s):
    print(f"\033[{y};{x}H{s}", end="", flush=True)


def rand_color():
    return random.choice([196, 202, 208, 214, 220, 226, 190, 154, 118, 82, 46])


def clear():
    print("\033[2J\033[H", end="", flush=True)


# ══════════════════════════════════════════════════════════════════
#  FIREWORKS
# ══════════════════════════════════════════════════════════════════
COLORS_FIRE = {
    "red": [196, 160, 124],
    "gold": [220, 214, 208],
    "green": [46, 40, 34],
    "blue": [21, 27, 33],
    "purple": [129, 93, 57],
    "cyan": [51, 45, 39],
    "pink": [201, 165, 129],
    "white": [255, 252, 249],
}


class Spark:
    def __init__(self, x, y, vx, vy, color_scheme, life):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color_scheme = color_scheme
        self.life = life
        self.max_life = life

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += 0.04
        self.vx *= 0.995
        self.life -= 1

    def alive(self):
        return self.life > 0 and 0 <= self.x < cols and 0 <= self.y < rows

    def pixel(self):
        t = self.life / self.max_life
        idx = min(int((1 - t) * len(self.color_scheme)), len(self.color_scheme) - 1)
        color = self.color_scheme[idx]
        if t < 0.15:
            return " "
        c = "·" if t < 0.3 else "•" if t < 0.6 else "✦" if t < 0.85 else "*"
        return f"\033[38;5;{color}m{c}\033[0m"


class Rocket:
    def __init__(self):
        self.x = random.randint(cols // 4, 3 * cols // 4)
        self.y = rows - 1
        self.target_y = random.randint(3, rows // 3)
        self.vy = -random.uniform(2.5, 4.5)
        self.trail: list[tuple[int, int]] = []
        self.done = False
        self.sparks: list[Spark] = []
        self.color_name = random.choice(list(COLORS_FIRE.keys()))
        self.color_scheme = COLORS_FIRE[self.color_name]
        self.trail_color = self.color_scheme[0]

    def update(self):
        if not self.done:
            self.trail.append((int(self.x), int(self.y)))
            if len(self.trail) > 8:
                self.trail.pop(0)
            self.y += self.vy
            if self.y <= self.target_y:
                self.done = True
                self._explode()

        # Update sparks
        for s in self.sparks:
            s.update()
        self.sparks = [s for s in self.sparks if s.alive()]

    def _explode(self):
        kind = random.choice(["ring", "sphere", "double"])
        count = random.randint(40, 80)
        cx, cy = int(self.x), int(self.y)
        if kind == "ring":
            for i in range(count):
                angle = (2 * math.pi * i) / count
                speed = random.uniform(1.5, 3.0)
                self.sparks.append(
                    Spark(cx, cy, math.cos(angle) * speed, math.sin(angle) * speed, self.color_scheme, random.randint(15, 30))
                )
        elif kind == "sphere":
            for _ in range(count):
                angle = random.uniform(0, 2 * math.pi)
                speed = random.uniform(1.0, 3.5)
                self.sparks.append(
                    Spark(cx, cy, math.cos(angle) * speed, math.sin(angle) * speed, self.color_scheme, random.randint(18, 35))
                )
        else:  # double ring
            for _ in range(count // 2):
                angle = random.uniform(0, 2 * math.pi)
                speed = random.uniform(1.2, 2.2)
                self.sparks.append(
                    Spark(cx, cy, math.cos(angle) * speed, math.sin(angle) * speed, self.color_scheme, random.randint(20, 30))
                )
            color2 = random.choice([c for c in COLORS_FIRE if c != self.color_name])
            scheme2 = COLORS_FIRE[color2]
            for _ in range(count // 2):
                angle = random.uniform(0, 2 * math.pi)
                speed = random.uniform(2.0, 3.8)
                self.sparks.append(
                    Spark(cx, cy, math.cos(angle) * speed, math.sin(angle) * speed, scheme2, random.randint(15, 25))
                )

    def active(self):
        return not self.done or len(self.sparks) > 0


def fireworks():
    clear()
    rockets: list[Rocket] = []
    frame = 0
    title = "✦ FIREWORKS  ✦"
    try:
        while not quit_flag.is_set():
            if frame % random.randint(8, 18) == 0 and len(rockets) < 6:
                rockets.append(Rocket())
            for r in rockets:
                r.update()
            rockets = [r for r in rockets if r.active()]

            screen = {}
            # Draw rockets + trails
            for r in rockets:
                if not r.done:
                    screen[(int(r.x), int(r.y))] = f"\033[38;5;{r.trail_color}m█\033[0m"
                    for i, (tx, ty) in enumerate(r.trail):
                        alpha = int(255 * (i / len(r.trail)))
                        c = 232 + (alpha // 42)
                        screen[(tx, ty)] = f"\033[38;5;{c}m│\033[0m"
            # Draw sparks
            for r in rockets:
                for s in r.sparks:
                    sx, sy = int(s.x), int(s.y)
                    screen[(sx, sy)] = s.pixel()

            buf = ["\033[H"]
            for y in range(rows):
                line = []
                for x in range(cols):
                    line.append(screen.get((x, y), " "))
                buf.append("".join(line))
            # Title
            tx = cols // 2 - len(title) // 2
            buf[1] = buf[1][:tx] + f"\033[1;38;5;220m{title}\033[0m" + buf[1][tx + len(title):]
            sys.stdout.write("".join(buf))
            sys.stdout.flush()
            time.sleep(0.03)
            frame += 1
    except Exception:
        pass


# ══════════════════════════════════════════════════════════════════
#  STARFIELD
# ══════════════════════════════════════════════════════════════════
class Star:
    def __init__(self):
        self.x = random.uniform(-1, 1)
        self.y = random.uniform(-1, 1)
        self.z = random.uniform(0.01, 1)  # avoid exactly 0

    def update(self, speed):
        self.z -= speed
        if self.z <= 0.01:
            self.z = 1
            self.x = random.uniform(-1, 1)
            self.y = random.uniform(-1, 1)

    def screen_pos(self):
        scale = 0.5
        sx = int(cols / 2 + (self.x / self.z) * cols * scale)
        sy = int(rows / 2 + (self.y / self.z) * rows * scale * 0.5)
        return sx, sy

    def bright(self):
        # Brighter when closer (z small)
        return max(0, min(1, 1 - self.z))


def starfield():
    stars = [Star() for _ in range(300)]
    base_speed = 0.008
    frame = 0
    title = "✦ STARFIELD  ✦"
    try:
        while not quit_flag.is_set():
            speed = base_speed * (1 + 0.5 * math.sin(frame * 0.02))
            for s in stars:
                s.update(speed)
                sx, sy = s.screen_pos()
                if not (0 <= sx < cols and 0 <= sy < rows):
                    s.z = 1
                    s.x = random.uniform(-1, 1)
                    s.y = random.uniform(-1, 1)

            screen = [[" "] * cols for _ in range(rows)]
            for s in stars:
                sx, sy = s.screen_pos()
                if 0 <= sx < cols and 0 <= sy < rows:
                    b = s.bright()
                    if b > 0.7:
                        c = f"\033[38;5;{255}m"
                        ch = "●"
                    elif b > 0.4:
                        c = f"\033[38;5;{252}m"
                        ch = "•"
                    elif b > 0.15:
                        c = f"\033[38;5;{244}m"
                        ch = "·"
                    else:
                        c = f"\033[38;5;{236}m"
                        ch = "·"
                    screen[sy][sx] = f"{c}{ch}\033[0m"

            buf = ["\033[H"]
            for y in range(rows):
                buf.append("".join(screen[y]))
            # Title
            tx = cols // 2 - len(title) // 2
            buf[1] = buf[1][:tx] + f"\033[1;38;5;153m{title}\033[0m" + buf[1][tx + len(title):]
            sys.stdout.write("".join(buf))
            sys.stdout.flush()
            time.sleep(0.02)
            frame += 1
    except Exception:
        pass


# ══════════════════════════════════════════════════════════════════
import atexit

if __name__ == "__main__":
    try:
        fireworks()
        quit_flag.clear()
        starfield()
    except KeyboardInterrupt:
        pass
    finally:
        reset()
