import pyttsx3

jarvis_brain = input()

jarvis_speak = pyttsx3.init()
jarvis_speak.say(jarvis_brain)
jarvis_speak.runAndWait()