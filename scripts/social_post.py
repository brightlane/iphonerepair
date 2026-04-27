import os
import requests

def post_to_mastodon(text):
    # Get your token from Mastodon -> Preferences -> Development
    access_token = os.getenv("MASTODON_ACCESS_TOKEN")
    instance_url = "https://mastodon.social" # Change if you use a different one
    
    if not access_token:
        print("No Mastodon token found. Skipping.")
        return

    headers = {"Authorization": f"Bearer {access_token}"}
    payload = {"status": text}
    
    res = requests.post(f"{instance_url}/api/v1/statuses", headers=headers, data=payload)
    if res.status_code == 200:
        print("Successfully tooted to Mastodon!")
    else:
        print(f"Mastodon Error: {res.text}")

def main():
    # We find the latest post from the content folder
    blog_dir = 'content/blog'
    posts = sorted([f for f in os.listdir(blog_dir) if f.endswith('.html')])
    
    if not posts:
        return
        
    latest_post = posts[-1]
    title = latest_post.replace('-post.html', '').replace('-', ' ').title()
    link = f"https://brightlane.github.io/SkyScanner/content/blog/{latest_post}"

    social_text = f"🚀 New Post: {title}\n\nCheck out our latest guide on AI Voice and ElevenLabs! #AI #Tech #Marketing\n\nRead more: {link}"
    
    # Run the posters
    post_to_mastodon(social_text)

if __name__ == "__main__":
    main()
