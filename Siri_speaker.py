import win32com.client as wincom
import time
speak = wincom.Dispatch("SAPI.SpVoice")
print("Welcome to the MY First Siri its just know to pronounce what u ask her to pronounce: ")
while True:
   text =input("enter your text:\n")
   if text=="q":
      speak.Speak("See you soon friend, Time to say you a goodbie!")
      break
   speak.Speak(text)


