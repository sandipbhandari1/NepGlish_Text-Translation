import sounddevice as sd
import scipy.io.wavfile as wav
import numpy as np
import whisper
from gtts import gTTS
import os
import sys

# ── Settings ──────────────────────────────────────────
SAMPLE_RATE  = 16000       # Whisper requires 16kHz
DURATION     = 10          # seconds to record your voice
INPUT_FILE   = "input.wav"
OUTPUT_FILE   = "output.mp3"
TRANSCRIPT_FILE = "transcript.txt"
WHISPER_MODEL  = "base"     # tiny | base | small | medium
# ──────────────────────────────────────────────────────


def record_voice():
    """Step 1: Record your Nenglish voice"""
    print("\n🎤 Speak now! Recording for {} seconds...".format(DURATION))

    audio = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="int16"
    )
    sd.wait()

    wav.write(INPUT_FILE, SAMPLE_RATE, audio)
    print("✓ Voice recorded → {}".format(INPUT_FILE))
    return INPUT_FILE


def load_wav_audio(audio_file):
    """Load a WAV file without requiring ffmpeg."""
    if not audio_file.lower().endswith(".wav"):
        raise ValueError("Only WAV input is supported without ffmpeg: {}".format(audio_file))

    sample_rate, data = wav.read(audio_file)
    if data.ndim > 1:
        data = np.mean(data, axis=1)

    if data.dtype == np.int16:
        audio = data.astype(np.float32) / 32768.0
    elif data.dtype == np.int32:
        audio = data.astype(np.float32) / 2147483648.0
    elif data.dtype == np.uint8:
        audio = (data.astype(np.float32) - 128) / 128.0
    else:
        audio = data.astype(np.float32)

    return audio, sample_rate


def transcribe_voice(audio_file):
    """Step 2: Use Whisper to convert your speech to text"""
    print("\n Transcribing with Whisper...")

    model = whisper.load_model(WHISPER_MODEL)

    if audio_file.lower().endswith(".wav"):
        audio, sample_rate = load_wav_audio(audio_file)
        if sample_rate != SAMPLE_RATE:
            raise ValueError("Expected {} Hz WAV, got {} Hz".format(SAMPLE_RATE, sample_rate))
        result = model.transcribe(audio, language=None, task="transcribe")
    else:
        result = model.transcribe(audio_file, language=None, task="transcribe")

    text = result["text"].strip()
    detected_lang = result.get("language", "unknown")

    print("✓ Detected language : {}".format(detected_lang))
    print("✓ You said          : \"{}\"".format(text))
    return text


def copy_sentence(text):
    """Copy the transcribed sentence before speaking it back."""
    if not text:
        return text

    print("\n🧠 AI is copying your sentence...")
    copied = text
    print("✓ Copied sentence   : \"{}\"".format(copied))
    return copied


def save_text(text, filename):
    """Save the transcribed sentence to a text file."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    print("✓ Saved transcription to {}".format(filename))


def choose_tts_language(text):
    """Choose the best gTTS voice language for the transcribed text."""
    if any("\u0900" <= ch <= "\u097F" for ch in text):
        return "ne"
    if any("\u0600" <= ch <= "\u06FF" for ch in text):
        return "ur"
    return "en"


def speak_text(text):
    """Step 3: Speak the transcribed text back aloud"""
    if not text:
        print("⚠ Nothing to speak — transcription was empty.")
        return

    lang = choose_tts_language(text)
    print("\n🔊 Speaking back using {} voice...".format(lang))

    tts = gTTS(text, lang=lang)
    tts.save(OUTPUT_FILE)

    if sys.platform == "win32":
        os.system("start {}".format(OUTPUT_FILE))
    elif sys.platform == "darwin":
        os.system("afplay {}".format(OUTPUT_FILE))
    else:
        os.system("mpg321 {} 2>/dev/null || ffplay -nodisp -autoexit {}".format(
            OUTPUT_FILE, OUTPUT_FILE))

    print("✓ Done speaking!")


def speak_text_from_file(filename):
    """Read text from a file and speak it back."""
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read().strip()

    if not text:
        print("⚠ Transcript file is empty.")
        return

    print("\n🔊 Speaking from saved transcript...")
    speak_text(text)


def run():
    print("=" * 50)
    print("  Nenglish Voice Pipeline")
    print("  Record → Transcribe → Speak")
    print("=" * 50)

    while True:
        input("\nPress ENTER to start recording (Ctrl+C to quit)...")

        audio_file = record_voice()
        text = transcribe_voice(audio_file)
        copied = copy_sentence(text)
        save_text(copied, TRANSCRIPT_FILE)
        speak_text_from_file(TRANSCRIPT_FILE)

        print("\n" + "-" * 50)
        print("  Written : \"{}\"".format(copied))
        print("-" * 50)


if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print("\n\nGoodbye!")