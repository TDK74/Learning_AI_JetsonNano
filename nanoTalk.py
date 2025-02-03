import os
import pyttsx3


text = 'Get ready Player 1. The play will be rough. Are you ready to rumble!'

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('voice', 'english+f3') # m2, m3, m4, f1, f2, f3
engine.say(text)
engine.runAndWait()
