import sounddevice as sd
import scipy.io.wavfile as wav

SAMPLE_RATE = 16000
DURATION = 10
OUTPUT_FILE = "input.wav"

audio = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype="int16")
sd.wait()
wav.write(OUTPUT_FILE, SAMPLE_RATE, audio)
print(f"Saved recording to {OUTPUT_FILE}")
