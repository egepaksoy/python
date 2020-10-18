from gtts import gTTS
from playsound import playsound
import os
import random

def speak(string):
    tts = gTTS(string, lang='en')
    rand = random.randint(1,1000)
    file = 'audio-'+str(rand)+'.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)
    return string
