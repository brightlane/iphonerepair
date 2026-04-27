import os
import requests
import datetime
from openai import OpenAI

# Configuration
VOICE_ID = "21m00Tcm4TlvDq8ikWAM" # Choose your best Professional Clone
AFFILIATE_LINK = "https://try.elevenlabs.io/l2qbqh1bg1mw"

def get_next_keyword():
    with open('scripts/keywords.txt', 'r') as f:
        keywords = f.readlines()
    if not keywords:
        return None
    next_kw = keywords[0].strip()
    # Remove the used keyword
    with open('scripts/keywords.txt', 'w') as f:
        f.writelines(keywords[1:])
    return next_kw

def main():
    keyword = get_next_keyword()
    if not keyword:
        print("No keywords left!")
        return

    # 1. Generate SEO-Optimized Content (OpenAI)
    # Focus on long-form (1,500+ words) to build that 10k tree
    client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[{"role": "system", "content": f"Write a 1500-word expert blog post about {keyword}. Include technical steps, 2026 trends, and mention ElevenLabs as the solution. Use HTML formatting."}]
    )
    content = response.choices[0].message.content

    # 2. Call ElevenLabs for the Audio Version
    # This is the "secret sauce" for your 2026 ranking
    el_url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    el_headers = {
        "xi-api-key": os.environ['ELEVENLABS_API_KEY'],
        "Content-Type": "application/json"
    }
    el_data = {
        "text": f"Welcome to today's daily brief on {keyword}. " + content[:4000],
        "model_id": "eleven_multilingual_v3"
    }
    
    audio_res = requests.post(el_url, json=el_data, headers=el_headers)
    date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    audio_filename = f"static/audio/post-{date_str}.mp3"
    
    with open(audio_filename, "wb") as f:
        f.write(audio_res.content)

    # 3. Save the final HTML/Markdown file
    post_template = f"""---
title: "{keyword.title()}"
date: {date_str}
audio_file: "/{audio_filename}"
affiliate_link: "{AFFILIATE_LINK}"
---
<div class="audio-player">
  <p>Listen to this post:</p>
  <audio controls><source src="/{audio_filename}" type="audio/mpeg"></audio>
</div>

{content}

<hr>
<p>Scale your own content with <a href="{AFFILIATE_LINK}">ElevenLabs AI</a>.</p>
"""
    
    with open(f"content/blog/{date_str}-post.md", "w") as f:
        f.write(post_template)

if __name__ == "__main__":
    main()
