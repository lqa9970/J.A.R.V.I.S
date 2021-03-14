import speech_recognition
import pyttsx3
from datetime import date
import time


jarvis = ""
jarvis_speak = pyttsx3.init()
jarvis_listen = speech_recognition.Recognizer()

while True:
    with speech_recognition.Microphone() as mic:
        print("J.A.R.V.I.S: I'm Listening")
        print("J.A.R.V.I.S: ...")
        audio = jarvis_listen.listen(mic)

    try:
        you = jarvis_listen.recognize_google(audio)
    except:
        you = ""

    print("You said: " + you)

    if you == "":
        jarvis = "I can't hear you"
    elif "hello" in you:
        jarvis = "Hello QA"
    elif "date today" in you:
        today = date.today()
        jarvis = today.strftime("%B %d, %Y")
    elif "time" in you:
        now = time.localtime()
        jarvis = time.strftime("%H:%M", now)
    elif "bye" in you:
        jarvis = "Thank you, have a nice day. See you next time"
        print("J.A.R.V.I.S: " + str(jarvis))

        jarvis_speak.say(jarvis)
        jarvis_speak.runAndWait()
        break
    else:
        jarvis = "I'm good, thanks"

    print("J.A.R.V.I.S: " + str(jarvis))

    jarvis_speak.say(jarvis)
    jarvis_speak.runAndWait()