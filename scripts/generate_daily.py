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
    return keywords[0], keywords[1:]

def main():
    result = get_next_keyword()
    if not result:
        print("No keywords found.")
        return
    
    keyword, remaining_keywords = result

    # 1. Generate Blog Post + Social Media Caption
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a professional SEO copywriter and viral social media marketer."},
                {"role": "user", "content": f"1. Write a 1500-word deep-dive guide for '{keyword}'. Focus on ElevenLabs. Use HTML tags. Include {AFFILIATE_LINK}. 2. At the very end, provide a 'SOCIAL_START' section with a viral tweet and a LinkedIn post."}
            ]
        )
        full_content = response.choices[0].message.content
        
        # Save the remaining keywords if the AI call worked
        with open('scripts/keywords.txt', 'w') as f:
            f.writelines("\n".join(remaining_keywords))
            
    except Exception as e:
        print(f"OpenAI Error (Check Quota): {e}")
        return

    date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    post_url = f"https://brightlane.github.io/SkyScanner/content/blog/{date_str}-post.html"

    # 2. Generate Audio Narration
    audio_url = "https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM"
    headers = {"xi-api-key": EL_KEY, "Content-Type": "application/json"}
    payload = {
        "text": f"New guide on {keyword}. {full_content[:3000]}", 
        "model_id": "eleven_multilingual_v3"
    }
    
    try:
        audio_res = requests.post(audio_url, json=payload, headers=headers)
        os.makedirs('static/audio', exist_ok=True)
        os.makedirs('content/blog', exist_ok=True)

        with open(f"static/audio/{date_str}.mp3", "wb") as f:
            f.write(audio_res.content)

        with open(f"content/blog/{date_str}-post.html", "w") as f:
            f.write(f"<h1>{keyword}</h1><audio controls src='/static/audio/{date_str}.mp3'></audio>{full_content}")
        
        # 3. VULTURE SOCIAL BLAST
        # This sends the update to your Discord, which you can link to X/LinkedIn
        webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
        if webhook_url:
            social_payload = {
                "content": f"🚀 **Vulture Protocol Active**\n**Topic:** {keyword}\n**Link:** {post_url}\n\n*The AI has also prepared viral captions in the blog file!*"
            }
            requests.post(webhook_url, json=social_payload)
            print("Social blast sent to Discord.")

        print(f"Success: Generated post and social for {keyword}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
