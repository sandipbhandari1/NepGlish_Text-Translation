from gtts import gTTS
import os

text = "Namaskar Global IME Bank ma swagatam cha"

tts = gTTS(text, lang="ne")
tts.save("greeting.mp3")
os.system("start greeting.mp3")

    