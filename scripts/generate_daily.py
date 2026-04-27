import os
import random
import re
from datetime import datetime

def descramble_content(kw):
    """Generates unique-looking HTML by shuffling pre-written technical blocks."""
    
    # Block 1: Intros
    intros = [
        f"In 2026, the landscape of {kw} is being reshaped by high-fidelity neural synthesis.",
        f"Integrating ElevenLabs voice models into your {kw} strategy offers a massive edge.",
        f"The technical requirements for {kw} have shifted toward low-latency AI responses.",
        f"Exploring the future of {kw} starts with understanding automated voice protocols."
    ]
    
    # Block 2: Technical Body (Shuffled for uniqueness)
    body_parts = [
        f"Our research into {kw} shows that user engagement increases with personalized audio.",
        f"Deploying {kw} at scale requires a robust Vulture Protocol infrastructure.",
        f"Security and data integrity remain the top priorities for all {kw} deployments.",
        f"The intersection of {kw} and AI automation is creating new revenue streams."
    ]
    random.shuffle(body_parts)
    
    # Block 3: CTAs
    ctas = [f"Unlock {kw} Potential", f"Hear {kw} in Action", f"Deploy {kw} Now"]

    return f"""
    <p>{random.choice(intros)}</p>
    <ul>
        <li>{body_parts[0]}</li>
        <li>{body_parts[1]}</li>
    </ul>
    <div style="background:#f4f4f4; padding:15px; border-radius:5px; text-align:center;">
        <a href="#"><strong>{random.choice(ctas)}</strong></a>
    </div>
    <p>{body_parts[2]}</p>
    """

def main():
    # Ensure directories exist
    if not os.path.exists('pages'):
        os.makedirs('pages')
    
    # Load keywords
    keywords = ["AI Voice Search", "Neural Audio"]
    if os.path.exists('keywords.txt'):
        with open('keywords.txt', 'r', encoding='utf-8') as f:
            keywords = [line.strip() for line in f if line.strip()]

    # Process first 5,000 for stability
    for kw in keywords[:5000]:
        html_body = descramble_content(kw)
        safe_name = re.sub(r'[^a-zA-Z0-9\s-]', '', kw.lower()).strip().replace(' ', '-')
        
        with open(f"pages/{safe_name}.html", 'w', encoding='utf-8') as f:
            f.write(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{kw} | 2026 ElevenLabs Hub</title>
    <style>body{{font-family:sans-serif; max-width:800px; margin:auto; padding:50px; line-height:1.7;}}</style>
</head>
<body>
    <h1>{kw}</h1>
    {html_body}
    <hr>
    <p><small>System Sync: {datetime.now().strftime('%Y-%m-%d')}</small></p>
</body>
</html>""")
    
    print(f"🏁 Vulture Sync Complete: {len(keywords[:5000])} pages built.")

if __name__ == "__main__":
    main()
