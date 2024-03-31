import os
import openai
import tempfile

openai.api_key = os.environ["OPENAI_API_KEY"]

def get_transcription(audio: bytes) :
    print("Getting transcription from OpenAi")
    
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_file:
        temp_file.write(audio)
        temp_file.seek(0)
        transcript = openai.Audio.transcribe("whisper-1", file=temp_file)

    return transcript
    