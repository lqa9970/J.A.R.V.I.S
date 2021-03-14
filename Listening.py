import speech_recognition

jarvis_listen = speech_recognition.Recognizer()

with speech_recognition.Microphone() as mic:
    print("J.A.R.V.I.S: I'm Listening")
    audio = jarvis_listen.listen(mic)

try:
    you = jarvis_listen.recognize_google(audio)
except:
    you = ""

print("You said:" + you)
print("Thank you, have a nice day")