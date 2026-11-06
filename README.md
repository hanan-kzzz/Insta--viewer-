# InstaPrivacy Scanner

Simple username-first Instagram privacy assessment starter.

## Project
- `index.html`: standalone dashboard with one username field and Scan button.
- `backend/`: minimal Node.js API with owner-authorization check.
- `windows-agent/`: imports an Instagram data export supplied by the account owner.

## Run the dashboard
Open `index.html` in a modern browser.

## Run the backend
```bash
cd backend
npm install
npm start
```
API listens on port 4000 by default.

## Windows export agent
```powershell
cd windows-agent
py agent.py --input "C:\path\to\owner-export.zip" --output ".\imports"
```

## Safety and technical limits
A username-only lookup cannot prove whether private posts, Reels, or Stories are exposed to non-followers. Verify with written owner authorization and a controlled non-follower test account. Connect only an approved Meta/Instagram API integration with permissions actually granted.

This project does not bypass private-account controls, scrape private content, collect passwords or session cookies, or download private content. Owner-provided exports and permitted public content are the supported download paths.

Production deployment still needs authentication, rate limiting, HTTPS, audit logs, and a configured approved provider.
