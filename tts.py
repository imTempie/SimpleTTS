import gtts
from playsound import playsound

tts = gtts.gTTS(input())

tts.save("textToSpeech.mp3")

playsound("textToSpeech.mp3")
