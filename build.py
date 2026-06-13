#!/usr/bin/env python3
"""
Wondershare MobileTrans SEO Site Builder
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Domain: brightlane.github.io/iphonerepair
• 200+ keyword-targeted pages
• 12 full blog posts
• 11 essential pages including Glossary
• llms.txt, sitemap.xml, robots.txt
• Old-file cleanup baked into workflow

Usage: python3 build.py
Output: ./dist/
"""

import os, json
from datetime import date
from collections import defaultdict

AFFILIATE_URL = "https://www.linkconnector.com/ta.php?lc=007949095047004532&atid=iphonetransfer"
SITE_DOMAIN   = "https://brightlane.github.io/iphonerepair"
BASE_PATH     = "/iphonerepair"
BUILD_DATE    = date.today().isoformat()
DIST          = "dist"
YEAR          = date.today().year

# ═══════════════════════════════════════════════
#  KEYWORDS
# ═══════════════════════════════════════════════
KEYWORDS = []
_seen = set()
def kw(slug, keyword, cat):
    if slug in _seen: return
    _seen.add(slug)
    KEYWORDS.append({"slug": slug, "keyword": keyword, "cat": cat})

# Brand
for s,k in [
    ("wondershare-mobiletrans","Wondershare MobileTrans"),
    ("mobiletrans","MobileTrans phone transfer"),
    ("mobiletrans-review","MobileTrans review 2025"),
    ("mobiletrans-download","MobileTrans download"),
    ("mobiletrans-free","MobileTrans free download"),
    ("mobiletrans-free-trial","MobileTrans free trial"),
    ("mobiletrans-windows","MobileTrans for Windows"),
    ("mobiletrans-mac","MobileTrans for Mac"),
    ("mobiletrans-2025","MobileTrans 2025"),
    ("mobiletrans-price","MobileTrans price"),
    ("mobiletrans-coupon","MobileTrans coupon code 2025"),
    ("mobiletrans-safe","is MobileTrans safe"),
    ("mobiletrans-legit","is MobileTrans legit"),
    ("mobiletrans-features","MobileTrans features"),
    ("mobiletrans-tutorial","MobileTrans tutorial"),
    ("mobiletrans-how-to-use","how to use MobileTrans"),
    ("wondershare-phone-transfer","Wondershare phone transfer software"),
    ("mobiletrans-6000-devices","MobileTrans supports 6000 devices"),
    ("mobiletrans-18-data-types","MobileTrans 18 data types transfer"),
    ("mobiletrans-alternative","MobileTrans alternative"),
    ("mobiletrans-vs-drfone","MobileTrans vs Dr.Fone"),
]: kw(s,k,"brand")

# iPhone transfer
for s,k in [
    ("iphone-transfer-software","iPhone transfer software"),
    ("best-iphone-transfer-software","best iPhone transfer software 2025"),
    ("transfer-iphone-to-iphone","transfer iPhone to iPhone"),
    ("transfer-data-to-new-iphone","transfer data to new iPhone"),
    ("iphone-to-iphone-transfer","iPhone to iPhone data transfer"),
    ("iphone-data-transfer","iPhone data transfer software"),
    ("transfer-iphone-without-icloud","transfer iPhone without iCloud"),
    ("transfer-iphone-without-itunes","transfer iPhone without iTunes"),
    ("transfer-old-iphone-to-new","transfer data from old iPhone to new iPhone"),
    ("iphone-17-transfer","transfer data to iPhone 17"),
    ("iphone-16-transfer","transfer data to iPhone 16"),
    ("switch-to-new-iphone","how to switch to new iPhone"),
    ("iphone-transfer-contacts","transfer contacts to new iPhone"),
    ("iphone-transfer-photos","transfer photos to new iPhone"),
    ("iphone-transfer-videos","transfer videos to new iPhone"),
    ("iphone-transfer-messages","transfer messages to new iPhone"),
    ("iphone-transfer-music","transfer music to new iPhone"),
    ("iphone-transfer-apps","transfer apps to new iPhone"),
    ("iphone-backup-transfer","iPhone backup and transfer software"),
    ("iphone-data-migration","iPhone data migration software"),
    ("move-to-iphone","move data to iPhone from Android"),
    ("iphone-transfer-fast","fast iPhone data transfer software"),
    ("iphone-transfer-free","iPhone transfer software free"),
]: kw(s,k,"iphone")

# Android to iPhone
for s,k in [
    ("android-to-iphone-transfer","Android to iPhone transfer"),
    ("android-to-iphone-data-transfer","Android to iPhone data transfer software"),
    ("switch-from-android-to-iphone","switch from Android to iPhone"),
    ("samsung-to-iphone-transfer","Samsung to iPhone transfer"),
    ("samsung-to-iphone-data","transfer data from Samsung to iPhone"),
    ("android-to-ios-transfer","Android to iOS transfer software"),
    ("move-from-android-to-ios","move from Android to iOS"),
    ("google-pixel-to-iphone","Google Pixel to iPhone transfer"),
    ("android-to-iphone-contacts","transfer contacts Android to iPhone"),
    ("android-to-iphone-photos","transfer photos Android to iPhone"),
    ("android-to-iphone-messages","transfer messages Android to iPhone"),
    ("android-to-iphone-whatsapp","transfer WhatsApp Android to iPhone"),
    ("android-to-iphone-music","transfer music Android to iPhone"),
    ("android-to-iphone-free","Android to iPhone transfer free"),
    ("best-android-to-iphone-app","best Android to iPhone transfer app"),
    ("move-to-ios-alternative","Move to iOS app alternative"),
    ("move-to-ios-not-working","Move to iOS alternative when not working"),
]: kw(s,k,"android-to-iphone")

# iPhone to Android
for s,k in [
    ("iphone-to-android-transfer","iPhone to Android transfer"),
    ("iphone-to-samsung-transfer","iPhone to Samsung transfer"),
    ("switch-from-iphone-to-android","switch from iPhone to Android"),
    ("iphone-to-android-contacts","transfer contacts iPhone to Android"),
    ("iphone-to-android-photos","transfer photos iPhone to Android"),
    ("iphone-to-android-messages","transfer messages iPhone to Android"),
    ("iphone-to-android-whatsapp","transfer WhatsApp iPhone to Android"),
    ("iphone-to-android-music","transfer music iPhone to Android"),
    ("ios-to-android-transfer","iOS to Android transfer software"),
    ("best-iphone-to-android-app","best iPhone to Android transfer app 2025"),
]: kw(s,k,"iphone-to-android")

# WhatsApp transfer
for s,k in [
    ("whatsapp-transfer","WhatsApp transfer software"),
    ("whatsapp-transfer-android-to-iphone","WhatsApp transfer Android to iPhone"),
    ("whatsapp-transfer-iphone-to-android","WhatsApp transfer iPhone to Android"),
    ("transfer-whatsapp-to-new-phone","transfer WhatsApp to new phone"),
    ("whatsapp-backup-transfer","WhatsApp backup and transfer"),
    ("whatsapp-chat-transfer","WhatsApp chat history transfer"),
    ("whatsapp-transfer-without-google","WhatsApp transfer without Google Drive"),
    ("whatsapp-transfer-without-icloud","WhatsApp transfer without iCloud"),
    ("best-whatsapp-transfer-software","best WhatsApp transfer software 2025"),
    ("whatsapp-transfer-free","WhatsApp transfer free software"),
    ("whatsapp-business-transfer","WhatsApp Business transfer software"),
    ("transfer-whatsapp-iphone-17","transfer WhatsApp to iPhone 17"),
    ("transfer-whatsapp-samsung","transfer WhatsApp to Samsung"),
    ("whatsapp-transfer-viber-line","transfer Viber LINE WeChat between phones"),
    ("whatsapp-export-pdf","export WhatsApp chats to PDF"),
    ("google-drive-whatsapp-to-iphone","Google Drive WhatsApp backup to iPhone"),
]: kw(s,k,"whatsapp")

# Phone to phone
for s,k in [
    ("phone-to-phone-transfer","phone to phone transfer software"),
    ("phone-transfer-software","phone transfer software"),
    ("best-phone-transfer-software","best phone transfer software 2025"),
    ("phone-data-transfer","phone data transfer software"),
    ("switch-phones-data-transfer","switch phones data transfer tool"),
    ("new-phone-setup-transfer","new phone setup data transfer"),
    ("phone-upgrade-data-transfer","phone upgrade data transfer"),
    ("cross-platform-transfer","cross-platform phone transfer software"),
    ("samsung-to-samsung-transfer","Samsung to Samsung data transfer"),
    ("android-to-android-transfer","Android to Android data transfer"),
    ("huawei-to-iphone-transfer","Huawei to iPhone transfer"),
    ("oneplus-to-iphone-transfer","OnePlus to iPhone transfer"),
    ("xiaomi-to-iphone-transfer","Xiaomi to iPhone transfer"),
    ("phone-contacts-transfer","phone contacts transfer software"),
    ("phone-photos-transfer","phone photos transfer software"),
    ("transfer-sms-to-new-phone","transfer SMS messages to new phone"),
    ("transfer-call-logs","transfer call logs to new phone"),
    ("transfer-calendar-new-phone","transfer calendar to new phone"),
    ("phone-backup-restore","phone backup and restore software"),
]: kw(s,k,"phone-transfer")

# Backup & restore
for s,k in [
    ("phone-backup-software","phone backup software"),
    ("iphone-backup-software","iPhone backup software"),
    ("android-backup-software","Android backup software"),
    ("backup-phone-to-computer","backup phone to computer software"),
    ("iphone-backup-to-pc","backup iPhone to PC without iTunes"),
    ("iphone-backup-to-mac","backup iPhone to Mac"),
    ("android-backup-to-pc","backup Android phone to PC"),
    ("backup-whatsapp-to-computer","backup WhatsApp to computer"),
    ("restore-iphone-backup","restore iPhone from backup"),
    ("icloud-backup-to-android","transfer iCloud backup to Android"),
    ("icloud-to-android","move iCloud data to Android"),
    ("phone-backup-free","free phone backup software 2025"),
    ("backup-contacts-phone","backup phone contacts to computer"),
    ("backup-photos-phone","backup phone photos to computer"),
]: kw(s,k,"backup")

# Comparisons
for s,k in [
    ("best-phone-transfer-app-2025","best phone transfer app 2025"),
    ("mobiletrans-vs-imazing","MobileTrans vs iMazing"),
    ("mobiletrans-vs-anytrans","MobileTrans vs AnyTrans"),
    ("mobiletrans-vs-syncios","MobileTrans vs Syncios"),
    ("move-to-ios-alternative","Move to iOS app alternative 2025"),
    ("itunes-alternative-transfer","iTunes alternative phone transfer"),
    ("icloud-alternative-transfer","iCloud alternative data transfer"),
    ("best-android-iphone-transfer","best Android iPhone transfer tool"),
    ("phone-transfer-free-vs-paid","free vs paid phone transfer software"),
    ("mobiletrans-comparison","MobileTrans comparison 2025"),
]: kw(s,k,"compare")

# How-to
for s,k in [
    ("how-to-transfer-iphone-to-iphone","how to transfer iPhone to iPhone"),
    ("how-to-transfer-android-to-iphone","how to transfer Android to iPhone"),
    ("how-to-transfer-iphone-to-android","how to transfer iPhone to Android"),
    ("how-to-transfer-whatsapp-new-phone","how to transfer WhatsApp to new phone"),
    ("how-to-transfer-contacts-new-phone","how to transfer contacts to new phone"),
    ("how-to-transfer-photos-new-iphone","how to transfer photos to new iPhone"),
    ("how-to-transfer-sms-iphone","how to transfer SMS messages to iPhone"),
    ("how-to-backup-iphone-pc","how to backup iPhone to PC without iTunes"),
    ("how-to-switch-phone-keep-data","how to switch phones and keep all data"),
    ("how-to-transfer-without-wifi","how to transfer phone data without WiFi"),
    ("how-to-transfer-music-iphone","how to transfer music to iPhone without iTunes"),
    ("how-to-transfer-iphone-broken-screen","how to transfer data from broken iPhone"),
    ("how-to-move-apps-new-iphone","how to move apps to new iPhone"),
]: kw(s,k,"howto")

# Platforms / devices
for s,k in [
    ("iphone-transfer-windows-pc","iPhone transfer software for Windows PC"),
    ("iphone-transfer-mac","iPhone transfer software for Mac"),
    ("iphone-17-data-transfer","iPhone 17 data transfer software"),
    ("iphone-16-data-transfer","iPhone 16 data transfer"),
    ("ios-18-transfer","iOS 18 data transfer software"),
    ("ios-26-transfer","iOS 26 data transfer software"),
    ("samsung-s25-transfer","Samsung Galaxy S25 data transfer"),
    ("samsung-s26-transfer","Samsung Galaxy S26 data transfer"),
    ("android-14-transfer","Android 14 data transfer software"),
    ("ipad-transfer-software","iPad data transfer software"),
    ("ipad-to-iphone-transfer","transfer data from iPad to iPhone"),
    ("iphone-to-ipad-transfer","transfer data from iPhone to iPad"),
]: kw(s,k,"platform")

# Global
for s,k in [
    ("iphone-transfer-uk","iPhone transfer software UK"),
    ("iphone-transfer-australia","iPhone transfer software Australia"),
    ("iphone-transfer-canada","iPhone transfer software Canada"),
    ("iphone-transfer-india","iPhone transfer software India"),
    ("iphone-transfer-germany","iPhone transfer software Germany"),
    ("phone-transfer-worldwide","phone transfer software worldwide"),
    ("mobiletrans-uk","MobileTrans UK download"),
    ("mobiletrans-india","MobileTrans India"),
]: kw(s,k,"global")

# Business
for s,k in [
    ("business-phone-transfer","business phone data transfer"),
    ("enterprise-phone-migration","enterprise phone data migration"),
    ("it-phone-transfer","IT department phone transfer tool"),
    ("phone-transfer-employees","transfer data to employee new phone"),
    ("bulk-phone-transfer","bulk phone data transfer software"),
]: kw(s,k,"business")

print(f"Keywords loaded: {len(KEYWORDS)}")

COLORS = {
    "brand":            ("#0ea5e9","#0369a1"),
    "iphone":           ("#6366f1","#4338ca"),
    "android-to-iphone":("#10b981","#065f46"),
    "iphone-to-android":("#f59e0b","#92400e"),
    "whatsapp":         ("#22c55e","#15803d"),
    "phone-transfer":   ("#3b82f6","#1d4ed8"),
    "backup":           ("#8b5cf6","#5b21b6"),
    "compare":          ("#475569","#1e293b"),
    "howto":            ("#0284c7","#0369a1"),
    "platform":         ("#64748b","#334155"),
    "global":           ("#0ea5e9","#0c4a6e"),
    "business":         ("#7c3aed","#4c1d95"),
}
def ac(cat):
    c = COLORS.get(cat, ("#0ea5e9","#0369a1"))
    return c[0], c[1]

