import os
import uuid
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs

# Load your API key from environment variable
# Make sure you set ELEVENLABS_API_KEY in your system or .env file
from config import ELEVENLABS_API_KEY

# Initialize the ElevenLabs client
client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

def text_to_speech_file(text: str,folder:str) -> str:
    """
    Convert text to speech using ElevenLabs and save as an MP3 file.
    Returns the path to the saved file.
    """
    # Call the ElevenLabs TTS API
    response = client.text_to_speech.convert(
        voice_id="pNInz6obpgDQGcFmaJgB",  # Adam pre-made voice
        output_format="mp3_22050_32",      # MP3 format, 22kHz, 32kbps
        text=text,
        model_id="eleven_turbo_v2_5",      # Turbo model for low latency
        voice_settings=VoiceSettings(
            stability=0.5,                 # Controls consistency of voice
            similarity_boost=0.75,         # How close to the original voice
            style=0.5,                     # Expressiveness
            use_speaker_boost=True         # Boost clarity
        )
    )
    # Generate a unique filename
    filename = os.path.join(f"user_uploads/{folder}","audio.mp3")

    # Save the audio chunks to file
    with open(filename, "wb") as f:
        for chunk in response:
            f.write(chunk)

    print(f"{filename}: A new audio file was saved successfully!") # Return the path of the saved audio file 
    return filename




