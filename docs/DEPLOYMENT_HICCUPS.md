# Deployment Hiccups Log

> Running list of mistakes, surprises, and fixes. The point is to not repeat them.

## 2026-06-05 — Robert

- Hardcoded token in `entrypoint.sh` overrode env token
- Missing `xz-utils` broke browser tool Node.js extraction
- Shared host gateway caused cross-talk risk
- Wrong profile name / missing profile caused container restart loops
- Stale certbot dry-run process confused renew checks
- Nginx backup file left enabled, causing duplicate server warnings
- Website needed explicit security headers (`HSTS`, `nosniff`, `DENY`, etc.)

## Rule
If something surprises us once, write it down here before moving on.