CAT_DESC = {
    "brand":            "Everything about Wondershare MobileTrans — reviews, pricing, downloads and tutorials.",
    "iphone":           "Transfer data to and from your iPhone — photos, contacts, messages, music and more.",
    "android-to-iphone":"Switch from Android to iPhone — transfer all your data across platforms seamlessly.",
    "iphone-to-android":"Switch from iPhone to Android — move contacts, photos, messages and WhatsApp.",
    "whatsapp":         "Transfer WhatsApp chat history between Android and iPhone — the easy way.",
    "phone-transfer":   "Transfer all data between any two phones — cross-platform, cross-brand.",
    "backup":           "Backup your iPhone or Android phone to your computer and restore anytime.",
    "compare":          "Compare MobileTrans vs alternatives — find the best phone transfer tool.",
    "howto":            "Step-by-step guides for every phone data transfer scenario.",
    "platform":         "Phone transfer software for Windows, Mac, iPhone 17 and the latest Android devices.",
    "global":           "MobileTrans phone transfer software available worldwide.",
    "business":         "Phone data transfer for businesses, IT teams and employee device upgrades.",
}

CSS = """<style>
:root{--ink:#0f172a;--paper:#f0f9ff;--card:#fff;--border:#e0f2fe;--muted:#475569;
  --dark:#0f172a;--ha:#0ea5e9;--hb:#0369a1;--fa:rgba(14,165,233,.08)}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--paper);color:var(--ink);font-family:'Segoe UI',system-ui,-apple-system,sans-serif;font-size:16px;line-height:1.65;overflow-x:hidden}
a{color:var(--ha);text-decoration:none}a:hover{text-decoration:underline}
nav{position:sticky;top:0;z-index:100;background:var(--dark);display:flex;align-items:center;justify-content:space-between;padding:0 clamp(1rem,4vw,2.5rem);height:58px;box-shadow:0 1px 0 rgba(255,255,255,.07)}
.nl{font-size:1.2rem;color:#fff;font-weight:800;letter-spacing:-.03em;white-space:nowrap}.nl span{color:#38bdf8}
.nlinks{display:flex;gap:1.4rem;align-items:center}
.nlinks a{color:rgba(255,255,255,.6);font-size:.82rem;font-weight:500;white-space:nowrap}
.nlinks a:hover{color:#fff;text-decoration:none}
.ncta{background:var(--ha)!important;color:#fff!important;padding:.38rem 1.05rem;border-radius:6px;font-weight:700!important;font-size:.82rem!important}
.hero{background:linear-gradient(135deg,#0c4a6e 0%,#0369a1 50%,#0ea5e9 100%);color:#fff;padding:clamp(3.5rem,8vw,6.5rem) clamp(1rem,5vw,3rem);text-align:center;position:relative;overflow:hidden}
.hero::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse 60% 50% at 50% 110%,rgba(56,189,248,.4) 0%,transparent 70%);pointer-events:none}
.eyebrow{display:inline-block;border-radius:100px;font-size:.7rem;font-weight:700;letter-spacing:.09em;text-transform:uppercase;padding:.26rem .95rem;margin-bottom:1.25rem;border:1px solid rgba(56,189,248,.5);color:#38bdf8;background:rgba(56,189,248,.1)}
h1{font-size:clamp(2rem,5.5vw,3.9rem);line-height:1.05;letter-spacing:-.035em;max-width:880px;margin:0 auto 1.1rem;font-weight:800}
h1 em{color:#bae6fd;font-style:italic}
.hsub{font-size:clamp(.95rem,2vw,1.12rem);color:rgba(255,255,255,.72);max-width:620px;margin:0 auto 2.3rem}
.btn-p{background:var(--ha);color:#fff;padding:.88rem 2.1rem;border-radius:8px;font-weight:700;font-size:1rem;display:inline-block;transition:transform .15s,box-shadow .15s}
.btn-p:hover{transform:translateY(-2px);box-shadow:0 8px 28px rgba(14,165,233,.5);text-decoration:none}
.btn-s{background:transparent;border:1px solid rgba(255,255,255,.3);color:rgba(255,255,255,.85);padding:.88rem 2.1rem;border-radius:8px;font-weight:600;font-size:1rem;display:inline-block}
.btn-s:hover{background:rgba(255,255,255,.1);text-decoration:none}
.btn-w{background:#fff;color:var(--ha);padding:.88rem 2.3rem;border-radius:8px;font-weight:700;font-size:1rem;display:inline-block;transition:transform .15s,box-shadow .15s}
.btn-w:hover{transform:translateY(-2px);box-shadow:0 8px 24px rgba(0,0,0,.18);text-decoration:none}
.btns{display:flex;gap:1rem;justify-content:center;flex-wrap:wrap}
.stats{display:flex;justify-content:center;gap:clamp(1.5rem,4vw,3.5rem);margin-top:3.5rem;padding-top:3rem;border-top:1px solid rgba(255,255,255,.12);flex-wrap:wrap}
.stat-n{font-size:clamp(1.8rem,3.5vw,2.6rem);color:#fff;display:block;font-weight:800;line-height:1}
.stat-l{font-size:.7rem;color:rgba(255,255,255,.5);text-transform:uppercase;letter-spacing:.07em;margin-top:.3rem}
section{padding:clamp(3rem,7vw,5.5rem) clamp(1rem,5vw,2.5rem)}
.container{max-width:1100px;margin:0 auto}
.sec-ey{font-size:.68rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--ha);margin-bottom:.55rem}
h2{font-size:clamp(1.7rem,3.5vw,2.55rem);line-height:1.1;letter-spacing:-.025em;margin-bottom:.75rem;font-weight:800}
h3{font-size:1.03rem;font-weight:700;margin-bottom:.42rem}
.sec-sub{color:var(--muted);max-width:590px;font-size:1rem;margin-bottom:3rem;line-height:1.7}
.grid2{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:1.5rem}
.grid3{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:1.4rem}
.grid4{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:1.2rem}
.card{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:1.75rem;transition:box-shadow .2s,transform .2s}
.card:hover{box-shadow:0 10px 36px rgba(14,165,233,.1);transform:translateY(-3px)}
.fi{width:46px;height:46px;border-radius:11px;display:flex;align-items:center;justify-content:center;font-size:1.3rem;margin-bottom:1.1rem;background:var(--fa)}
.card p,.card li{font-size:.87rem;color:var(--muted);line-height:1.7}
.card ul{padding-left:1.2rem;margin-top:.42rem}.card ul li{margin-bottom:.28rem}
.prose{max-width:780px;color:var(--muted);font-size:.95rem;line-height:1.82}
.prose p{margin-bottom:1.1rem}
.prose h2,.prose h3{color:var(--ink);margin:1.9rem 0 .5rem;font-weight:700}
.prose ul,.prose ol{padding-left:1.4rem;margin-bottom:1.1rem}
.prose li{margin-bottom:.4rem}
.prose strong{color:var(--ink);font-weight:600}
.steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:2rem;margin-top:2.5rem}
.step{text-align:center}
.sn{display:inline-flex;align-items:center;justify-content:center;width:50px;height:50px;border-radius:50%;background:var(--ha);color:#fff;font-size:1.25rem;font-weight:800;margin-bottom:.9rem}
.step h3{font-size:.94rem;margin-bottom:.3rem}
.step p{font-size:.82rem;color:var(--muted);line-height:1.6}
.tbl-wrap{overflow-x:auto;margin-top:2rem}
table{width:100%;border-collapse:collapse;font-size:.85rem;min-width:600px}
th{padding:.88rem 1rem;text-align:left;font-size:.73rem;font-weight:700;text-transform:uppercase;letter-spacing:.06em;border-bottom:2px solid var(--border)}
td{padding:.88rem 1rem;border-bottom:1px solid var(--border)}
tr:hover td{background:#f0f9ff}
.hl{color:var(--ha);font-weight:700}.ck{color:#16a34a;font-weight:600}.cr{color:#d1d5db}.cp{color:#f59e0b}
.faq-list{max-width:820px}
.faq-item{background:var(--card);border:1px solid var(--border);border-radius:10px;margin-bottom:.7rem;overflow:hidden}
.faq-q{padding:1.05rem 1.35rem;font-weight:700;font-size:.93rem;cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:1rem;user-select:none}
.faq-q::after{content:'+';font-size:1.3rem;color:var(--ha);flex-shrink:0;line-height:1}
.faq-item.open .faq-q::after{content:'\2212'}
.faq-a{padding:0 1.35rem 1.05rem;font-size:.87rem;color:var(--muted);line-height:1.75;display:none}
.faq-item.open .faq-a{display:block}
.cta-strip{background:linear-gradient(135deg,var(--hb) 0%,var(--ha) 100%);color:#fff;text-align:center;padding:clamp(3.5rem,7vw,6.5rem) clamp(1rem,5vw,3rem)}
.cta-strip h2{color:#fff;margin-bottom:.88rem}
.cta-strip p{color:rgba(255,255,255,.78);max-width:520px;margin:0 auto 2.3rem;font-size:1rem}
.bcrumb{font-size:.77rem;color:var(--muted);padding:.88rem clamp(1rem,5vw,2.5rem);max-width:1100px;margin:0 auto}
.bcrumb a{color:var(--muted)}.bcrumb a:hover{color:var(--ha);text-decoration:none}
.kw-cloud{display:flex;flex-wrap:wrap;gap:.46rem;margin-top:1.5rem}
.kw{background:var(--card);border:1px solid var(--border);border-radius:6px;padding:.27rem .72rem;font-size:.77rem;color:var(--muted)}
a.kw:hover{border-color:var(--ha);color:var(--ha);text-decoration:none}
.tcard{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:1.75rem}
.stars{color:#fbbf24;font-size:.95rem;margin-bottom:.88rem}
.ttext{font-size:.88rem;color:var(--ink);margin-bottom:1.3rem;line-height:1.78;font-style:italic}
.tauthor{font-weight:700;font-size:.8rem;color:var(--muted)}
.dark-sec{background:var(--dark);color:#fff}
.dark-sec .sec-ey{color:#38bdf8}.dark-sec h2{color:#fff}.dark-sec .sec-sub{color:rgba(255,255,255,.6)}
.dark-sec .kw{background:rgba(255,255,255,.07);border-color:rgba(255,255,255,.14);color:rgba(255,255,255,.7)}
.notice{background:rgba(14,165,233,.08);border:1px solid rgba(14,165,233,.25);border-radius:8px;padding:.92rem 1.35rem;font-size:.83rem;color:var(--muted);margin-top:2rem}
.badge{display:inline-block;font-size:.67rem;font-weight:700;letter-spacing:.07em;text-transform:uppercase;padding:.19rem .56rem;border-radius:4px;background:rgba(14,165,233,.1);color:var(--ha)}
.tr-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(155px,1fr));gap:1rem;margin-top:2rem}
.tr-card{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:1.2rem;text-align:center;transition:box-shadow .2s,transform .2s;display:block}
.tr-card:hover{box-shadow:0 8px 24px rgba(14,165,233,.12);transform:translateY(-2px);text-decoration:none}
.trc-icon{font-size:1.8rem;display:block;margin-bottom:.55rem}
.trc-label{font-size:.83rem;font-weight:700;color:var(--ink);display:block}
.trc-sub{font-size:.73rem;color:var(--muted);margin-top:.2rem;display:block}
footer{background:#020617;color:rgba(255,255,255,.48);padding:clamp(2.5rem,5vw,4rem) clamp(1rem,5vw,2.5rem) 2rem}
.fg{max-width:1100px;margin:0 auto;display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:2.5rem;margin-bottom:2.5rem}
.fn{font-size:1.3rem;color:#fff;font-weight:800;letter-spacing:-.03em;margin-bottom:.6rem}
.fn span{color:#38bdf8}
.fdesc{font-size:.79rem;color:rgba(255,255,255,.4);max-width:230px;margin-bottom:.9rem;line-height:1.6}
.fc h4{color:#fff;font-size:.73rem;font-weight:700;text-transform:uppercase;letter-spacing:.07em;margin-bottom:.82rem}
.fc ul{list-style:none}.fc ul li{margin-bottom:.38rem}
.fc ul li a{color:rgba(255,255,255,.44);font-size:.79rem}
.fc ul li a:hover{color:#fff;text-decoration:none}
.fb{max-width:1100px;margin:0 auto;border-top:1px solid rgba(255,255,255,.08);padding-top:1.75rem;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.75rem;font-size:.72rem}
.aff{background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.1);border-radius:6px;padding:.44rem .98rem;font-size:.72rem;margin-top:.75rem;max-width:530px;line-height:1.5}
@media(max-width:900px){.fg{grid-template-columns:1fr 1fr}}
@media(max-width:640px){.fg{grid-template-columns:1fr}.nlinks a:not(.ncta){display:none}h1{font-size:2rem}.steps{grid-template-columns:1fr 1fr}}
@media(max-width:400px){.steps{grid-template-columns:1fr}}
</style>"""

FAQ_JS = """<script>
document.querySelectorAll('.faq-q').forEach(q=>{
  q.addEventListener('click',()=>{
    const item=q.parentElement;
    document.querySelectorAll('.faq-item.open').forEach(o=>{if(o!==item)o.classList.remove('open')});
    item.classList.toggle('open');
  });
});
</script>"""

def NAV():
    return (f'<nav><a class="nl" href="{BASE_PATH}/">Mobile<span>Trans</span></a>'
            f'<div class="nlinks">'
            f'<a href="{BASE_PATH}/">Home</a>'
            f'<a href="{BASE_PATH}/features.html">Features</a>'
            f'<a href="{BASE_PATH}/how-it-works.html">How It Works</a>'
            f'<a href="{BASE_PATH}/compare.html">Compare</a>'
            f'<a href="{BASE_PATH}/faq.html">FAQ</a>'
            f'<a href="{BASE_PATH}/blog.html">Blog</a>'
            f'<a href="{AFFILIATE_URL}" class="ncta" target="_blank" rel="nofollow sponsored">&#8659; Free Download</a>'
            f'</div></nav>')

def FOOTER():
    return (f'<footer><div class="fg"><div>'
            f'<div class="fn">Mobile<span>Trans</span></div>'
            f'<p class="fdesc">Wondershare MobileTrans &#8212; #1 phone transfer app. Move data between any phones in minutes. 6,000+ devices, 18+ data types.</p>'
            f'<div class="aff">&#128279; Affiliate disclosure: Links on this site are affiliate links. We earn a commission at no extra cost to you.</div>'
            f'</div>'
            f'<div class="fc"><h4>Switch Phones</h4><ul>'
            f'<li><a href="{BASE_PATH}/android-to-iphone-transfer.html">Android to iPhone</a></li>'
            f'<li><a href="{BASE_PATH}/iphone-to-android-transfer.html">iPhone to Android</a></li>'
            f'<li><a href="{BASE_PATH}/transfer-iphone-to-iphone.html">iPhone to iPhone</a></li>'
            f'<li><a href="{BASE_PATH}/samsung-to-iphone-transfer.html">Samsung to iPhone</a></li>'
            f'<li><a href="{BASE_PATH}/phone-to-phone-transfer.html">Phone to Phone</a></li>'
            f'</ul></div>'
            f'<div class="fc"><h4>WhatsApp</h4><ul>'
            f'<li><a href="{BASE_PATH}/whatsapp-transfer.html">WhatsApp Transfer</a></li>'
            f'<li><a href="{BASE_PATH}/whatsapp-transfer-android-to-iphone.html">Android to iPhone</a></li>'
            f'<li><a href="{BASE_PATH}/whatsapp-transfer-iphone-to-android.html">iPhone to Android</a></li>'
            f'<li><a href="{BASE_PATH}/whatsapp-backup-transfer.html">Backup &amp; Restore</a></li>'
            f'<li><a href="{BASE_PATH}/transfer-whatsapp-to-new-phone.html">New Phone Transfer</a></li>'
            f'</ul></div>'
            f'<div class="fc"><h4>Resources</h4><ul>'
            f'<li><a href="{BASE_PATH}/faq.html">FAQ</a></li>'
            f'<li><a href="{BASE_PATH}/blog.html">Blog</a></li>'
            f'<li><a href="{BASE_PATH}/compare.html">Comparisons</a></li>'
            f'<li><a href="{BASE_PATH}/glossary.html">Glossary</a></li>'
            f'<li><a href="{BASE_PATH}/keywords.html">All Topics</a></li>'
            f'</ul></div></div>'
            f'<div class="fb">'
            f'<span>&#169; {YEAR} MobileTrans Guide. MobileTrans is a product of Wondershare Technology Co., Ltd.</span>'
            f'<span>Windows &amp; macOS &#183; Available Worldwide</span>'
            f'</div></footer>')

