A Python voice recording, transcription, and speech synthesis pipeline that works with mixed Nepali-English speech (Nepglish).

## Features

- 🎤 **Record audio** from your microphone (10 seconds)
- 🔄 **Transcribe speech** using OpenAI Whisper (supports multiple languages)
- 💾 **Save transcriptions** to a text file
- 🔊 **Speak text aloud** using Google Text-to-Speech (gTTS)
- 🌍 **Multi-language support** - automatically detects Nepali, Urdu, and English
- ⚡ **No ffmpeg required** - loads WAV files directly with scipy

## How It Works

```
Record Audio (10 sec) → Transcribe with Whisper → Save to Text File → Speak Aloud with gTTS
```

### Pipeline Steps

1. **Recording**: Captures microphone input at 16 kHz and saves as `input.wav`
2. **Transcription**: Uses OpenAI Whisper to convert audio to text (detects language automatically)
3. **Text Saving**: Writes the transcribed text to `transcript.txt`
4. **Speech Synthesis**: Generates audio using Google Text-to-Speech and plays it back

## Installation

### Requirements

- Python 3.8 or higher
- Windows, macOS, or Linux

- sounddevice>=0.4.6
scipy>=1.10.0
numpy>=1.24.0
openai-whisper>=20230314
gtts>=2.3.0
fpdf2>=2.7.0

### Install Dependencies

```bash
pip install sounddevice scipy numpy whisper gtts fpdf2
```

Or install from requirements file:

```bash
pip install -r requirements.txt
```

## Usage

### Main Pipeline (Record → Transcribe → Speak)

```bash
python nenglish_pipeline.py
```

Then:
1. Press **ENTER** to start recording
2. Speak your sentence for 10 seconds
3. The script will transcribe your speech
4. Your sentence will be played back aloud

### Standalone Recording (10 seconds)

```bash
python record_voice.py
```

Saves to `input.wav`

### Standalone Speech Output

```bash
python speak_greeting.py
```

Speaks the greeting: "Namaskar Global IME Bank ma swagatam cha"

### Generate Documentation PDF

```bash
python create_pdf_summary.py
