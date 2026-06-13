# MobileTrans SEO Site

> Affiliate promotional site for Wondershare MobileTrans — #1 phone transfer app for iPhone, Android and WhatsApp.

**Live site:** https://brightlane.github.io/iphonerepair/

---

## What This Repo Does

A single Python build script (`build.py`) generates a complete phone transfer affiliate site into `dist/`. The workflow cleans all old files from the repo first, then deploys to GitHub Pages.

```
build.py   ←  the only file you need to edit or commit
```

---

## Quick Start

### Repo needs:

```
iphonerepair/
├── build.py
├── README.md
└── .github/
    └── workflows/
        └── deploy.yml
```

### Enable GitHub Pages

**Settings → Pages → Source: GitHub Actions**

### Run the workflow

**Actions → Build & Deploy MobileTrans → Run workflow**

Old files deleted automatically. Site live at **https://brightlane.github.io/iphonerepair/**

---

## What Gets Built

| Content | Count |
|---|---|
| Essential pages | 11 |
| Keyword-targeted pages | 167 |
| Blog posts | 12 |
| Total files | ~2,156 |
| Total size | ~59 MB |

### Essential Pages

| File | Description |
|---|---|
| `index.html` | Homepage — 8-scenario hub, features, why MobileTrans |
| `features.html` | Feature list with 5-tool comparison table |
| `how-it-works.html` | 3-step guide + USB vs WiFi + special scenarios |
| `faq.html` | 18 FAQs with FAQPage schema |
| `compare.html` | vs Move to iOS, iCloud, iTunes, Dr.Fone |
| `blog.html` | Blog index — 12 full articles |
| `download.html` | Download CTA with system requirements |
| `keywords.html` | All 167 topics by category |
| `glossary.html` | 25 phone transfer terms defined |
| `privacy.html` | Privacy policy + affiliate disclosure |
| `404.html` | Branded 404 with auto-redirect |

### Blog Posts (in `blog/`)

1. How to Transfer Everything from Android to iPhone
2. How to Transfer iPhone Data to Android
3. Transfer WhatsApp from Android to iPhone
4. Transfer WhatsApp from iPhone to Android
5. Transfer All Data to Your New iPhone
6. Samsung to iPhone Transfer Guide
7. Move to iOS Not Working? Here's the Fix
8. Backup iPhone to PC Without iTunes
9. Transfer WhatsApp to Any New Phone
10. Transfer iCloud Data to Android
11. Best Phone Transfer App 2025 — Ranked
12. Transfer Data from a Broken iPhone

### Keyword Categories (12)

`brand` · `iphone` · `android-to-iphone` · `iphone-to-android` · `whatsapp` · `phone-transfer` · `backup` · `compare` · `howto` · `platform` · `global` · `business`

---

## Config at the top of `build.py`

```python
AFFILIATE_URL = "https://www.linkconnector.com/ta.php?lc=007949095047004532&atid=iphonetransfer"
SITE_DOMAIN   = "https://brightlane.github.io/iphonerepair"
BASE_PATH     = "/iphonerepair"
```

---

## Affiliate Disclosure

All links use `rel="nofollow sponsored"`. Disclosure in footer and privacy page.

MobileTrans is a product of Wondershare Technology Co., Ltd.