def BC(items):
    parts = []
    for label, url in items:
        if url: parts.append('<a href="' + url + '">' + label + '</a>')
        else: parts.append(label)
    return '<div class="bcrumb container">' + ' &rsaquo; '.join(parts) + '</div>'

def CTA(h="Switch Phones Without Losing a Single File &#8212; Download Free",
        p="Move everything to your new phone in minutes. 6,000+ devices, 18+ data types, WhatsApp included. Free trial."):
    return (f'<div class="cta-strip"><h2>{h}</h2><p>{p}</p>'
            f'<a href="{AFFILIATE_URL}" class="btn-w" target="_blank" rel="nofollow sponsored">&#8659; Download Free Trial</a></div>')

def SW_SCHEMA():
    d = {"@context":"https://schema.org","@type":"SoftwareApplication","name":"Wondershare MobileTrans",
         "operatingSystem":"Windows, macOS","applicationCategory":"UtilitiesApplication",
         "offers":{"@type":"Offer","price":"0","priceCurrency":"USD","description":"Free trial — transfer up to 20 photos"},
         "description":"MobileTrans transfers contacts, photos, videos, messages, WhatsApp and more between any two phones. 6,000+ devices, cross-platform.",
         "url":AFFILIATE_URL,
         "publisher":{"@type":"Organization","name":"Wondershare Technology"},
         "aggregateRating":{"@type":"AggregateRating","ratingValue":"4.8","reviewCount":"7432","bestRating":"5"}}
    return '<script type="application/ld+json">' + json.dumps(d) + '</script>'

def BC_SCHEMA(items):
    els = [{"@type":"ListItem","position":i+1,"name":l,"item":SITE_DOMAIN+"/"+u if u else SITE_DOMAIN} for i,(l,u) in enumerate(items)]
    return '<script type="application/ld+json">' + json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":els}) + '</script>'

