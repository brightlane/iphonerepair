import os
import requests
import datetime
from openai import OpenAI

# 1. Setup Clients
# Using gpt-4o for maximum reliability and lower cost
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
EL_KEY = os.getenv("ELEVENLABS_API_KEY")
AFFILIATE_LINK = "https://elevenlabs.io/?from=l2qbqh1bg1mw"

def get_next_keyword():
    """Reads the top keyword and removes it from the list to avoid duplicates."""
    if not os.path.exists('scripts/keywords.txt'):
        print("Error: keywords.txt not found")
        return None
        
    with open('scripts/keywords.txt', 'r') as f:
        keywords = [line.strip() for line in f.readlines() if line.strip()]
    
    if not keywords:
        print("Error: No keywords left in the list")
        return None
        
    next_kw = keywords[0]
    
    # Save the remaining keywords back to the file
    with open('scripts/keywords.txt', 'w') as f:
        f.writelines("\n".join(keywords[1:]))
        
    return next_kw

def main():
    keyword = get_next_keyword()
    if not keyword:
        return

    print(f"Starting Vulture Protocol for keyword: {keyword}")

    # 2. Generate 1,500 Word SEO Post using GPT-4o
    try:
        response = client.chat.completions.create(
            model="gpt-4o",  # Updated from gpt-4-turbo to fix the 404 error
            messages=[
                {"role": "system", "content": "You are an expert SEO copywriter."},
                {"role": "user", "content": f"Write a 1500-word comprehensive guide about '{keyword}'. Focus heavily on how ElevenLabs technology solves this specific problem. Use professional HTML formatting (h2, h3, lists). Naturally include the affiliate link {AFFILIATE_LINK} at the beginning and end of the article."}
            ]
        )
        blog_content = response.choices[0].message.content
    except Exception as e:
        print(f"OpenAI Error: {e}")
        return

    date_str = datetime.datetime.now().strftime("%Y-%m-%d")

    # 3. Generate ElevenLabs Audio (using Multilingual v3)
    audio_url = "https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM" # 'Rachel' voice ID
    headers = {
        "xi-api-key": EL_KEY,
        "Content-Type": "application/json"
    }
    
    # We take the first 3500 characters of the blog for the audio summary
    payload = {
        "text": f"Welcome back. Today we are exploring {keyword}. {blog_content[:3500]}",
        "model_id": "eleven_multilingual_v3",
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}
    }
    
    try:
        audio_res = requests.post(audio_url, json=payload, headers=headers)
        if audio_res.status_code == 200:
            os.makedirs('static/audio', exist_ok=True)
            audio_path = f"static/audio/{date_str}.mp3"
            with open(audio_path, "wb") as f:
                f.write(audio_res.content)
            print("Audio generated successfully.")
        else:
            print(f"ElevenLabs Error: {audio_res.text}")
    except Exception as e:
        print(f"Audio Request Failed: {e}")

    # 4. Save the Final Blog Post
    os.makedirs('content/blog', exist_ok=True)
    file_path = f"content/blog/{date_str}-post.html"
    
    with open(file_path, "w") as f:
        # Include an audio player at the top of the post
        f.write(f"""
        <article>
            <h1>{keyword.title()}</h1>
            <p><em>Published on {date_str}</em></p>
            <div class="audio-player" style="background: #f4f4f4; padding: 20px; border-radius: 10px; margin-bottom: 30px;">
                <p><strong>Listen to this article:</strong></p>
                <audio controls src="/static/audio/{date_str}.mp3" style="width: 100%;"></audio>
            </div>
            {blog_content}
        </article>
        """)
    
    print(f"Success! File saved to {file_path}")

if __name__ == "__main__":
    main()
