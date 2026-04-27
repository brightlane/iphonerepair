import os
import requests
import datetime
from openai import OpenAI

# Setup Clients
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
EL_KEY = os.getenv("ELEVENLABS_API_KEY")
AFFILIATE_LINK = "https://elevenlabs.io/?from=l2qbqh1bg1mw"

def get_next_keyword():
    if not os.path.exists('scripts/keywords.txt'):
        return None
    with open('scripts/keywords.txt', 'r') as f:
        keywords = [line.strip() for line in f.readlines() if line.strip()]
    if not keywords:
        return None
    next_kw = keywords[0]
    # We only remove the keyword if the process actually starts
    return next_kw, keywords[1:]

def main():
    result = get_next_keyword()
    if not result:
        print("No keywords found.")
        return
    
    keyword, remaining_keywords = result

    # 1. Generate Blog Post with Error Handling for Quota
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a professional SEO copywriter."},
                {"role": "user", "content": f"Write a 1500-word deep-dive guide for '{keyword}'. Focus on ElevenLabs solutions. Use HTML tags. Include {AFFILIATE_LINK} in intro/outro."}
            ]
        )
        blog_html = response.choices[0].message.content
        
        # If successful, remove the keyword from the list
        with open('scripts/keywords.txt', 'w') as f:
            f.writelines("\n".join(remaining_keywords))
            
    except Exception as e:
        if "insufficient_quota" in str(e):
            print("!!! ERROR: OpenAI Account is out of credits. Add funds to your billing dashboard. !!!")
        else:
            print(f"OpenAI Error: {e}")
        return

    date_str = datetime.datetime.now().strftime("%Y-%m-%d")

    # 2. Generate Audio Narration
    audio_url = "https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM"
    headers = {"xi-api-key": EL_KEY, "Content-Type": "application/json"}
    payload = {
        "text": f"Topic: {keyword}. {blog_html[:3000]}", 
        "model_id": "eleven_multilingual_v3"
    }
    
    try:
        audio_res = requests.post(audio_url, json=payload, headers=headers)
        os.makedirs('static/audio', exist_ok=True)
        os.makedirs('content/blog', exist_ok=True)

        with open(f"static/audio/{date_str}.mp3", "wb") as f:
            f.write(audio_res.content)

        with open(f"content/blog/{date_str}-post.html", "w") as f:
            f.write(f"<h1>{keyword}</h1><audio controls src='/static/audio/{date_str}.mp3'></audio>{blog_html}")
        
        print(f"Success: Generated post for {keyword}")
    except Exception as e:
        print(f"Audio/Save Error: {e}")

if __name__ == "__main__":
    main()
