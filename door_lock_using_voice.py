import speech_recognition as sr
from time import ctime
import time
import os
import RPi.GPIO as GPIO
from gtts import gTTS

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
pwm=GPIO.PWM(11,50)
pwm.start(5)

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("/home/pi/Abey/audio.mp3")
    os.system("mpeg321 /home/pi/Abey/audio.mp3")

def recordAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=2)
        print("Say something!")
        audio = r.listen(source)#listening to microphone
        data =r.recognize_google(audio)
        print("you said " + data)
        if "lock" in data:
            print("locking")
            speak("Locking")
            pwm.ChangeDutyCycle(3)
        if "unlock"in data:
            print("unlocking")
            speak("unlocking")
            pwm.ChangeDutyCycle(12)
        if "stop"  in data:
            print("closing")
            speak("closing")
            pwm.stop()
        if "" in data:
            print("starting")
            speak("setting up pwm")
            pwm.start(5)
        


time.sleep(2)

while 1:
    data = recordAudio()

pwm.stop()
