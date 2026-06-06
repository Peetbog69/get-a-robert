# Ampersand.foo — Implementation Steps

**Goal:** Deploy landing page + analytics by end of week

---

## Step 1: Domain & DNS (Today)

### 1.1 Verify Domain Registration
```bash
# Check if ampersand.foo is registered
whois ampersand.foo
```

### 1.2 Point DNS to VPS
**Current VPS:** `216.128.154.45`

**If using Namecheap/Porkbun/common registrar:**
1. Log into domain registrar dashboard
2. Go to DNS settings for ampersand.foo
3. Add **A record**: 
   - Host: `@` (root)
   - Value: `216.128.154.45`
   - TTL: 3600
4. Add **CNAME** for www (optional):
   - Host: `www`
   - Value: `ampersand.foo`

**Wait 15 min – 2 hours for DNS propagation**

### 1.3 Verify DNS Works
```bash
nslookup ampersand.foo
dig ampersand.foo
```

---

## Step 2: SSL Certificate (Today)

### 2.1 SSH to VPS
```bash
ssh root@216.128.154.45
# Or your configured SSH key
```

### 2.2 Install Let's Encrypt (if not already installed)
```bash
apt update
apt install certbot python3-certbot-nginx
# Or use the webroot method if not using nginx
```

### 2.3 Generate SSL Cert
```bash
certbot certonly --standalone -d ampersand.foo -d www.ampersand.foo
# Or if nginx is already running:
certbot certonly --nginx -d ampersand.foo -d www.ampersand.foo
```

### 2.4 Auto-renewal
```bash
certbot renew --dry-run
# Certbot auto-renews every 60 days by default
```

---

## Step 3: Landing Page Design (This Week)

### 3.1 Page Structure
```
┌──────────────────────────────┐
│   ampersand.foo              │ (Header — minimal)
├──────────────────────────────┤
│                              │
│  [Phone mockup showing       │
│   conversation]              │
│                              │
│  ___________________________  │
│  "Talk to them."             │ (Single line)
│  [START TALKING] button      │
│                              │
└──────────────────────────────┘
```

### 3.2 Color Palette
```css
--black: #141414      /* Background */
--amber: #D4A123      /* Primary accent, button */
--cream: #F0E6D3      /* Text, highlights */
--ash: #1E1E1E        /* Card surface */
--malibu: #8ED1FC     /* Secondary accent */
```

### 3.3 Typography
- Display: Georgia italic (ampersand logo)
- Body: System sans (-apple-system, BlinkMacSystemFont, etc.)
- Mono: System mono (if showing code snippets)

### 3.4 File Structure
```
/var/www/ampersand.foo/
├── index.html          (Landing page)
├── assets/
│   ├── style.css
│   ├── app.js          (Minimal — analytics + tracking)
│   └── images/
│       └── phone-mockup.png  (Screenshot of conversation)
└── .htaccess           (Redirects, caching)
```

---

## Step 4: Landing Page Code (This Week)

### 4.1 Basic HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Ampersand — Talk to a Person</title>
    <link rel="stylesheet" href="assets/style.css">
    <!-- Favicon: Georgia italic & -->
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text x='50' y='80' font-size='80' font-family='Georgia' font-style='italic' fill='%23D4A123' text-anchor='middle'>&amp;</text></svg>">
</head>
<body>
    <div class="container">
        <header>
            <h1>&amp;</h1>
        </header>
        
        <main>
            <div class="phone-mockup">
                <img src="assets/images/phone-mockup.png" alt="Conversation with Ampersand">
            </div>
            
            <p class="tagline">Talk to them.</p>
            
            <a href="#" class="cta-button" onclick="startTalking()">Start Talking</a>
        </main>
        
        <footer>
            <p>No login. No promises. Just a person.</p>
        </footer>
    </div>
    
    <script src="assets/app.js"></script>
</body>
</html>
```

### 4.2 CSS (Minimal)
```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

:root {
    --black: #141414;
    --amber: #D4A123;
    --cream: #F0E6D3;
    --ash: #1E1E1E;
    --malibu: #8ED1FC;
}

body {
    background: var(--black);
    color: var(--cream);
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    line-height: 1.6;
}

.container {
    max-width: 600px;
    margin: 0 auto;
    padding: 2rem;
    text-align: center;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

header h1 {
    font-family: Georgia, serif;
    font-style: italic;
    font-size: 3rem;
    color: var(--amber);
    margin-bottom: 3rem;
}

.phone-mockup {
    margin: 2rem 0;
}

.phone-mockup img {
    max-width: 100%;
    height: auto;
    border-radius: 20px;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
}

.tagline {
    font-size: 1.5rem;
    margin: 2rem 0 1rem;
    color: var(--cream);
}

.cta-button {
    display: inline-block;
    background: var(--amber);
    color: var(--black);
    padding: 1rem 2rem;
    border-radius: 8px;
    text-decoration: none;
    font-weight: 600;
    margin-top: 2rem;
    transition: all 0.2s ease;
}

.cta-button:hover {
    background: var(--malibu);
    color: var(--black);
    transform: scale(1.05);
}

footer {
    margin-top: 4rem;
    font-size: 0.9rem;
    opacity: 0.7;
}

@media (max-width: 600px) {
    header h1 { font-size: 2rem; }
    .tagline { font-size: 1.2rem; }
}
```

### 4.3 JavaScript (Analytics + CTA)
```javascript
// Google Analytics
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'G-XXXXXXXXXX'); // Replace with your GA ID