def FAQ_SCHEMA(pairs):
    items = [{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in pairs]
    return '<script type="application/ld+json">' + json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":items}) + '</script>'

def ART_SCHEMA(title, desc, pub):
    d = {"@context":"https://schema.org","@type":"Article","headline":title,"description":desc,
         "datePublished":pub,"dateModified":BUILD_DATE,
         "author":{"@type":"Organization","name":"MobileTrans Guide"},
         "publisher":{"@type":"Organization","name":"MobileTrans Guide"}}
    return '<script type="application/ld+json">' + json.dumps(d) + '</script>'

def HEAD(title, desc, canon, extra="", og_type="website"):
    return ("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n"
            "<meta charset=\"UTF-8\"/><meta name=\"viewport\" content=\"width=device-width,initial-scale=1.0\"/>\n"
            f"<title>{title}</title>\n"
            f"<meta name=\"description\" content=\"{desc}\"/>\n"
            f"<link rel=\"canonical\" href=\"{SITE_DOMAIN}/{canon}\"/>\n"
            f"<meta property=\"og:title\" content=\"{title}\"/>\n"
            f"<meta property=\"og:description\" content=\"{desc}\"/>\n"
            f"<meta property=\"og:type\" content=\"{og_type}\"/>\n"
            f"<meta property=\"og:url\" content=\"{SITE_DOMAIN}/{canon}\"/>\n"
            "<meta property=\"og:site_name\" content=\"MobileTrans Guide\"/>\n"
            "<meta name=\"twitter:card\" content=\"summary_large_image\"/>\n"
            f"<meta name=\"twitter:title\" content=\"{title}\"/>\n"
            f"<meta name=\"twitter:description\" content=\"{desc}\"/>\n"
            "<meta name=\"robots\" content=\"index,follow\"/>\n"
            + CSS + "\n" + SW_SCHEMA() + "\n" + extra + "\n</head>")

FEATURES = [
    ("&#128247;","Phone to Phone Transfer","Move everything between any two phones in minutes &#8212; cross-platform, no brand limits.",
     ["Photos, videos, music, contacts","SMS, call logs, calendar","Apps and documents","200x faster than Bluetooth (30 MB/s)"]),
    ("&#128241;","Android &#8596; iPhone","Seamlessly switch between Android and iOS &#8212; the official tools often miss files, MobileTrans doesn't.",
     ["All 18+ data types transferred","Contacts, messages, photos, music","Cross-platform without ecosystem limits","Works even with broken screen devices"]),
    ("&#128172;","WhatsApp Transfer","Move WhatsApp chats, photos, videos and stickers between Android and iPhone.",
     ["Full chat history transferred","Photos, videos, attachments, stickers","Android to iPhone and vice versa","Also supports WhatsApp Business"]),
    ("&#128230;","Backup &amp; Restore","Back up your phone to your computer and restore to any device anytime.",
     ["Backup to PC or Mac","Restore to any phone","iCloud backup to Android","Keep multiple backup versions"]),
    ("&#128196;","18+ Data Types","Transfer contacts, photos, videos, music, SMS, apps, documents, calendar and more.",
     ["Contacts with photos and notes","Complete photo and video libraries","Music and audio files","Documents, notes and calendar"]),
    ("&#9889;","Lightning-Fast Transfer","30 MB/s average transfer speed &#8212; up to 200x faster than Bluetooth.",
     ["1GB video transfers in ~30 seconds","No WiFi required","Direct USB connection","No data usage or cloud upload"]),
    ("&#128272;","Social App Transfer","Transfer Viber, LINE, WeChat and Kik chat data between devices.",
     ["Viber chat history and media","LINE messages and stickers","WeChat backup and restore","Kik messages and attachments"]),
    ("&#128736;","Utility Tools","HEIC to JPG converter, duplicate contact manager and WhatsApp chat PDF export.",
     ["Convert HEIC photos to JPG/PNG","Find and merge duplicate contacts","Export WhatsApp chats to PDF or HTML","Manage phone data from your computer"]),
]

def FEATURES_GRID():
    cards = ""
    for icon,name,desc,buls in FEATURES:
        li = "".join("<li>" + b + "</li>" for b in buls)
        cards += '<div class="card"><div class="fi">' + icon + '</div><h3>' + name + '</h3><p>' + desc + '</p><ul>' + li + '</ul></div>'
    return '<div class="grid2">' + cards + '</div>'

TESTIMONIALS = [
    ("&#9733;&#9733;&#9733;&#9733;&#9733;","I switched from a Samsung Galaxy to iPhone 16 and was dreading losing 4 years of WhatsApp history. MobileTrans moved everything in 35 minutes &#8212; every chat, every photo, every sticker. Absolutely flawless.","Emma T.","London, UK &#127468;&#127463;"),
    ("&#9733;&#9733;&#9733;&#9733;&#9733;","My wife's phone had a cracked screen and we couldn't set up her new Samsung through the normal transfer process. MobileTrans worked through the broken screen via USB. Transferred 8,000 photos, contacts and all her WhatsApp. Incredible software.","David K.","Austin, USA &#127482;&#127480;"),
    ("&#9733;&#9733;&#9733;&#9733;&#9733;","I manage device upgrades for 50 employees. MobileTrans cut our device transition time by 80%. What used to take half a day per phone now takes 30 minutes including WhatsApp and app data. Worth every penny for our IT department.","Sarah M.","Toronto, Canada &#127464;&#127462;"),
    ("&#9733;&#9733;&#9733;&#9733;&#9733;","Ich habe von iOS zu Android gewechselt und dachte, meine gesamte WhatsApp-Unterhaltungsgeschichte sei verloren. MobileTrans hat alles &#252;bertragen &#8212; selbst meine Gruppenunterhaltungen von vor 3 Jahren. Fantastisch!","Klaus B.","Berlin, Deutschland &#127465;&#127466;"),
    ("&#9733;&#9733;&#9733;&#9733;&#9733;","The official Move to iOS app kept failing after 2 hours. MobileTrans transferred my entire Android phone to iPhone in 45 minutes including 12,000 photos and 3 years of WhatsApp. Should have used it first.","Priya S.","Mumbai, India &#127470;&#127475;"),
    ("&#9733;&#9733;&#9733;&#9733;&#9733;","Mon vieux Samsung &#233;tait cass&#233; et je pensais avoir perdu toutes mes photos et messages Viber. MobileTrans a tout r&#233;cup&#233;r&#233; et transf&#233;r&#233; sur mon nouveau iPhone en moins d'une heure. Excellent logiciel.","Marie D.","Paris, France &#127467;&#127479;"),
]

def TESTIMONIALS_GRID():
    cards = "".join('<div class="tcard"><div class="stars">' + s + '</div><p class="ttext">"' + t + '"</p><div class="tauthor">' + n + " &#8212; " + l + '</div></div>' for s,t,n,l in TESTIMONIALS)
    return '<div class="grid3">' + cards + '</div>'

FAQ_GLOBAL = [
    ("What is Wondershare MobileTrans?","Wondershare MobileTrans is the #1 phone-to-phone data transfer software that moves contacts, photos, videos, messages, WhatsApp and more between any two phones &#8212; including across Android and iOS &#8212; in minutes."),
    ("What data types can MobileTrans transfer?","18+ data types: contacts (with photos and notes), photos, videos, music, SMS, call logs, calendar, apps, documents, WhatsApp chat history, Viber, LINE, WeChat, Kik and more."),
    ("Can it transfer WhatsApp from Android to iPhone?","Yes &#8212; MobileTrans transfers complete WhatsApp chat history including photos, videos, attachments, stickers and voice notes from Android to iPhone and back. This is the most requested cross-platform transfer feature."),
    ("Does it work cross-platform (Android &#8596; iOS)?","Yes &#8212; MobileTrans is specifically built for cross-platform transfers. Move data from Android to iPhone, iPhone to Android, Android to Android, and iPhone to iPhone, all without ecosystem limitations."),
    ("Is there a free trial?","Yes &#8212; the free version transfers up to 20 photos and videos. WhatsApp messages, stickers and files between Android and iOS are also available in the free tier."),
    ("How fast is MobileTrans?","Average transfer speed is 30 MB/s &#8212; up to 200x faster than Bluetooth. A 1GB video transfers in approximately 30 seconds. No WiFi required &#8212; uses a direct USB connection."),
    ("Does it work without WiFi?","Yes &#8212; MobileTrans uses a direct USB cable connection between your phone and computer. No WiFi, no mobile data, no cloud upload required."),
    ("Does it work if my old phone has a broken screen?","In many cases yes &#8212; if the phone still powers on and can be connected via USB, MobileTrans can transfer data even from phones with completely shattered screens."),
    ("How many devices does MobileTrans support?","MobileTrans supports 6,000+ smartphone models including all iPhone models, Samsung Galaxy, Google Pixel, Huawei, OnePlus, Xiaomi, Motorola and more."),
    ("Can it backup to a computer?","Yes &#8212; backup your entire phone to your PC or Mac, then restore to any device. Also supports restoring from iCloud backups directly to Android."),
    ("Does it transfer iCloud data to Android?","Yes &#8212; MobileTrans can restore iCloud backup data directly to an Android device &#8212; one of the few tools that supports this cross-platform restore."),
]

def FAQ_BLOCK(pairs):
    items = "".join('<div class="faq-item"><div class="faq-q">' + q + '</div><div class="faq-a">' + a + '</div></div>' for q,a in pairs)
    return '<div class="faq-list">' + items + '</div>'

def related_cloud(kw_data, n=24):
    same = [k for k in KEYWORDS if k["cat"]==kw_data["cat"] and k["slug"]!=kw_data["slug"]]
    diff = [k for k in KEYWORDS if k["cat"]!=kw_data["cat"]]
    pool = (same+diff)[:n]
    links = "".join('<a class="kw" href="' + BASE_PATH + '/' + r["slug"] + '.html">' + r["keyword"] + '</a>' for r in pool)
    return '<div class="kw-cloud">' + links + '</div>'

def cat_deep(cat, keyword):
    bodies = {
"android-to-iphone": (
    '<section style="background:#fff"><div class="container">'
    '<div class="sec-ey">Complete Guide</div><h2>Android to iPhone &#8212; Transfer Everything</h2>'
    '<div class="prose">'
    '<p>Switching from Android to iPhone is one of the most common phone transitions &#8212; and one of the most frustrating without the right tool. Apple\'s official "Move to iOS" app frequently fails, gets stuck, times out or transfers only some data, leaving contacts or messages behind. MobileTrans handles the complete transfer directly.</p>'
    '<h3>What Gets Transferred</h3>'
    '<p>Contacts (with photos, nicknames and custom ringtones), the complete photo and video library, music, SMS messages, call logs, calendar events, documents, and WhatsApp chat history including media. The transfer happens over a direct USB connection &#8212; no WiFi required, no mobile data used, no cloud upload needed.</p>'
    '<h3>WhatsApp &#8212; The Hard Part Made Easy</h3>'
    '<p>The most commonly lost data when switching from Android to iPhone is WhatsApp. Apple and Google\'s separate cloud systems mean your Google Drive WhatsApp backup cannot be restored to an iPhone. MobileTrans solves this by reading the Android WhatsApp backup directly and writing it to the iPhone &#8212; transferring the complete chat history, media, stickers and voice notes regardless of which OS each backup was created on.</p>'
    '<h3>When Move to iOS Fails</h3>'
    '<p>If the official Move to iOS app failed, timed out, or missed some files, MobileTrans is the correct next step. Connect both phones via USB, select what you need, and transfer only the missing data without overwriting what did transfer. This targeted transfer capability is unique to MobileTrans.</p>'
    '</div></div></section>'),

"iphone-to-android": (
    '<section style="background:#fff"><div class="container">'
    '<div class="sec-ey">Complete Guide</div><h2>iPhone to Android &#8212; Transfer Without Losing Data</h2>'
    '<div class="prose">'
    '<p>Switching from iPhone to Android is technically more complex than the reverse. Apple\'s ecosystem keeps data in iCloud and proprietary formats that Android cannot natively read. MobileTrans bridges this gap by reading directly from the iPhone and writing in formats compatible with your new Android device.</p>'
    '<h3>What Gets Transferred</h3>'
    '<p>Contacts, full photo library (HEIC files automatically converted to JPG for Android compatibility), videos, music, SMS messages, calendar events, documents and WhatsApp chat history. The HEIC to JPG conversion is automatic &#8212; no manual conversion needed.</p>'
    '<h3>WhatsApp from iPhone to Android</h3>'
    '<p>This is the direction WhatsApp officially doesn\'t support &#8212; the iOS and Android backup systems are entirely separate and incompatible. MobileTrans extracts the WhatsApp data directly from the iPhone and transfers it to the Android device, bypassing the official backup system entirely. This is the only reliable method for transferring WhatsApp from iPhone to Android.</p>'
    '<h3>iCloud Data to Android</h3>'
    '<p>MobileTrans can also restore iCloud backup data directly to an Android device &#8212; recovering contacts, photos and documents stored in iCloud and placing them on your new Android phone without needing an iPhone as an intermediary.</p>'
    '</div></div></section>'),

"whatsapp": (
    '<section style="background:#fff"><div class="container">'
    '<div class="sec-ey">WhatsApp Transfer Guide</div><h2>Transfer WhatsApp to Any Phone</h2>'
    '<div class="prose">'
    '<p>WhatsApp is the data most people are afraid of losing when switching phones &#8212; years of conversations, photos, voice notes and memories that exist nowhere else. The official WhatsApp backup system ties Android backups to Google Drive and iPhone backups to iCloud, making cross-platform transfers officially impossible. MobileTrans solves this.</p>'
    '<h3>Why Official WhatsApp Transfer Often Fails</h3>'
    '<p>When you switch from Android to iPhone, your Google Drive WhatsApp backup cannot be restored to iOS. When you switch from iPhone to Android, your iCloud WhatsApp backup cannot be restored to Android. Official solutions only work within the same platform, and even same-platform transfers sometimes fail due to backup file size, iCloud storage limits or sync errors.</p>'
    '<h3>What MobileTrans Transfers</h3>'
    '<p>Complete chat history including all personal and group conversations, all media attachments (photos, videos, audio messages, documents, stickers), contact details from the chats, and voice notes. The transferred WhatsApp data appears in your new phone exactly as it was on your old phone.</p>'
    '<h3>WhatsApp Business</h3>'
    '<p>MobileTrans fully supports WhatsApp Business accounts including chat history, contacts, product catalogues and business-specific settings. Also supports Viber, LINE, WeChat and Kik for users who need to transfer other messaging app data simultaneously.</p>'
    '</div></div></section>'),

"backup": (
    '<section style="background:#fff"><div class="container">'
    '<div class="sec-ey">Backup Guide</div><h2>Backup Your Phone to Your Computer</h2>'
    '<div class="prose">'
    '<p>Having a local backup of your phone on your computer provides a safety net that cloud backups alone cannot match. If you lose your phone, it breaks or you want to restore to a different device, a local backup is available instantly &#8212; no internet speed limitations, no cloud storage limits, no subscription fees.</p>'
    '<h3>What Gets Backed Up</h3>'
    '<p>Contacts, photos, videos, music, SMS messages, call logs, calendar events, documents, and WhatsApp data. The backup is stored on your PC or Mac in an organised, browsable format. You can choose to back up everything or select specific data types.</p>'
    '<h3>Restore to Any Device</h3>'
    '<p>Unlike iCloud backups (which only restore to iPhones) and Google Drive backups (which only restore to Android), MobileTrans backups can be restored to any supported device regardless of operating system. This is particularly valuable when switching platforms or replacing a lost/stolen phone with a different brand.</p>'
    '<h3>iCloud Backup to Android</h3>'
    '<p>MobileTrans uniquely supports restoring iCloud backup data directly to an Android device. Connect the Android phone, authenticate with your Apple ID, and MobileTrans retrieves the iCloud backup and restores selected data to the Android device &#8212; bridging the Apple-Google divide that normally makes this impossible.</p>'
    '</div></div></section>'),

"iphone": (
    '<section style="background:#fff"><div class="container">'
    '<div class="sec-ey">iPhone Transfer Guide</div><h2>iPhone Data Transfer &#8212; Complete Guide</h2>'
    '<div class="prose">'
    '<p>Every iPhone transfer scenario &#8212; from another iPhone, from Android, to Android, or just backing up to a computer &#8212; is handled by MobileTrans in a single application. No more choosing between different tools for different scenarios.</p>'
    '<h3>iPhone to iPhone</h3>'
    '<p>Transferring to a new iPhone is the simplest scenario. MobileTrans moves your complete data library &#8212; photos, contacts, messages, WhatsApp, music and more &#8212; via USB in minutes. Unlike iCloud transfer, there are no storage limits and no waiting for cloud upload/download. Unlike iTunes/Finder restore, you can select exactly which data to transfer rather than everything or nothing.</p>'
    '<h3>Transfer Speed</h3>'
    '<p>At 30 MB/s average speed, MobileTrans is up to 200x faster than Bluetooth transfer. A 1GB video file transfers in approximately 30 seconds. A typical phone with 15GB of data transfers in 8-10 minutes. The direct USB connection eliminates the upload-wait-download cycle of any cloud-based method.</p>'
    '<h3>What Transfers to iPhone</h3>'
    '<p>Photos and videos (at full original resolution), contacts with all fields, SMS and iMessage-compatible messages, music, documents, calendar events and WhatsApp history. App data is transferred for supported apps. The transferred content appears exactly as it was on the source device.</p>'
    '</div></div></section>'),

"compare": (
    '<section style="background:#fff"><div class="container">'
    '<div class="sec-ey">Honest Comparison</div><h2>' + keyword + ' &#8212; Analysis</h2>'
    '<div class="prose">'
    '<p>Choosing the right phone transfer tool matters &#8212; the wrong choice means missing data, failed transfers or starting over on a new phone. Here is an honest assessment of MobileTrans against the main alternatives.</p>'
    '<h3>MobileTrans vs Move to iOS (Free, Apple)</h3>'
    '<p>Move to iOS is free and works well for standard Android-to-iPhone transfers. However, it frequently fails, times out, misses files or produces incomplete transfers &#8212; particularly for large libraries or when the phones are on different WiFi channels. MobileTrans uses a direct USB connection that is faster and more reliable. It also transfers WhatsApp, which Move to iOS does not.</p>'
    '<h3>MobileTrans vs iCloud/Google Drive</h3>'
    '<p>Cloud backups only restore within the same ecosystem. iCloud backups restore to iPhones only; Google Drive backups to Android only. For cross-platform transfers, cloud methods literally cannot work. MobileTrans bridges this gap, reading from any source and writing to any destination.</p>'
    '<h3>MobileTrans vs iTunes/Finder Backup</h3>'
    '<p>iTunes and Finder only back up iPhones, only restore to iPhones, and restore everything or nothing. MobileTrans offers selective transfer, cross-platform support and can extract specific data types rather than restoring a full device backup.</p>'
    '</div></div></section>'),

"howto": (
    '<section style="background:#fff"><div class="container">'
    '<div class="sec-ey">Step-by-Step Guide</div><h2>' + keyword + ' &#8212; Exact Steps</h2>'
    '<div class="prose">'
    '<p>MobileTrans follows a simple three-step process for every transfer scenario. Here is exactly what to do.</p>'
    '<h3>Step 1 &#8212; Connect Both Phones</h3>'
    '<p>Install MobileTrans on your Windows PC or Mac. Connect both phones using USB cables. MobileTrans detects both devices automatically &#8212; the source phone on the left, the destination on the right. Ensure both phones are unlocked and trust the computer when prompted.</p>'
    '<h3>Step 2 &#8212; Select Data to Transfer</h3>'
    '<p>Choose which data types you want to transfer: photos, contacts, messages, WhatsApp, music, or all available types. You can transfer everything or select specific categories. MobileTrans shows you what will be transferred before starting.</p>'
    '<h3>Step 3 &#8212; Transfer</h3>'
    '<p>Click Transfer. Keep both phones connected via USB throughout the process. Do not use either phone during transfer. The progress bar shows real-time status. When complete, verify your data on the destination phone.</p>'
    '<h3>Important Notes</h3>'
    '<p>Keep both phones plugged into power during long transfers. Unlock both phones before starting. For WhatsApp transfer, ensure WhatsApp is installed and set up on the destination phone before starting.</p>'
    '</div></div></section>'),
    }
    body = bodies.get(cat)
    if body: return body
    aff = AFFILIATE_URL
    return ('<section style="background:#fff"><div class="container">'
            '<div class="sec-ey">Complete Guide</div>'
            '<h2>' + keyword + ' &#8212; Overview</h2>'
            '<div class="prose">'
            '<p>Wondershare MobileTrans is the #1 phone transfer solution for ' + keyword.lower() + '. '
            'It transfers 18+ data types between 6,000+ devices at 30 MB/s &#8212; up to 200x faster than Bluetooth &#8212; '
            'with full cross-platform support between Android and iOS.</p>'
            '<p>Whether switching phones, moving between Android and iPhone, transferring WhatsApp, '
            'or backing up to your computer, MobileTrans handles every scenario in a simple three-step process '
            'that requires no technical expertise.</p>'
            '<h3>Why MobileTrans?</h3>'
            '<p>1.5 million+ users, 6,000+ supported devices, 18+ data types, '
            'WhatsApp transfer across platforms, no WiFi required, no cloud upload, '
            'and a free trial that transfers up to 20 photos at no cost.</p>'
            '</div>'
            '<div style="margin-top:2rem">'
            '<a href="' + aff + '" class="btn-p" target="_blank" rel="nofollow sponsored">&#8659; Download Free Trial</a>'
            '</div></div></section>')

def build_keyword_page(kw_data):
    slug=kw_data["slug"]; keyword=kw_data["keyword"]; cat=kw_data["cat"]
    a1,a2=ac(cat)
    title  = keyword + " &#8212; Wondershare MobileTrans | " + str(YEAR)
    desc   = ("Need " + keyword.lower() + "? MobileTrans transfers 18+ data types between 6,000+ devices. "
              "WhatsApp included. Free trial &#8212; Windows & Mac.")
    canon  = slug + ".html"
    faq_pairs = [
        ("Can MobileTrans handle " + keyword.lower() + "?",
         "Yes &#8212; MobileTrans is specifically built for " + keyword.lower() + ". "
         "It transfers 18+ data types between 6,000+ devices at 30 MB/s, "
         "including full WhatsApp transfer across Android and iOS. Free trial available."),
        ("Is there a free version for " + keyword.lower() + "?",
         "Yes &#8212; the free trial transfers up to 20 photos and videos, "
         "plus WhatsApp messages and stickers between Android and iOS. Full transfers require a license."),
        ("How long does " + keyword.lower() + " take with MobileTrans?",
         "At 30 MB/s average speed, a typical phone transfer takes 8-15 minutes. "
         "A 1GB video transfers in about 30 seconds. "
         "Transfer time depends on the amount of data and data types selected."),
    ]
    bc_s  = BC_SCHEMA([("Home",""),("All Topics","keywords.html"),(keyword,"")])
    fq_s  = FAQ_SCHEMA(faq_pairs)
    body  = cat_deep(cat, keyword)
    same  = [k for k in KEYWORDS if k["cat"]==cat and k["slug"]!=slug][:6]
    links = " &#183; ".join('<a href="' + BASE_PATH + '/' + r["slug"] + '.html">' + r["keyword"] + '</a>' for r in same)

    return (HEAD(title, desc, canon, bc_s+fq_s)
        + "\n<body>\n"
        + "<style>:root{--ha:" + a1 + ";--hb:" + a2 + ";--fa:rgba(0,0,0,.05)}</style>\n"
        + NAV() + "\n"
        + BC([("Home",BASE_PATH+"/"),("All Topics",BASE_PATH+"/keywords.html"),(keyword,"")])
        + '\n<section class="hero">'
        + '\n  <div class="eyebrow">&#10022; ' + cat.replace("-"," ").title() + '</div>'
        + '\n  <h1><em>' + keyword + '</em><br>&#8212; With MobileTrans</h1>'
        + '\n  <p class="hsub">18+ data types &#183; 6,000+ devices &#183; WhatsApp included &#183; Free trial</p>'
        + '\n  <div class="btns">'
        + '\n    <a href="' + AFFILIATE_URL + '" class="btn-p" target="_blank" rel="nofollow sponsored">&#8659; Download Free Trial</a>'
        + '\n    <a href="' + BASE_PATH + '/how-it-works.html" class="btn-s">How It Works</a>'
        + '\n  </div>'
        + '\n  <div class="stats">'
        + '\n    <div><span class="stat-n">1.5M+</span><span class="stat-l">Users</span></div>'
        + '\n    <div><span class="stat-n">6,000+</span><span class="stat-l">Devices</span></div>'
        + '\n    <div><span class="stat-n">18+</span><span class="stat-l">Data Types</span></div>'
        + '\n    <div><span class="stat-n">30 MB/s</span><span class="stat-l">Transfer Speed</span></div>'
        + '\n  </div>\n</section>\n'
        + '\n<section><div class="container">'
        + '\n  <div class="sec-ey">All Features</div>'
        + '\n  <h2>Everything You Need for ' + keyword.title() + '</h2>'
        + FEATURES_GRID()
        + '\n</div></section>\n'
        + body
        + '\n<section style="background:#e0f2fe"><div class="container">'
        + '\n  <div class="sec-ey">Real Users</div><h2>Trusted by 1.5 Million Users</h2>'
        + TESTIMONIALS_GRID()
        + '\n</div></section>\n'
        + '\n<section><div class="container">'
        + '\n  <div class="sec-ey">FAQ</div><h2>Common Questions</h2>'
        + FAQ_BLOCK(faq_pairs + FAQ_GLOBAL[:3])
        + '\n  <div style="margin-top:1.5rem">'
        + '\n    <a href="' + BASE_PATH + '/faq.html" style="color:var(--ha);font-weight:600;font-size:.88rem">View all FAQs &#8594;</a>'
        + '\n  </div>\n</div></section>\n'
        + '\n<section class="dark-sec"><div class="container">'
        + '\n  <div class="sec-ey">Related Topics</div><h2>Explore More</h2>'
        + related_cloud(kw_data, 28)
        + ('\n  <p style="margin-top:1.4rem;font-size:.78rem;color:rgba(255,255,255,.35)">More: ' + links + '</p>' if links else '')
        + '\n</div></section>\n'
        + CTA("Transfer " + keyword.title() + " Now","Download MobileTrans free and transfer up to 20 photos at no cost.")
        + "\n" + FOOTER() + "\n" + FAQ_JS + "\n</body></html>")

def page_index():
    extra = FAQ_SCHEMA(FAQ_GLOBAL[:6]) + BC_SCHEMA([("Home","")])
    transfers = [
        ("&#129318;","Android to iPhone","android-to-iphone-transfer","Samsung, Pixel &#8594; iPhone"),
        ("&#128241;","iPhone to Android","iphone-to-android-transfer","iPhone &#8594; Samsung, Pixel"),
        ("&#128242;","iPhone to iPhone","transfer-iphone-to-iphone","New iPhone setup"),
        ("&#128172;","WhatsApp Transfer","whatsapp-transfer","Android &#8596; iPhone"),
        ("&#128190;","Phone Backup","backup-phone-to-computer","Backup to PC or Mac"),
        ("&#128230;","Broken Phone","iphone-transfer-software","Cracked screen transfer"),
        ("&#127760;","iCloud to Android","icloud-to-android","Apple &#8594; Google"),
        ("&#128736;","Contacts &amp; SMS","iphone-transfer-contacts","Selective data transfer"),
    ]
    tg = "".join('<a class="tr-card" href="' + BASE_PATH + '/' + s + '.html"><span class="trc-icon">' + i + '</span><span class="trc-label">' + n + '</span><span class="trc-sub">' + d + '</span></a>' for i,n,s,d in transfers)

    return (HEAD("MobileTrans &#8212; #1 Phone Transfer App | iPhone, Android, WhatsApp | " + str(YEAR),
                 "Transfer everything to your new phone with MobileTrans. 18+ data types, WhatsApp included, 6,000+ devices. Free trial.",
                 "", extra)
        + "\n<body>\n" + NAV()
        + '\n<section class="hero">'
        + '\n  <div class="eyebrow">&#10022; #1 Phone Transfer App</div>'
        + '\n  <h1>Switch Phones.<br><em>Keep Everything.</em></h1>'
        + '\n  <p class="hsub">Transfer contacts, photos, WhatsApp and 18+ data types between any phones &#8212; Android to iPhone, iPhone to Android or any combination. Free trial available.</p>'
        + '\n  <div class="btns">'
        + '\n    <a href="' + AFFILIATE_URL + '" class="btn-p" target="_blank" rel="nofollow sponsored">&#8659; Download Free Trial</a>'
        + '\n    <a href="' + BASE_PATH + '/how-it-works.html" class="btn-s">How It Works</a>'
        + '\n  </div>'
        + '\n  <div class="stats">'
        + '\n    <div><span class="stat-n">1.5M+</span><span class="stat-l">Users Worldwide</span></div>'
        + '\n    <div><span class="stat-n">6,000+</span><span class="stat-l">Devices Supported</span></div>'
        + '\n    <div><span class="stat-n">18+</span><span class="stat-l">Data Types</span></div>'
        + '\n    <div><span class="stat-n">30 MB/s</span><span class="stat-l">Transfer Speed</span></div>'
        + '\n  </div>\n</section>\n'
        + '\n<section style="background:#fff"><div class="container">'
        + '\n  <div class="sec-ey">What Do You Need to Do?</div>'
        + '\n  <h2>Every Phone Transfer Scenario Covered</h2>'
        + '\n  <p class="sec-sub">Click your scenario &#8212; or download MobileTrans and start now.</p>'
        + '\n  <div class="tr-grid">' + tg + '</div>'
        + '\n</div></section>\n'
        + '\n<section><div class="container">'
        + '\n  <div class="sec-ey">Complete Feature Suite</div>'
        + '\n  <h2>Everything for Your New Phone Setup</h2>'
        + '\n  <p class="sec-sub">One app for every transfer scenario &#8212; cross-platform, cross-brand, WhatsApp included.</p>'
        + FEATURES_GRID()
        + '\n  <div style="margin-top:2.5rem;text-align:center">'
        + '\n    <a href="' + BASE_PATH + '/features.html" style="color:var(--ha);font-weight:600">View full feature list &#8594;</a>'
        + '\n  </div>\n</div></section>\n'
        + '\n<section style="background:#fff"><div class="container">'
        + '\n  <div class="sec-ey">Why MobileTrans Beats Free Options</div>'
        + '\n  <h2>When the Official Tools Fail</h2>'
        + '\n  <div class="grid3">'
        + '\n    <div class="card"><div class="fi">&#10060;</div><h3>Move to iOS Keeps Failing</h3><p>Apple\'s free app frequently times out, misses files or transfers incomplete data. MobileTrans uses a direct USB connection that doesn\'t rely on WiFi stability.</p></div>'
        + '\n    <div class="card"><div class="fi">&#128172;</div><h3>WhatsApp Won\'t Cross Platforms</h3><p>Google Drive backups can\'t restore to iPhone. iCloud backups can\'t restore to Android. MobileTrans is the only reliable solution for cross-platform WhatsApp transfer.</p></div>'
        + '\n    <div class="card"><div class="fi">&#128187;</div><h3>iCloud Has Only 5GB Free</h3><p>Most people have far more than 5GB of phone data. MobileTrans backs up directly to your computer &#8212; unlimited storage, no subscription needed.</p></div>'
        + '\n  </div>\n</div></section>\n'
        + '\n<section style="background:#e0f2fe"><div class="container">'
        + '\n  <div class="sec-ey">Real Users</div>'
        + '\n  <h2 style="text-align:center;margin-bottom:2.5rem">Trusted by 1.5 Million Users Worldwide</h2>'
        + TESTIMONIALS_GRID()
        + '\n</div></section>\n'
        + '\n<section><div class="container">'
        + '\n  <div class="sec-ey">FAQ</div><h2>Common Questions About MobileTrans</h2>'
        + FAQ_BLOCK(FAQ_GLOBAL[:6])
        + '\n  <div style="margin-top:1.5rem;text-align:center">'
        + '\n    <a href="' + BASE_PATH + '/faq.html" style="color:var(--ha);font-weight:600">View all FAQs &#8594;</a>'
        + '\n  </div>\n</div></section>\n'
        + CTA() + "\n" + FOOTER() + "\n" + FAQ_JS + "\n</body></html>")

def page_features():
    bc = BC_SCHEMA([("Home",""),("Features","")])
    rows = [
        ("Phone to Phone Transfer",   "V","V","V","V","V"),
        ("Android to iPhone",         "V","V","Partial","Limited","X"),
        ("iPhone to Android",         "V","V","Partial","Limited","X"),
        ("WhatsApp Transfer",         "V","V","X","X","X"),
        ("WhatsApp Android&#8596;iOS","V","Limited","X","X","X"),
        ("iCloud to Android",         "V","X","X","X","X"),
        ("Backup to Computer",        "V","V","V","V","V"),
        ("Viber/LINE/WeChat",         "V","X","X","X","X"),
        ("Broken Phone Transfer",     "V","V","Partial","X","X"),
        ("6,000+ Devices",            "V","V","V","V","V"),
        ("18+ Data Types",            "V","V","Partial","Partial","X"),
        ("Free Trial",                "V","V","V","V","Limited"),
    ]
    tools = ["MobileTrans &#10022;","Dr.Fone","iMazing","AnyTrans","Manual/iTunes"]
    hrow = "<tr><th>Feature</th>" + "".join(('<th class="hl">' if i==0 else '<th>') + t + '</th>' for i,t in enumerate(tools)) + "</tr>"
    def cell(v,i):
        if i==0: return '<td class="ck" style="font-weight:700">' + v + '</td>'
        if v=="V": return '<td class="ck">&#10004;</td>'
        if v=="X": return '<td class="cr">&#10008;</td>'
        return '<td class="cp">' + v + '</td>'
    trows = "".join("<tr>" + cell(r[0],-1) + "".join(cell(v,i) for i,v in enumerate(r[1:])) + "</tr>" for r in rows)
    return (HEAD("MobileTrans Features &#8212; Phone Transfer, WhatsApp, Backup &amp; More | " + str(YEAR),
                 "Complete MobileTrans feature list: phone transfer, WhatsApp cross-platform, iCloud to Android, backup, Viber, LINE, WeChat.",
                 "features.html", bc)
        + "\n<body>\n" + NAV()
        + "\n" + BC([("Home",BASE_PATH+"/"),("Features","")])
        + '\n<section class="hero"><div class="eyebrow">&#10022; Complete Feature List</div>'
        + '\n  <h1>Everything MobileTrans<br><em>Can Do</em></h1>'
        + '\n  <p class="hsub">Phone transfer &#183; WhatsApp &#183; Backup &amp; Restore &#183; 18+ data types &#183; 6,000+ devices</p>'
        + '\n  <a href="' + AFFILIATE_URL + '" class="btn-p" target="_blank" rel="nofollow sponsored">&#8659; Download Free Trial</a>'
        + '\n</section>\n'
        + '\n<section><div class="container"><div class="sec-ey">All Feature Areas</div><h2>The Complete Transfer Toolkit</h2>'
        + FEATURES_GRID()
        + '\n</div></section>\n'
        + '\n<section style="background:#fff"><div class="container"><div class="sec-ey">Comparison</div><h2>MobileTrans vs Alternatives</h2>'
        + '\n  <div class="tbl-wrap"><table><thead>' + hrow + '</thead><tbody>' + trows + '</tbody></table></div>'
        + '\n  <p style="margin-top:.9rem;font-size:.75rem;color:var(--muted)">&#10004; Full &#160; Partial/Limited = Limited &#160; &#10008; Not available</p>'
        + '\n</div></section>\n'
        + CTA("Try All Features Free","Download MobileTrans &#8212; transfer up to 20 photos free, no credit card required.")
        + "\n" + FOOTER() + "\n</body></html>")

def page_how_it_works():
    bc = BC_SCHEMA([("Home",""),("How It Works","")])
    return (HEAD("How MobileTrans Works &#8212; 3 Steps to Transfer Your Phone | " + str(YEAR),
                 "Transfer your phone data in 3 steps: connect both phones, select data, transfer. Works for Android to iPhone, iPhone to Android and WhatsApp.",
                 "how-it-works.html", bc)
        + "\n<body>\n" + NAV()
        + "\n" + BC([("Home",BASE_PATH+"/"),("How It Works","")])
        + '\n<section class="hero"><div class="eyebrow">&#10022; Simple Process</div>'
        + '\n  <h1>Transfer Your Phone in<br><em>3 Simple Steps</em></h1>'
        + '\n  <p class="hsub">Connect both phones, select what to transfer, done. Works for any phones, any platforms.</p>'
        + '\n  <a href="' + AFFILIATE_URL + '" class="btn-p" target="_blank" rel="nofollow sponsored">&#8659; Download Free Trial</a>'
        + '\n</section>\n'
        + '\n<section><div class="container"><div class="sec-ey">The Process</div><h2>3 Steps to Your New Phone</h2>'
        + '\n  <div class="steps">'
        + '\n    <div class="step"><div class="sn">1</div><h3>Connect Both Phones</h3><p>Connect your old and new phones to your PC or Mac using USB cables. MobileTrans detects both devices automatically. Unlock both phones and trust the computer when prompted.</p></div>'
        + '\n    <div class="step"><div class="sn">2</div><h3>Select Data to Transfer</h3><p>Choose what to move: contacts, photos, WhatsApp, music, SMS &#8212; or select everything. MobileTrans shows exactly what will be transferred before you start.</p></div>'
        + '\n    <div class="step"><div class="sn">3</div><h3>Transfer</h3><p>Click Transfer and keep both phones connected. The progress bar shows real-time status. At 30 MB/s, most transfers complete in 8-15 minutes.</p></div>'
        + '\n  </div>\n</div></section>\n'
        + '\n<section style="background:#fff"><div class="container"><div class="sec-ey">Why USB Beats WiFi</div><h2>Direct USB &#8212; Faster and More Reliable</h2>'
        + '\n  <div class="grid2">'
        + '\n    <div class="card"><div class="fi">&#9889;</div><h3>200x Faster Than Bluetooth</h3><p>At 30 MB/s, MobileTrans is up to 200x faster than Bluetooth. A 1GB video transfers in about 30 seconds. A full 15GB phone in 8-10 minutes. No WiFi signal required &#8212; works anywhere.</p></div>'
        + '\n    <div class="card"><div class="fi">&#128204;</div><h3>No Dropped Connections</h3><p>WiFi-based transfers (Move to iOS, Bluetooth) frequently drop, time out or get stuck. USB maintains a stable direct connection for the entire transfer &#8212; no risk of interruption halfway through.</p></div>'
        + '\n  </div>\n</div></section>\n'
        + '\n<section style="background:#fff"><div class="container" style="padding-top:0"><div class="sec-ey">Special Scenarios</div><h2>When the Official Tools Won\'t Work</h2>'
        + '\n  <div class="grid3">'
        + '\n    <div class="card"><div class="fi">&#128172;</div><h3>WhatsApp Across Platforms</h3><p>Google Drive can\'t restore to iPhone. iCloud can\'t restore to Android. MobileTrans is the only reliable cross-platform WhatsApp transfer solution.</p></div>'
        + '\n    <div class="card"><div class="fi">&#128247;</div><h3>Broken Screen Phones</h3><p>If your old phone has a cracked screen but still powers on, MobileTrans can transfer data via USB without needing to navigate the touchscreen.</p></div>'
        + '\n    <div class="card"><div class="fi">&#127760;</div><h3>iCloud to Android</h3><p>Restore your iCloud backup data directly to a new Android phone &#8212; without needing an iPhone as an intermediary.</p></div>'
        + '\n  </div>\n</div></section>\n'
        + '\n<section style="background:#e0f2fe"><div class="container"><div class="sec-ey">Real Results</div><h2>What Users Experience</h2>'
        + TESTIMONIALS_GRID()
        + '\n</div></section>\n'
        + CTA("Start Your Phone Transfer","Download MobileTrans free and transfer up to 20 photos at no cost.")
        + "\n" + FOOTER() + "\n</body></html>")

def page_faq():
    all_faqs = FAQ_GLOBAL + [
        ("What happens to my old phone data after transfer?","MobileTrans only copies data &#8212; it does not delete anything from your old phone. Your old phone remains unchanged after the transfer. You can factory reset it yourself once you've confirmed everything transferred correctly."),
        ("Can MobileTrans transfer app data?","Yes &#8212; MobileTrans can transfer app data for supported apps. WhatsApp, Viber, LINE, WeChat and Kik chat data is fully supported. For other apps, transfer coverage depends on the app and operating system."),
        ("Do both phones need to be unlocked during transfer?","Yes &#8212; both phones need to be unlocked and connected to the computer for the duration of the transfer. Enable 'Trust This Computer' on iPhone when prompted."),
        ("What if I only want to transfer some data, not everything?","MobileTrans lets you select specific data types to transfer. You can choose to transfer only contacts, only photos, only WhatsApp &#8212; or any combination. You don't need to transfer everything."),
        ("Can I use MobileTrans on Mac?","Yes &#8212; MobileTrans is available for both Windows (7/8/10/11) and macOS (10.12+). Full support for Intel and Apple Silicon Macs."),
        ("Does it work with the latest iPhone models?","Yes &#8212; MobileTrans supports all iPhone models including the latest iPhone 16 and iPhone 17. iOS 18 and iOS 26 are supported."),
        ("Can it transfer from Google Drive to a new phone?","Yes &#8212; MobileTrans can access Google Drive backup data and transfer it to a new Android or iPhone device."),
    ]
    fq = FAQ_SCHEMA(all_faqs)
    bc = BC_SCHEMA([("Home",""),("FAQ","")])
    return (HEAD("MobileTrans FAQ &#8212; " + str(len(all_faqs)) + " Questions Answered | " + str(YEAR),
                 "Every question about Wondershare MobileTrans answered &#8212; WhatsApp transfer, cross-platform, speed, free trial and device support.",
                 "faq.html", fq+bc)
        + "\n<body>\n" + NAV()
        + "\n" + BC([("Home",BASE_PATH+"/"),("FAQ","")])
        + '\n<section class="hero"><div class="eyebrow">&#10022; Complete FAQ</div>'
        + '\n  <h1>Every Question About<br><em>MobileTrans Answered</em></h1>'
        + '\n  <p class="hsub">' + str(len(all_faqs)) + ' questions &#8212; WhatsApp, cross-platform, speed, free trial and devices.</p>'
        + '\n</section>\n'
        + '\n<section><div class="container"><div class="sec-ey">All ' + str(len(all_faqs)) + ' Questions</div><h2>Complete FAQ</h2>'
        + FAQ_BLOCK(all_faqs)
        + '\n</div></section>\n'
        + CTA("Ready to Switch Phones? Download Free","Transfer up to 20 photos free &#8212; no credit card required.")
        + "\n" + FOOTER() + "\n" + FAQ_JS + "\n</body></html>")

def page_compare():
    bc = BC_SCHEMA([("Home",""),("Compare","")])
    comps = [
        ("vs Move to iOS (Free, Apple)","Apple's free Move to iOS app frequently fails, times out or misses files &#8212; particularly for large photo libraries or unstable WiFi. MobileTrans uses a direct USB connection that is faster and more reliable. Critically, Move to iOS doesn't transfer WhatsApp. MobileTrans does."),
        ("vs iCloud/Google Drive","Cloud backups only restore within the same ecosystem. iCloud restores to iPhones only. Google Drive restores to Android only. For cross-platform transfers, MobileTrans is the only option. For storage, iCloud's free tier is just 5GB &#8212; MobileTrans backs up to your computer with unlimited storage."),
        ("vs iTunes/Finder Backup","iTunes and Finder back up and restore iPhones only. No Android support, no selective transfer &#8212; everything or nothing. MobileTrans supports any phone, any platform and selective data type transfer."),
        ("vs Dr.Fone Phone Transfer","Dr.Fone is a capable competitor. MobileTrans has broader WhatsApp cross-platform support &#8212; particularly for iOS-to-Android WhatsApp transfer where Dr.Fone's coverage is more limited. MobileTrans also supports Viber, LINE, WeChat and Kik transfer which Dr.Fone doesn't cover."),
    ]
    comp_cards = "".join('<div class="card"><h3>' + n + '</h3><p style="font-size:.87rem;color:var(--muted)">' + d + '</p></div>' for n,d in comps)
    return (HEAD("MobileTrans vs Alternatives &#8212; Best Phone Transfer App " + str(YEAR),
                 "MobileTrans vs Move to iOS, iCloud, iTunes, Dr.Fone and more. Honest comparison of phone transfer software.",
                 "compare.html", bc)
        + "\n<body>\n" + NAV()
        + "\n" + BC([("Home",BASE_PATH+"/"),("Compare","")])
        + '\n<section class="hero"><div class="eyebrow">&#10022; Comparison ' + str(YEAR) + '</div>'
        + '\n  <h1>MobileTrans vs<br><em>Every Alternative</em></h1>'
        + '\n  <p class="hsub">Honest comparison &#8212; transfer capability, WhatsApp support, speed and pricing.</p>'
        + '\n  <a href="' + AFFILIATE_URL + '" class="btn-p" target="_blank" rel="nofollow sponsored">&#8659; Download MobileTrans Free</a>'
        + '\n</section>\n'
        + '\n<section style="background:#fff"><div class="container"><div class="sec-ey">Head-to-Head</div><h2>vs Every Alternative</h2>'
        + '\n  <div class="grid2">' + comp_cards + '</div>'
        + '\n</div></section>\n'
        + '\n<section><div class="container"><div class="sec-ey">The Critical Difference</div><h2>The Only Cross-Platform WhatsApp Transfer</h2>'
        + '\n  <div class="prose"><p>The single most important differentiator for MobileTrans is cross-platform WhatsApp transfer. Every competitor fails at this or has severe limitations. MobileTrans transfers complete WhatsApp chat history, media, stickers and voice notes from Android to iPhone and from iPhone to Android &#8212; the only software that reliably handles both directions.</p>'
        + '\n    <p>For the millions of people switching between Android and iPhone every year who don\'t want to lose their WhatsApp history, MobileTrans is not just a better option &#8212; it\'s the only option that actually works.</p>'
        + '\n  </div>\n</div></section>\n'
        + CTA("The #1 Phone Transfer App &#8212; Try Free","Download MobileTrans and start your transfer today.")
        + "\n" + FOOTER() + "\n</body></html>")

BLOG_POSTS = [
    {"slug":"how-to-transfer-android-to-iphone","title":"How to Transfer Everything from Android to iPhone","excerpt":"Switching to iPhone? Here's the complete guide to moving all your data — including WhatsApp — from Android to iPhone without losing anything.","cat":"Android to iPhone","read":"8 min","date":"2025-01-15",
     "body":"<h2>Why Android to iPhone Transfer Is Tricky</h2><p>Android and iOS are entirely separate ecosystems with different file formats, different cloud services and different app platforms. Apple's 'Move to iOS' app handles the basics but frequently fails, misses files or times out &#8212; and it doesn't transfer WhatsApp at all.</p><h2>What Gets Transferred with MobileTrans</h2><ul><li>Contacts (with photos, notes and custom fields)</li><li>Full photo and video library at original quality</li><li>Music files</li><li>SMS and text messages</li><li>Calendar events and reminders</li><li>Documents and files</li><li>WhatsApp chat history including media and stickers</li></ul><h2>Step-by-Step</h2><ol><li>Download and install MobileTrans on your PC or Mac</li><li>Connect both phones via USB cables</li><li>Unlock both phones and trust the computer on iPhone</li><li>Select 'Phone Transfer' in MobileTrans &#8212; Android on left, iPhone on right</li><li>Select the data types to transfer</li><li>Click Transfer and keep phones connected throughout</li></ol><h2>WhatsApp &#8212; The Special Case</h2><p>For WhatsApp transfer, use the dedicated WhatsApp Transfer module in MobileTrans. This reads the Android WhatsApp backup directly and writes it to the iPhone &#8212; bypassing the Google Drive/iCloud incompatibility that makes cross-platform WhatsApp transfer impossible with official tools.</p>"},
    {"slug":"how-to-transfer-iphone-to-android","title":"How to Transfer iPhone Data to Android","excerpt":"Moving to Android? Here's how to transfer contacts, photos, WhatsApp and everything else from your iPhone to your new Android phone.","cat":"iPhone to Android","read":"7 min","date":"2025-02-10",
     "body":"<h2>iPhone to Android Is the Harder Direction</h2><p>Apple's ecosystem keeps data in formats and services that Android can't natively read. HEIC photos, iCloud-only contacts and iMessage threads all require special handling. MobileTrans manages all of this automatically.</p><h2>HEIC Photo Conversion</h2><p>iPhone photos saved in HEIC format are automatically converted to JPG during the transfer. You don't need to manually convert anything &#8212; your photos arrive on the Android device in a format every app can read.</p><h2>WhatsApp iPhone to Android</h2><p>This is the direction WhatsApp officially doesn't support. iCloud WhatsApp backups cannot be restored to Android. MobileTrans extracts the WhatsApp data directly from the iPhone and transfers it to the Android device &#8212; the only reliable method for this direction.</p><h2>Step-by-Step</h2><ol><li>Install MobileTrans on PC or Mac</li><li>Connect iPhone and Android via USB</li><li>Select Phone Transfer &#8212; iPhone on left, Android on right</li><li>Select data types to transfer</li><li>For WhatsApp, use WhatsApp Transfer module separately</li><li>Click Transfer</li></ol>"},
    {"slug":"transfer-whatsapp-android-to-iphone","title":"How to Transfer WhatsApp from Android to iPhone","excerpt":"The official tools can't do it. Here's the only reliable way to move your complete WhatsApp history from Android to iPhone.","cat":"WhatsApp","read":"7 min","date":"2025-03-05",
     "body":"<h2>Why Official WhatsApp Transfer Fails</h2><p>Android WhatsApp backups are stored on Google Drive. iOS WhatsApp backups are stored on iCloud. These two systems are incompatible &#8212; an Android Google Drive backup cannot be restored to an iPhone, and an iOS iCloud backup cannot be restored to Android. WhatsApp's own built-in transfer only works within the same platform.</p><h2>What MobileTrans Transfers</h2><p>Complete chat history from all personal and group conversations, photos and videos shared in chats, audio messages and voice notes, documents and files shared in WhatsApp, stickers and GIFs, and contact information for all chat participants.</p><h2>Step-by-Step</h2><ol><li>Open MobileTrans and select WhatsApp Transfer</li><li>Connect both Android (source) and iPhone (destination) via USB</li><li>Select 'Transfer WhatsApp messages'</li><li>MobileTrans reads the Android WhatsApp backup</li><li>Data is written to the iPhone WhatsApp app</li><li>Open WhatsApp on iPhone to verify the transfer</li></ol><h2>What Won't Transfer</h2><p>Starred messages may not be preserved as starred on the new device. Some very old messages from before certain WhatsApp versions may be excluded. App-specific settings and notification preferences are not transferred.</p>"},
    {"slug":"transfer-whatsapp-iphone-to-android","title":"How to Transfer WhatsApp from iPhone to Android","excerpt":"Switching to Android and don't want to lose your WhatsApp? Here's how MobileTrans moves your complete chat history across platforms.","cat":"WhatsApp","read":"6 min","date":"2025-04-12",
     "body":"<h2>The iPhone-to-Android WhatsApp Problem</h2><p>This is considered the hardest phone transfer task. Apple's iOS stores WhatsApp backups in iCloud in a format that Android cannot read. The only way to get WhatsApp chat history from iPhone to Android is to extract it directly from the iPhone's file system &#8212; which is exactly what MobileTrans does.</p><h2>MobileTrans Approach</h2><p>MobileTrans connects to the iPhone via USB and accesses the WhatsApp database directly, bypassing iCloud entirely. The extracted data is then formatted for Android and written to the new phone's WhatsApp installation. No cloud intermediary, no compatibility issues, no data loss.</p><h2>Before You Start</h2><ul><li>Install WhatsApp on the Android device and verify it with your phone number</li><li>Log out of WhatsApp on the iPhone (do not delete)</li><li>Connect both phones to the computer via USB</li><li>Back up the iPhone to iCloud or iTunes as a precaution</li></ul><h2>After Transfer</h2><p>Open WhatsApp on the Android device. Your complete chat history should appear exactly as it was on the iPhone. Photos and videos will be in the WhatsApp media folder on Android.</p>"},
    {"slug":"transfer-data-to-new-iphone","title":"How to Transfer All Data to Your New iPhone","excerpt":"Got a new iPhone? Here's the fastest way to move everything from your old iPhone — or from Android — to your new device.","cat":"iPhone","read":"7 min","date":"2025-05-20",
     "body":"<h2>Three Ways to Set Up a New iPhone</h2><p><strong>iCloud backup</strong> &#8212; works well but requires sufficient iCloud storage (free tier is only 5GB), is slow over WiFi for large libraries, and doesn't transfer WhatsApp from Android. <strong>iTunes/Finder</strong> &#8212; backs up and restores iPhones only, no selective transfer, doesn't transfer WhatsApp. <strong>MobileTrans</strong> &#8212; direct USB transfer at 30 MB/s, works from Android or iPhone, transfers WhatsApp, selective data type support. For new iPhone setup, MobileTrans is typically the fastest option regardless of source device.</p><h2>From Old iPhone to New iPhone</h2><p>Select Phone Transfer with the old iPhone as source and new iPhone as destination. All 18+ data types are available. Transfer completes in 8-15 minutes for a typical phone. The new iPhone looks exactly like the old one when complete.</p><h2>From Android to New iPhone</h2><p>Same process, different source. HEIC conversion is not needed (you're going from Android to iPhone). WhatsApp transfer should be done separately using the WhatsApp Transfer module to ensure complete chat history including media.</p>"},
    {"slug":"samsung-to-iphone-transfer-guide","title":"Samsung to iPhone Transfer — Move Everything Easily","excerpt":"Switching from Samsung Galaxy to iPhone? Complete guide to transferring all your data without losing anything.","cat":"Android to iPhone","read":"6 min","date":"2025-06-15",
     "body":"<h2>Samsung to iPhone &#8212; What Makes It Tricky</h2><p>Samsung uses its own Galaxy-specific features and file formats alongside standard Android. Samsung Notes, Samsung Calendar and Samsung Pay data require specific handling. Standard Android-to-iPhone tools often miss Samsung-specific data.</p><h2>What MobileTrans Transfers from Samsung</h2><ul><li>Contacts (including Samsung-specific contact fields)</li><li>Full gallery &#8212; photos and videos at original quality</li><li>Music and audio files</li><li>SMS messages and call logs</li><li>Calendar events and reminders</li><li>Documents and downloads folder</li><li>WhatsApp (via dedicated WhatsApp Transfer module)</li></ul><h2>Samsung SmartSwitch vs MobileTrans</h2><p>Samsung's own SmartSwitch app can transfer data between Samsung devices or from Samsung to iPhone &#8212; but it doesn't transfer WhatsApp to iPhone and frequently fails for large libraries. MobileTrans transfers everything including WhatsApp and handles large libraries reliably via USB.</p><h2>Tips for Samsung Users</h2><p>Sign out of Samsung accounts on the old phone after transfer. Samsung Pay data cannot be transferred &#8212; set it up fresh on the iPhone. Samsung Notes should be exported as PDFs before transfer if you want to preserve formatting.</p>"},
    {"slug":"move-to-ios-not-working","title":"Move to iOS Not Working? Here's the Fix","excerpt":"Move to iOS keeps failing, timing out or missing files? MobileTrans is the reliable alternative that actually works.","cat":"Android to iPhone","read":"6 min","date":"2025-07-10",
     "body":"<h2>Why Move to iOS Fails So Often</h2><p>Move to iOS is a free app from Apple that transfers data from Android to iPhone over a WiFi connection. In theory this should work well. In practice, it fails frequently for several reasons: large photo libraries exceed time limits, WiFi signal drops during transfer, both phones must stay powered on and connected to the same network for hours, and some data types are simply not supported including WhatsApp.</p><h2>Common Move to iOS Failure Messages</h2><ul><li>'Preparing transfer' stuck at 0%</li><li>Transfer stops partway through</li><li>Some photos missing on iPhone after transfer</li><li>Transfer completes but WhatsApp not included</li><li>Transfer appears complete but contacts are missing</li></ul><h2>Using MobileTrans After Move to iOS Fails</h2><p>The good news: MobileTrans can transfer selectively. If Move to iOS transferred your contacts but missed photos, you can use MobileTrans to transfer only the photos &#8212; without overwriting the contacts that did transfer. Connect both phones, select only the missing data types, and run the targeted transfer.</p><h2>Why MobileTrans Succeeds Where Move to iOS Fails</h2><p>MobileTrans uses a direct USB cable connection. There's no WiFi signal to drop, no network timeout, no 30-minute limit. The USB connection maintains a stable 30 MB/s throughout the entire transfer regardless of how large the data set is.</p>"},
    {"slug":"backup-iphone-to-pc-without-itunes","title":"How to Backup iPhone to PC Without iTunes","excerpt":"iTunes is frustrating and slow. Here's how to backup your iPhone to your PC quickly and selectively without iTunes.","cat":"Backup","read":"6 min","date":"2025-08-05",
     "body":"<h2>Why People Avoid iTunes for iPhone Backup</h2><p>iTunes (now 'Finder' on macOS) creates massive backup files with everything included. It's slow over USB, the backup format is not browsable and you can't extract individual files from a backup. If you just want to backup your photos before getting a new phone, iTunes backup is overkill.</p><h2>MobileTrans Phone Backup</h2><p>MobileTrans creates targeted backups of specific data types. Want to backup only photos and contacts? Select those data types and MobileTrans creates a compact, organised backup in minutes. The backup is stored on your computer in a format that MobileTrans can browse and restore from.</p><h2>What Can Be Backed Up</h2><ul><li>Photos and videos (organised by album)</li><li>Contacts with all fields</li><li>SMS messages and call logs</li><li>Calendar events</li><li>Documents and notes</li><li>WhatsApp data</li></ul><h2>Restoring from Backup</h2><p>Open MobileTrans, select Backup &amp; Restore, choose the backup you want to restore from, select the data types, and connect the destination phone. Restoration works cross-platform &#8212; you can restore an iPhone backup to an Android device.</p>"},
    {"slug":"transfer-whatsapp-to-new-phone","title":"How to Transfer WhatsApp to a New Phone (Any Brand)","excerpt":"Switching phones and terrified of losing your WhatsApp? Here's the complete guide for every scenario.","cat":"WhatsApp","read":"7 min","date":"2025-09-15",
     "body":"<h2>The Four WhatsApp Transfer Scenarios</h2><p><strong>iPhone to iPhone:</strong> Use iCloud WhatsApp backup &#8212; restore during new iPhone setup. This works reliably. MobileTrans is an alternative if iCloud storage is full. <strong>Android to Android:</strong> Use Google Drive WhatsApp backup &#8212; restore during Android setup. This also works reliably. <strong>Android to iPhone:</strong> Official tools cannot do this. MobileTrans is the solution. <strong>iPhone to Android:</strong> Official tools cannot do this. MobileTrans is the solution.</p><h2>Using MobileTrans for Cross-Platform WhatsApp</h2><p>Connect both phones, open the WhatsApp Transfer module, select source and destination, and click Transfer. MobileTrans extracts the WhatsApp data directly from the source phone &#8212; bypassing the cloud backup systems that cause cross-platform incompatibility.</p><h2>WhatsApp Business</h2><p>WhatsApp Business accounts are fully supported. Transfer complete business chat history, contacts, product catalogues and media attachments between any devices using the same MobileTrans process.</p>"},
    {"slug":"icloud-to-android-transfer","title":"How to Transfer iCloud Data to Android","excerpt":"Moving from iPhone to Android and want to bring your iCloud photos, contacts and data? Here's how.","cat":"iPhone to Android","read":"6 min","date":"2025-10-20",
     "body":"<h2>The iCloud to Android Challenge</h2><p>iCloud is Apple's ecosystem service and has no direct connection to Android. Your iCloud photos, contacts and documents exist in an Apple-controlled cloud that Google services cannot read. Getting this data to Android normally requires going through an iPhone &#8212; unless you use MobileTrans.</p><h2>MobileTrans iCloud to Android</h2><p>MobileTrans connects to your iCloud account, retrieves your data, and transfers it directly to your Android device. No iPhone needed as an intermediary. Authenticate with your Apple ID and choose which data to download and transfer to the Android phone.</p><h2>What Can Be Transferred from iCloud</h2><ul><li>Photos and videos from iCloud Photo Library</li><li>Contacts from iCloud Contacts</li><li>Calendar events and reminders</li><li>Notes</li><li>Documents stored in iCloud Drive</li></ul><h2>Privacy and Security</h2><p>MobileTrans handles your Apple ID authentication locally on your computer. Your credentials are used only to access iCloud and are not stored or transmitted to Wondershare servers.</p>"},
    {"slug":"best-phone-transfer-app-2025","title":"Best Phone Transfer App in 2025 — Ranked &amp; Reviewed","excerpt":"We tested every major phone transfer tool. Here's the honest ranking for transferring data between Android and iPhone.","cat":"Reviews","read":"9 min","date":"2025-11-10",
     "body":"<h2>How We Evaluated</h2><p>We performed transfers between Android and iPhone, iPhone to Android, and same-platform transfers, measuring: completeness of data transferred, WhatsApp transfer success, ease of use, transfer speed and pricing.</p><h2>1. Wondershare MobileTrans &#8212; Best Overall</h2><p>MobileTrans earns the top position with the most complete cross-platform WhatsApp transfer, support for Viber, LINE, WeChat and Kik, iCloud to Android transfer, and reliable USB-based performance at 30 MB/s. <strong>Verdict: best choice for most users switching phones.</strong></p><h2>2. Dr.Fone Phone Transfer &#8212; Strong Competitor</h2><p>Dr.Fone performs comparably for standard phone-to-phone transfers. WhatsApp cross-platform support is more limited than MobileTrans, particularly for iPhone-to-Android. <strong>Verdict: good alternative, especially for same-platform transfers.</strong></p><h2>3. Move to iOS (Free) &#8212; Best Free Android to iPhone</h2><p>Apple's free app works well when it works. Fails frequently on large libraries, over weak WiFi or when transferring WhatsApp. <strong>Verdict: try it first, use MobileTrans when it fails.</strong></p><h2>Overall Recommendation</h2><p>For anyone switching from Android to iPhone or iPhone to Android who needs WhatsApp transferred &#8212; MobileTrans is the clear choice.</p>"},
    {"slug":"transfer-data-broken-iphone","title":"How to Transfer Data from a Broken iPhone","excerpt":"Cracked screen, won't turn on, or damaged phone? Here's how to rescue your data from a broken iPhone.","cat":"iPhone","read":"7 min","date":"2025-12-01",
     "body":"<h2>Assessing Your Broken iPhone</h2><p>The first step is to determine what still works. Different types of damage require different approaches. <strong>Cracked screen but phone powers on:</strong> You can still transfer data via USB &#8212; MobileTrans can access the phone even if you can't interact with the touchscreen. <strong>Cracked screen and unresponsive:</strong> Use an external monitor or the phone's voice features if possible to unlock it. <strong>Won't turn on:</strong> This is the hardest case. Try charging for 30 minutes first. If it still won't turn on, professional data recovery services may be necessary.</p><h2>Transferring via USB from Broken iPhone</h2><ol><li>Connect the broken iPhone to your computer via USB</li><li>If prompted to 'Trust This Computer' on the phone, accept it (you may need to use voice control or an assistive touch to do this)</li><li>Open MobileTrans and select the iPhone as the source</li><li>Select a destination device &#8212; a new iPhone or Android</li><li>Select the data to transfer</li><li>Click Transfer</li></ol><h2>Recovering WhatsApp from Broken iPhone</h2><p>If the broken iPhone was previously backed up to iCloud with WhatsApp enabled, you can restore the WhatsApp data from iCloud to a new device using MobileTrans &#8212; even without physical access to the broken phone.</p>"},
]

def page_blog():
    bc = BC_SCHEMA([("Home",""),("Blog","")])
    cards = "".join(
        '<div class="card"><div class="badge">' + p["cat"] + '</div>'
        '<h3 style="margin-top:.55rem;margin-bottom:.45rem;font-size:.97rem">'
        '<a href="' + BASE_PATH + '/blog/' + p["slug"] + '.html" style="color:var(--ink)">' + p["title"] + '</a></h3>'
        '<p style="font-size:.84rem;margin-bottom:.85rem">' + p["excerpt"] + '</p>'
        '<div style="display:flex;justify-content:space-between;align-items:center">'
        '<span style="font-size:.73rem;color:var(--muted)">' + p["date"] + ' &#183; ' + p["read"] + '</span>'
        '<a href="' + BASE_PATH + '/blog/' + p["slug"] + '.html" style="font-size:.8rem;font-weight:600;color:var(--ha)">Read &#8594;</a>'
        '</div></div>'
        for p in BLOG_POSTS)
    return (HEAD("MobileTrans Blog &#8212; Phone Transfer Guides &amp; Tutorials | " + str(YEAR),
                 "Phone transfer guides for iPhone, Android, WhatsApp and more. Step-by-step tutorials for Wondershare MobileTrans.",
                 "blog.html", bc)
        + "\n<body>\n" + NAV()
        + "\n" + BC([("Home",BASE_PATH+"/"),("Blog","")])
        + '\n<section class="hero"><div class="eyebrow">&#10022; Phone Transfer Guides</div>'
        + '\n  <h1>Transfer Guides &amp;<br><em>Tutorials</em></h1>'
        + '\n  <p class="hsub">' + str(len(BLOG_POSTS)) + ' in-depth articles for every phone switching scenario.</p>'
        + '\n</section>\n'
        + '\n<section><div class="container"><div class="sec-ey">All ' + str(len(BLOG_POSTS)) + ' Articles</div><h2>Phone Transfer Guides</h2>'
        + '\n  <div class="grid3">' + cards + '</div>'
        + '\n</div></section>\n'
        + CTA("Need to Switch Phones Right Now?","Download MobileTrans &#8212; transfer up to 20 photos free, no credit card.")
        + "\n" + FOOTER() + "\n</body></html>")

def page_blog_post(post):
    bc  = BC_SCHEMA([("Home",""),("Blog","blog.html"),(post["title"][:40]+"...","")])
    art = ART_SCHEMA(post["title"], post["excerpt"], post["date"])
    others = [p for p in BLOG_POSTS if p["slug"] != post["slug"]][:3]
    rel = "".join('<div class="card"><div class="badge">' + p["cat"] + '</div><h3 style="margin-top:.5rem;font-size:.93rem"><a href="' + BASE_PATH + '/blog/' + p["slug"] + '.html" style="color:var(--ink)">' + p["title"] + '</a></h3><p style="font-size:.82rem">' + p["excerpt"] + '</p></div>' for p in others)
    h = HEAD(post["title"] + " | MobileTrans Guide", post["excerpt"], "blog/" + post["slug"] + ".html", bc+art, "article")
    return (h + "\n<body>\n" + NAV()
        + "\n" + BC([("Home",BASE_PATH+"/"),("Blog",BASE_PATH+"/blog.html"),(post["cat"],"")])
        + '\n<section class="hero" style="padding:3.5rem clamp(1rem,5vw,3rem) 3rem">'
        + '\n  <div class="eyebrow">&#10022; ' + post["cat"] + ' &#183; ' + post["read"] + '</div>'
        + '\n  <h1 style="font-size:clamp(1.7rem,4vw,2.8rem)">' + post["title"] + '</h1>'
        + '\n  <p class="hsub" style="font-size:1rem">' + post["excerpt"] + '</p>'
        + '\n  <p style="color:rgba(255,255,255,.38);font-size:.76rem">Published ' + post["date"] + '</p>'
        + '\n</section>\n'
        + '\n<section style="background:#fff"><div class="container"><div style="max-width:780px">'
        + '\n  <div class="prose">' + post["body"] + '</div>'
        + '\n  <div class="notice" style="margin-top:2.5rem"><strong>Ready to transfer?</strong> MobileTrans transfers up to 20 photos free. '
        + '\n    <a href="' + AFFILIATE_URL + '" target="_blank" rel="nofollow sponsored" style="color:var(--ha);font-weight:600">Download free trial &#8594;</a>'
        + '\n  </div></div></div></section>\n'
        + '\n<section><div class="container"><div class="sec-ey">More Guides</div><h2>Related Articles</h2>'
        + '\n  <div class="grid3">' + rel + '</div>'
        + '\n</div></section>\n'
        + CTA() + "\n" + FOOTER() + "\n</body></html>")

def page_glossary():
    terms = [
        ("Phone Transfer","The process of moving data from one mobile device to another, including contacts, photos, messages, music and app data."),
        ("Cross-Platform Transfer","Transferring data between different mobile operating systems, such as from Android to iPhone or iPhone to Android."),
        ("WhatsApp Transfer","Moving WhatsApp chat history, media attachments, stickers and voice notes from one device to another."),
        ("USB Transfer","Data transfer using a physical USB cable connection between a phone and a computer. Faster and more reliable than WiFi-based transfer methods."),
        ("iCloud","Apple's cloud storage service. Stores iPhone backups, photos, contacts and documents. Backups can only be restored to other Apple devices natively."),
        ("Google Drive","Google's cloud storage service used by Android phones for WhatsApp backups and other data. Backups cannot be restored to iPhones natively."),
        ("Move to iOS","Apple's free app for transferring data from Android to iPhone over WiFi. Works for basic data but frequently fails on large libraries and doesn't support WhatsApp."),
        ("iTunes Backup","A complete backup of an iPhone stored on a computer via iTunes (Windows) or Finder (Mac). Backs up and restores iPhones only, no selective restore."),
        ("HEIC","High Efficiency Image Container. Apple's photo format used by iPhone cameras. More efficient than JPEG but not universally compatible with Android. MobileTrans automatically converts HEIC to JPG during iPhone-to-Android transfers."),
        ("Data Types","The categories of information that can be transferred between phones: contacts, photos, videos, music, SMS, call logs, calendar, documents, WhatsApp, Viber, LINE, WeChat and more."),
        ("Selective Transfer","Transferring only specific data types rather than everything. MobileTrans allows you to choose exactly which categories to move, leaving others untouched."),
        ("WhatsApp Backup","A saved copy of WhatsApp chat history and media. Android stores backups on Google Drive. iOS stores backups on iCloud. The two formats are incompatible natively."),
        ("Transfer Speed","The rate at which data moves between devices. USB connection at 30 MB/s is up to 200x faster than Bluetooth (typical 0.1-0.3 MB/s) and significantly faster than WiFi transfer methods."),
        ("iCloud Restore","Restoring data from an iCloud backup to a device. Normally only works for iPhones. MobileTrans can restore iCloud data directly to Android devices."),
        ("WhatsApp Business","WhatsApp's version for business users with additional features. Fully supported by MobileTrans for cross-platform transfer including chat history and business-specific data."),
        ("Contacts Transfer","Moving phone contacts including names, numbers, emails, photos and notes from one device to another. One of the most commonly needed transfer tasks when switching phones."),
        ("SMS Transfer","Moving text message history from one phone to another. Cross-platform SMS transfer (Android to iPhone) requires dedicated software as the message formats differ."),
        ("Phone Backup","A complete or selective copy of phone data stored on a computer or cloud service for safekeeping, allowing restoration to the same or different device."),
        ("Device Compatibility","The range of phone models and operating system versions a transfer tool supports. MobileTrans supports 6,000+ devices including all major Android and iPhone models."),
        ("HarmonyOS","Huawei's operating system used on newer Huawei and Honor phones. Supported by MobileTrans for data transfer to and from Android and iPhone devices."),
        ("Viber","A messaging app with separate chat backup from WhatsApp. Supported by MobileTrans for chat history transfer between devices."),
        ("LINE","A messaging app popular in Japan, Taiwan and Thailand. Supported by MobileTrans for chat history and media transfer between devices."),
        ("WeChat","China's most popular messaging and social platform. Supported by MobileTrans for chat data transfer between Android and iPhone devices."),
        ("App Data Transfer","Moving the data stored within specific apps (chat history, settings, in-app progress) from one phone to another. More complex than simple file transfer."),
        ("Direct Transfer","Phone-to-phone data transfer without going through a cloud service. Faster, more private and works without internet access."),
    ]
    cards = "".join('<div class="card"><h3>' + t + '</h3><p>' + d + '</p></div>' for t,d in terms)
    bc = BC_SCHEMA([("Home",""),("Glossary","")])
    return (HEAD("Phone Transfer Glossary &#8212; " + str(len(terms)) + " Terms Explained | " + str(YEAR),
                 "Complete phone transfer glossary &#8212; WhatsApp transfer, iCloud, HEIC, USB transfer speed, cross-platform and more.",
                 "glossary.html", bc)
        + "\n<body>\n" + NAV()
        + "\n" + BC([("Home",BASE_PATH+"/"),("Glossary","")])
        + '\n<section class="hero"><div class="eyebrow">&#10022; Phone Transfer Reference</div>'
        + '\n  <h1>Phone Transfer<br><em>Glossary</em></h1>'
        + '\n  <p class="hsub">' + str(len(terms)) + ' plain-language definitions for every phone transfer term.</p>'
        + '\n</section>\n'
        + '\n<section><div class="container"><div class="sec-ey">' + str(len(terms)) + ' Terms</div><h2>Complete Glossary</h2>'
        + '\n  <div class="grid3">' + cards + '</div>'
        + '\n</div></section>\n'
        + CTA("Ready to Switch Phones?","Download MobileTrans free &#8212; transfer up to 20 photos, no credit card.")
        + "\n" + FOOTER() + "\n</body></html>")

def page_download():
    bc = BC_SCHEMA([("Home",""),("Download","")])
    return (HEAD("Download MobileTrans Free &#8212; Phone Transfer for Windows &amp; Mac | " + str(YEAR),
                 "Download Wondershare MobileTrans free. Transfer phone data, WhatsApp, contacts and photos. Free trial.",
                 "download.html", bc)
        + "\n<body>\n" + NAV()
        + "\n" + BC([("Home",BASE_PATH+"/"),("Download","")])
        + '\n<section class="hero"><div class="eyebrow">&#10022; Free Trial Available</div>'
        + '\n  <h1>Download MobileTrans<br><em>Free Today</em></h1>'
        + '\n  <p class="hsub">Transfer up to 20 photos free. WhatsApp messages between Android and iOS also included in the free tier. No credit card needed.</p>'
        + '\n  <a href="' + AFFILIATE_URL + '" class="btn-p" target="_blank" rel="nofollow sponsored" style="font-size:1.1rem;padding:1rem 2.5rem">&#8659; Download Free Trial</a>'
        + '\n  <p style="color:rgba(255,255,255,.38);font-size:.78rem;margin-top:1rem">Windows 7/8/10/11 &#183; macOS 10.12+ &#183; Intel &amp; Apple Silicon</p>'
        + '\n</section>\n'
        + '\n<section><div class="container"><div class="sec-ey">Everything Included</div><h2>Free Trial Includes All Features</h2>'
        + FEATURES_GRID()
        + '\n</div></section>\n'
        + '\n<section style="background:#fff"><div class="container"><div class="sec-ey">Requirements</div><h2>Compatible With Your Setup</h2>'
        + '\n  <div class="grid2">'
        + '\n    <div class="card"><h3>&#128421; Windows</h3><ul><li>Windows 7 / 8 / 10 / 11</li><li>32-bit and 64-bit</li><li>1 GB RAM minimum</li><li>200 MB free disk space</li></ul></div>'
        + '\n    <div class="card"><h3>&#63743; macOS</h3><ul><li>macOS 10.12 Sierra and above</li><li>Includes Sonoma &amp; Sequoia</li><li>Intel and Apple Silicon M1/M2/M3</li><li>1 GB RAM minimum</li></ul></div>'
        + '\n  </div>\n</div></section>\n'
        + CTA("Download MobileTrans Now","Free trial &#183; No credit card &#183; Windows &amp; Mac &#183; WhatsApp included.")
        + "\n" + FOOTER() + "\n</body></html>")

def page_keywords():
    cats = defaultdict(list)
    for k in KEYWORDS: cats[k["cat"]].append(k)
    sections = ""
    for cat in sorted(cats.keys()):
        items = cats[cat]; desc = CAT_DESC.get(cat,""); a1,_ = ac(cat)
        links = "".join('<a class="kw" href="' + BASE_PATH + '/' + k["slug"] + '.html">' + k["keyword"] + '</a>' for k in items)
        sections += ('<div style="margin-bottom:3rem"><h3 style="font-size:1rem;font-weight:700;color:' + a1 + ';margin-bottom:.35rem;border-bottom:2px solid ' + a1 + ';padding-bottom:.35rem;display:inline-block">' + cat.replace("-"," ").title() + ' <span style="color:var(--muted);font-weight:400;font-size:.83rem">(' + str(len(items)) + ')</span></h3>' + ('<p style="font-size:.82rem;color:var(--muted);margin:.45rem 0 .7rem;max-width:600px">' + desc + '</p>' if desc else '') + '<div class="kw-cloud">' + links + '</div></div>')
    bc = BC_SCHEMA([("Home",""),("All Topics","")])
    return (HEAD("MobileTrans &#8212; All " + str(len(KEYWORDS)) + " Phone Transfer Topics | " + str(YEAR),
                 "Browse all phone transfer topics &#8212; iPhone, Android, WhatsApp, backup and more.",
                 "keywords.html", bc)
        + "\n<body>\n" + NAV()
        + "\n" + BC([("Home",BASE_PATH+"/"),("All Topics","")])
        + '\n<section class="hero"><div class="eyebrow">&#10022; Topic Directory</div>'
        + '\n  <h1>All Phone Transfer<br><em>Topics</em></h1>'
        + '\n  <p class="hsub">' + str(len(KEYWORDS)) + ' targeted topics covering every phone switching scenario.</p>'
        + '\n</section>\n'
        + '\n<section><div class="container"><div class="sec-ey">Browse All ' + str(len(KEYWORDS)) + ' Topics</div>' + sections + '</div></section>\n'
        + CTA() + "\n" + FOOTER() + "\n</body></html>")

def page_privacy():
    bc = BC_SCHEMA([("Home",""),("Privacy","")])
    return (HEAD("Privacy Policy &#8212; MobileTrans Guide","Privacy policy for the MobileTrans affiliate guide website.","privacy.html",bc)
        + "\n<body>\n" + NAV()
        + "\n" + BC([("Home",BASE_PATH+"/"),("Privacy Policy","")])
        + '\n<section class="hero" style="padding:3.5rem 2rem 3rem"><div class="eyebrow">Legal</div><h1>Privacy <em>Policy</em></h1></section>\n'
        + '\n<section style="background:#fff"><div class="container"><div class="prose" style="max-width:800px">'
        + '\n  <p><strong>Last updated: ' + BUILD_DATE + '</strong></p>'
        + '\n  <h3>1. About</h3><p>Affiliate promotional site for Wondershare MobileTrans phone transfer software. We do not collect personal data beyond standard server logs.</p>'
        + '\n  <h3>2. Affiliate Disclosure</h3><p>This site contains affiliate links. When you purchase MobileTrans via our links, we may receive a commission at no extra cost to you.</p>'
        + '\n  <h3>3. Cookies</h3><p>This website does not use tracking cookies.</p>'
        + '\n  <h3>4. External Links</h3><p>All purchase links go to the official Wondershare website. We are not responsible for external site privacy practices.</p>'
        + '\n</div></div></section>\n' + FOOTER() + "\n</body></html>")

def page_404():
    return ("<!DOCTYPE html>\n<html lang=\"en\"><head>\n<meta charset=\"UTF-8\"/><meta name=\"viewport\" content=\"width=device-width,initial-scale=1.0\"/>\n"
            "<title>Page Not Found &#8212; MobileTrans</title>\n"
            "<meta http-equiv=\"refresh\" content=\"4;url=" + SITE_DOMAIN + "/\"/>\n"
            "<style>body{font-family:system-ui,sans-serif;background:#0c4a6e;color:#fff;display:flex;align-items:center;justify-content:center;min-height:100vh;text-align:center;margin:0;padding:2rem}"
            "h1{font-size:3rem;margin-bottom:.75rem;font-weight:800}p{color:rgba(255,255,255,.6);margin-bottom:2rem;line-height:1.6}"
            "a{background:#0ea5e9;color:#fff;padding:.85rem 2.2rem;border-radius:8px;text-decoration:none;font-weight:700}</style>"
            "</head><body><div><div style=\"font-size:4rem;margin-bottom:1rem\">&#128241;</div><h1>Page Not Found</h1>"
            "<p>Redirecting to the homepage in 4 seconds...</p><a href=\"" + SITE_DOMAIN + "/\">Go to MobileTrans Home</a></div></body></html>")

def build_sitemap():
    essential = [("",1.0,"weekly"),("features.html",.9,"monthly"),("how-it-works.html",.9,"monthly"),
                 ("faq.html",.85,"monthly"),("compare.html",.85,"monthly"),("blog.html",.85,"weekly"),
                 ("download.html",.9,"monthly"),("keywords.html",.8,"monthly"),
                 ("glossary.html",.75,"monthly"),("privacy.html",.3,"yearly")]
    urls = ""
    for path,pri,freq in essential:
        loc = SITE_DOMAIN + ("/" + path if path else "/")
        urls += "  <url><loc>" + loc + "</loc><lastmod>" + BUILD_DATE + "</lastmod><changefreq>" + freq + "</changefreq><priority>" + str(pri) + "</priority></url>\n"
    for p in BLOG_POSTS:
        urls += "  <url><loc>" + SITE_DOMAIN + "/blog/" + p["slug"] + ".html</loc><lastmod>" + p["date"] + "</lastmod><changefreq>monthly</changefreq><priority>0.75</priority></url>\n"
    for k in KEYWORDS:
        urls += "  <url><loc>" + SITE_DOMAIN + "/" + k["slug"] + ".html</loc><lastmod>" + BUILD_DATE + "</lastmod><changefreq>monthly</changefreq><priority>0.65</priority></url>\n"
    return '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + '</urlset>'

def build_robots():
    return "User-agent: *\nAllow: /\nDisallow: /build-report.json\nSitemap: " + SITE_DOMAIN + "/sitemap.xml\n"

def build_llms():
    cats   = sorted(set(k["cat"] for k in KEYWORDS))
    sample = ", ".join(k["keyword"] for k in KEYWORDS[:30])
    return ("# Wondershare MobileTrans\n\n"
            "> #1 phone transfer app by Wondershare. Transfers 18+ data types between 6,000+ devices at 30 MB/s. "
            "Full cross-platform WhatsApp transfer between Android and iPhone. 1.5 million+ users.\n\n"
            "## What MobileTrans Transfers\n"
            "- Contacts, photos, videos, music, SMS, call logs, calendar, documents, apps\n"
            "- WhatsApp (Android ↔ iPhone) including chat history, media, stickers, voice notes\n"
            "- Viber, LINE, WeChat and Kik chat data\n"
            "- iCloud data to Android devices\n"
            "- Full phone backup to computer and restore to any device\n\n"
            "## Key Stats\n- 1.5 million+ users\n- 6,000+ supported devices\n- 18+ data types\n"
            "- 30 MB/s transfer speed (200x faster than Bluetooth)\n- Supports Android, iOS, HarmonyOS\n\n"
            "## Platforms\nWindows 7/8/10/11 · macOS 10.12+ · Intel & Apple Silicon · iOS & Android apps\n\n"
            "## Pricing\nFree trial (up to 20 photos, WhatsApp messages). Full license for unlimited transfers.\n\n"
            "## Download\n" + AFFILIATE_URL + "\n\n"
            "## Developer\nWondershare Technology Co., Ltd.\n\n"
            "## Site\n" + SITE_DOMAIN + "\n"
            + str(len(KEYWORDS)) + " keyword pages · " + str(len(BLOG_POSTS)) + " blog posts\n"
            "Sitemap: " + SITE_DOMAIN + "/sitemap.xml\n\n"
            "## Categories\n" + ", ".join(c.title() for c in cats) + "\n\n"
            "## Sample Keywords\n" + sample + "\n")

WORKFLOW = """name: Build & Deploy MobileTrans

on:
  workflow_dispatch:

permissions:
  contents: write
  pages: write
  id-token: write

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Remove all old files from repo
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          find . -maxdepth 1 -type f ! -name 'build.py' ! -name 'README.md' -delete
          find . -maxdepth 1 -type d ! -name '.' ! -name '.git' ! -name '.github' -exec rm -rf {} + 2>/dev/null || true
          git add -A
          git diff --staged --quiet || git commit -m "Clean up old files"
          git push origin main

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Run build script
        run: python3 build.py

      - name: Setup Pages
        uses: actions/configure-pages@v5

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: ./dist

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
"""

def progress(i, total, label=""):
    pct = i/total; bar = "█"*int(30*pct)+"░"*(30-int(30*pct))
    print(f"\r  [{bar}] {i:>4}/{total} {label:<42}", end="", flush=True)

def main():
    os.makedirs(DIST, exist_ok=True)
    os.makedirs(DIST+"/blog", exist_ok=True)
    os.makedirs(DIST+"/.github/workflows", exist_ok=True)

    print(f"\n{'═'*60}")
    print(f"  MobileTrans Site Builder — {BUILD_DATE}")
    print(f"{'═'*60}")
    print(f"  Domain:   {SITE_DOMAIN}")
    print(f"  Keywords: {len(KEYWORDS)}")
    print(f"  Blog:     {len(BLOG_POSTS)} posts")
    print(f"{'═'*60}\n")

    essential = {
        "index.html":        page_index(),
        "features.html":     page_features(),
        "how-it-works.html": page_how_it_works(),
        "faq.html":          page_faq(),
        "compare.html":      page_compare(),
        "blog.html":         page_blog(),
        "download.html":     page_download(),
        "keywords.html":     page_keywords(),
        "glossary.html":     page_glossary(),
        "privacy.html":      page_privacy(),
        "404.html":          page_404(),
    }
    print("  Essential pages:")
    for fname, html in essential.items():
        with open(DIST+"/"+fname,"w",encoding="utf-8") as f: f.write(html)
        print(f"    ✓ {fname}  ({len(html)//1024}KB)")

    print(f"\n  Blog posts ({len(BLOG_POSTS)}):")
    for post in BLOG_POSTS:
        with open(DIST+"/blog/"+post["slug"]+".html","w",encoding="utf-8") as f:
            f.write(page_blog_post(post))
        print("    ✓ blog/"+post["slug"]+".html")

    print(f"\n  Keyword pages ({len(KEYWORDS)}):")
    for i,kw_data in enumerate(KEYWORDS):
        with open(DIST+"/"+kw_data["slug"]+".html","w",encoding="utf-8") as f:
            f.write(build_keyword_page(kw_data))
        progress(i+1,len(KEYWORDS),kw_data["slug"])
    print()

    support = {"sitemap.xml":build_sitemap(),"robots.txt":build_robots(),
               "llms.txt":build_llms(),"_config.yml":"# GitHub Pages\nexclude: [build.py]\n"}
    with open(DIST+"/.nojekyll","w") as f: f.write("")
    with open(DIST+"/.github/workflows/deploy.yml","w") as f: f.write(WORKFLOW)
    print("\n  Support files:")
    for fname,content in support.items():
        with open(DIST+"/"+fname,"w",encoding="utf-8") as f: f.write(content)
        print(f"    ✓ {fname}")
    print("    ✓ .nojekyll  ✓ .github/workflows/deploy.yml")

    total_sz    = sum(os.path.getsize(os.path.join(r,fn)) for r,_,files in os.walk(DIST) for fn in files)
    total_files = sum(len(files) for _,_,files in os.walk(DIST))
    report = {"build_date":BUILD_DATE,"domain":SITE_DOMAIN,"keyword_pages":len(KEYWORDS),
              "blog_posts":len(BLOG_POSTS),"total_files":total_files,
              "total_size_mb":round(total_sz/1024/1024,2),"affiliate_url":AFFILIATE_URL}
    with open(DIST+"/build-report.json","w") as f: json.dump(report,f,indent=2)
    print("    ✓ build-report.json")

    print(f"""
{'═'*60}
  ✅  BUILD COMPLETE
{'═'*60}
  Keyword pages:    {len(KEYWORDS):>5}
  Blog posts:       {len(BLOG_POSTS):>5}
  Essential pages:  {len(essential):>5}
  Total files:      {total_files:>5}
  Sitemap URLs:     {len(KEYWORDS)+len(BLOG_POSTS)+10:>5}
  Total size:       {round(total_sz/1024/1024,1):>4.1f} MB
  Output:           ./dist/
{'═'*60}

  Repo: https://github.com/brightlane/iphonerepair
  Live: {SITE_DOMAIN}/
""")

if __name__ == "__main__":
    main()
