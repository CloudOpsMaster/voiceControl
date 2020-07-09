# python -m pip install --upgrade pip
# python get-pip.py
# pip install SpeechRecognition
# pip install pipwin
# pipwin install PyAudio
# pip install pyttsx3 pypiwin32
# python -m pip install pipwin

import speech_recognition as sr
import os
import sys
import webbrowser
import pyttsx3
"""
def talk(words):
   print(words)
   os.system("say " + words)

talk("Привет")   
""" 

def talk(words):
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()

talk("Привет, как дела? ")   

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Говорите")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        task = r.recognize_google(audio, language="ru-RU").lower()
        print("Вы сказали " + task)
    except sr.UnknownValueError:
        talk("Я вас не поняла")
        task = command()
    return task

def makeSomething(task):
    if 'open website' in task:
        talk("Уже открываю")
        url = 'https://google.com' 
        webbrowser.open(url)
    elif 'stop' in task:
        talk("Да, конечно")
        sys.exit()

while True:
    makeSomething(command())          


