import os
import requests
from openai import OpenAI

# Initialize Clients
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
EL_API_KEY = os.getenv("ELEVENLABS_API_KEY")

def generate_audio(text, filename):
    # Uses your ElevenLabs affiliate logic
    url = "https://api.elevenlabs.io/v1/text-to-speech/YOUR_VOICE_ID"
    headers = {"xi-api-key": EL_API_KEY, "Content-Type": "application/json"}
    data = {
        "text": text[:5000], # First 5000 chars for preview/narrator
        "model_id": "eleven_multilingual_v3",
        "voice_settings": {"stability": 0.45, "similarity_boost": 0.8}
    }
    response = requests.post(url, json=data, headers=headers)
    with open(f"static/audio/{filename}.mp3", "wb") as f:
        f.write(response.content)

# 1. Select Next Keyword from your 10,000 list
# 2. Generate 1,500 word post with OpenAI
# 3. Generate Audio with ElevenLabs
# 4. Save as Markdown for Jekyll/Hugo
