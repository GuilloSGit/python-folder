import os
from openai import OpenAI
import dotenv
from flask import Flask, render_template

dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY2")

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("recorder.html")


@app.route("/audio", methods=["POST"])
def audio():
    audio = request.files.get("audio")
    audio.save("audio.mp3")
    transcription = openai.Audio.transcribe("whisper-1", open("audio.mp3", "rb"))
    return {"result": "ok", "text": transcription.text}