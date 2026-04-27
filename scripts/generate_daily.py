import os
import random
import re
from datetime import datetime

def descramble_elevenlabs(kw):
    # Layer 1: Opening Hooks
    intros = [
        f"Exploring the future of {kw} through high-fidelity AI voice.",
        f"Why {kw} is becoming the standard for 2026 digital infrastructure.",
        f"The intersection of ElevenLabs technology and {kw} optimization.",
        f"A deep dive into the {kw} ecosystem using neural synthesis."
    ]
    
    # Layer 2: Core Content Blocks (Shuffled every time)
    blocks = [
        f"Our latest research indicates that {kw} requires low-latency execution.",
        f"The deployment of {kw} assets has been streamlined for global reach.",
        f"By using AI-driven voice cloning, {kw} engagement has tripled this year.",
        f"Security and transparency are the twin pillars of our {kw} framework."
    ]
    random.shuffle(blocks)
    
    # Layer 3: Dynamic CTA
    ctas = ["Listen Now", "View Full Specs", "Get Started", "Learn More"]

    return f"""
    <p>{random.choice(intros)}</p>
    <ul>
        <li>{blocks[0]}</li>
        <li>{blocks[1]}</li>
    </ul>
    <div style='padding:15px; background:#f0f9ff; border:1px solid #bae6fd; text-align:center;'>
        <a href='#'><strong>{random.choice(ctas)}: {kw}</strong></a>
    </div>
    <p>{blocks[2]}</p>
    """

def main():
    if not os.path.exists('pages'): os.makedirs('pages')
    
    # Load your keywords
    keywords = ["AI Voices"]
    if os.path.exists('keywords.txt'):
        with open('keywords.txt', 'r') as f:
            keywords = [line.strip() for line in f if line.strip()]

    for kw in keywords[:1000]: # Safety limit
        content = descramble_elevenlabs(kw)
        safe_name = re.sub(r'[^a-zA-Z0-9\s-]', '', kw.lower()).strip().replace(' ', '-')
        
        with open(f"pages/{safe_name}.html", 'w') as f:
            f.write(f"<html><body><h1>{kw}</h1>{content}</body></html>")
    
    print(f"✅ Descrambled {len(keywords[:1000])} pages for elevenlabs.com")

if __name__ == "__main__":
    main()
