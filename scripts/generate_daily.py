import os
import requests
import datetime
from openai import OpenAI

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
    if not result: return
    keyword, remaining = result

    # 1. Generate Blog + Social Post
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a viral social media and SEO expert."},
            {"role": "user", "content": f"1. Write a 1500-word guide for '{keyword}' with HTML. 2. Provide a 280-character viral tweet and a LinkedIn post promoting it with the link: https://brightlane.github.io/SkyScanner/content/blog/{datetime.datetime.now().strftime('%Y-%m-%d')}-post.html"}
        ]
    )
    content = response.choices[0].message.content
    
    # Split the AI response (Assuming the AI follows instructions)
    # Note: In a real run, we'd use better parsing, but this gets the job done!
    
    # Save the blog and audio as usual...
    os.makedirs('content/blog', exist_ok=True)
    date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    
    with open(f"content/blog/{date_str}-post.html", "w") as f:
        f.write(content)
        
    # 2. Fire the 'Social Webhook' (The Vulture's Voice)
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
    if webhook_url:
        social_msg = f"📢 Vulture Daily Update!\nNew Guide: {keyword}\nRead: https://brightlane.github.io/SkyScanner/content/blog/{date_str}-post.html"
        requests.post(webhook_url, json={"content": social_msg})

    # Save remaining keywords
    with open('scripts/keywords.txt', 'w') as f:
        f.writelines("\n".join(remaining))

if __name__ == "__main__":
    main()