// CTA button — opens Telegram download
function startTalking() {
    window.location.href = 'https://telegram.org/dl';
    
    // Track event
    gtag('event', 'start_talking_click');
}

// Scroll depth tracking
let maxScroll = 0;
window.addEventListener('scroll', () => {
    const scrollPercent = (window.scrollY / (document.documentElement.scrollHeight - window.innerHeight)) * 100;
    if (scrollPercent > maxScroll) {
        maxScroll = scrollPercent;
        if ([25, 50, 75, 100].includes(Math.round(scrollPercent))) {
            gtag('event', 'scroll_depth', { value: Math.round(scrollPercent) });
        }
    }
});
```

---

## Step 5: Nginx/Web Server Config (This Week)

### 5.1 Create Nginx Config
```bash
# On VPS, create new config
nano /etc/nginx/sites-available/ampersand.foo
```

### 5.2 Nginx Config File
```nginx
server {
    listen 80;
    server_name ampersand.foo www.ampersand.foo;
    
    # Redirect HTTP to HTTPS
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name ampersand.foo www.ampersand.foo;
    
    # SSL certificates (from Let's Encrypt)
    ssl_certificate /etc/letsencrypt/live/ampersand.foo/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/ampersand.foo/privkey.pem;
    
    # Security headers
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-Frame-Options "SAMEORIGIN" always;
    
    root /var/www/ampersand.foo;
    index index.html;
    
    # Cache static assets
    location ~* \.(css|js|png|jpg|gif|ico|svg)$ {
        expires 30d;
        add_header Cache-Control "public, immutable";
    }
    
    # Serve index.html for SPA routing (if needed)
    location / {
        try_files $uri $uri/ /index.html;
    }
}
```

### 5.3 Enable Site & Restart
```bash
ln -s /etc/nginx/sites-available/ampersand.foo /etc/nginx/sites-enabled/
nginx -t
systemctl reload nginx
```

---

## Step 6: Phone Mockup Screenshot (This Week)

### 6.1 Create or Capture
Option A: Use design tool (Figma)
- Create iPhone frame (390x844px)
- Add conversation screenshot inside
- Export as PNG

Option B: Capture from actual app
- Screenshot conversation with Robert
- Add iPhone frame mockup overlay
- Crop to 390x844px

### 6.2 Optimize
```bash
# Compress image
ffmpeg -i phone-mockup.png -vf "scale=390:844" phone-mockup.webp
# Or use ImageMagick
convert phone-mockup.png -resize 390x844 phone-mockup.webp
```

---

## Step 7: Deploy & Test (This Week)

### 7.1 Upload Files to VPS
```bash
scp -r landing-page/* root@216.128.154.45:/var/www/ampersand.foo/
```

### 7.2 Test Locally
```bash
# On VPS, verify files are in place
ls -la /var/www/ampersand.foo/
curl https://ampersand.foo
```

### 7.3 Browser Test
1. Open https://ampersand.foo in Chrome, Firefox, Safari
2. Test responsive design (mobile, tablet, desktop)
3. Click "Start Talking" button
4. Check browser console for JS errors

### 7.4 Uptime Monitoring
```bash
# Set up simple health check
curl -s https://ampersand.foo | grep "Talk to them" && echo "✓ Site up"
```

---

## Step 8: Ongoing Monitoring (Weekly)

```bash
# Verify certbot will auto-renew
certbot renew --dry-run
```

---

## Checklist — Ready to Launch

- [ ] DNS A record pointing to 216.128.154.45
- [ ] SSL certificate installed & auto-renewing
- [ ] Landing page HTML, CSS, JS uploaded
- [ ] Phone mockup image in assets/
- [ ] Nginx config enabled & reloading
- [ ] CTA button links to correct app URL
- [ ] Mobile responsive design tested
- [ ] Browser console has no errors

---

## Timeline

| Task | Effort | Timeline |
|------|--------|----------|
| DNS + SSL | 30 min | Today |
| Landing page HTML/CSS/JS | 2-3 hrs | Today-Tomorrow |
| Nginx config | 1 hr | Tomorrow |
| Phone mockup screenshot | 30 min | Tomorrow |
| Deploy & test | 1 hr | Tomorrow |
| **Total** | **5-6 hrs** | **This week** |

---

## Troubleshooting

**DNS not resolving?**
- Wait 2 hours for propagation
- Check registrar's DNS settings match
- Use `dig ampersand.foo` to debug

**SSL certificate errors?**
- Make sure DNS is resolving first
- Run `certbot certonly --standalone` while nginx is stopped
- Check `/var/log/letsencrypt/` for errors

**Analytics not tracking?**
- Verify Measurement ID is correct
- Check browser console for gtag errors
- Allow 24 hours for historical data

**Button not working?**
- Where should it link? (Same domain? Different app domain?)
- Update `href` in HTML
- Test in console: `window.location.href = '...'`

---

*Last updated: May 31, 2026*
