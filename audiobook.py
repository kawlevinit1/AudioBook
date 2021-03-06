from gtts import gTTS
import os

f=open('audiobook.txt')
x=f.read()
langugage = 'en'

audio =gTTS(text=x,lang=langugage)

audio.save('audiobook.wav')
os.system('audiobook.wav')
