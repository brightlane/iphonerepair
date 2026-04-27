import os
import requests
import datetime
from openai import OpenAI

# 1. Setup Clients
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
EL_KEY = os.getenv("ELEVENLABS_API_KEY")
AFFILIATE_LINK = "https://elevenlabs.io/?from=l2qbqh1bg1mw"

def get_next_keyword():
    if not os.path.exists('scripts/keywords.txt'): return None
    with open('scripts/keywords.txt', 'r') as f:
        keywords = f.readlines()
    if not keywords: return None
    next_kw = keywords[0].strip()
    with open('scripts/keywords.txt', 'w') as f:
        f.writelines(keywords[1:])
    return next_kw

def main():
    keyword = get_next_keyword()
    if not keyword: return

    # 2. Generate 1,500 Word SEO Post
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[{"role": "system", "content": f"Write a 1500-word expert guide about {keyword}. Focus on how ElevenLabs solves this. Use HTML formatting. Mention the affiliate link {AFFILIATE_LINK} twice."}]
    )
    blog_content = response.choices[0].message.content
    date_str = datetime.datetime.now().strftime("%Y-%m-%d")

    # 3. Generate ElevenLabs Audio
    audio_url = "https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM"
    headers = {"xi-api-key": EL_KEY, "Content-Type": "application/json"}
    payload = {"text": f"Today we are discussing {keyword}. " + blog_content[:3000], "model_id": "eleven_multilingual_v3"}
    
    audio_res = requests.post(audio_url, json=payload, headers=headers)
    os.makedirs('static/audio', exist_ok=True)
    with open(f"static/audio/{date_str}.mp3", "wb") as f:
        f.write(audio_res.content)

    # 4. Save Blog Post
    os.makedirs('content/blog', exist_ok=True)
    with open(f"content/blog/{date_str}-post.html", "w") as f:
        f.write(f"<h1>{keyword}</h1><audio controls src='/static/audio/{date_str}.mp3'></audio>{blog_content}")

if __name__ == "__main__":
    main()
