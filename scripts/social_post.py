import os
import requests

def post_to_social():
    # 1. Find the latest blog post created today
    blog_dir = 'content/blog'
    if not os.path.exists(blog_dir):
        print("Blog directory not found.")
        return
        
    posts = sorted([f for f in os.listdir(blog_dir) if f.endswith('.html')])
    if not posts:
        print("No posts found to share.")
        return
        
    latest_post = posts[-1]
    # Clean up the filename for a pretty title
    title = latest_post.replace('-post.html', '').replace('-', ' ').title()
    url = f"https://brightlane.github.io/SkyScanner/content/blog/{latest_post}"

    message = f"🚀 New AI Guide: {title}\n\nLearn how to scale your content with ElevenLabs! \n\nRead more here: {url}\n\n#AI #ElevenLabs #DigitalMarketing"

    # 2. Post to Mastodon (Great for SEO Indexing)
    mastodon_token = os.getenv("MASTODON_ACCESS_TOKEN")
    if mastodon_token:
        res = requests.post(
            "https://mastodon.social/api/v1/statuses",
            headers={"Authorization": f"Bearer {mastodon_token}"},
            data={"status": message}
        )
        print(f"Mastodon Status: {res.status_code}")

    # 3. Post to Discord Webhook (Instant notification for you)
    discord_webhook = os.getenv("DISCORD_WEBHOOK_URL")
    if discord_webhook:
        requests.post(discord_webhook, json={"content": message})
        print("Discord notification sent.")

if __name__ == "__main__":
    post_to_social()
