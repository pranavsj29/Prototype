
"""
Created on Sun Dec 26 19:44:35 2021

@author: hp
"""

import pyttsx3
import datetime
import webbrowser
import os
import wikipedia
import speech_recognition as sr
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
'''print(voices[2].id)'''
engine.setProperty('voice', voices[2].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12 :
        speak('good morning')
        print("good morning")
    elif hour>=12 and hour < 18:
        speak('good after noon')
        print("good after noon")
        
    else:
        speak('good evening')
        print("good evening")
        
    speak(' i am prototype sir , how may i help you')
    print(' i am prototype sir , how may i help you')


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"boss said: {query}\n")  #User query will be printed.

    except Exception as e:
          
        print("Say that again please...")   
        return "None" 
    return query
        
        

wishMe()

if __name__ == "__main__":
    query = takeCommand().lower()
    print(takeCommand())
    if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
    elif 'open youtube' in query:
            webbrowser.open("youtube.com")
    elif 'open google' in query:
            webbrowser.open("google.com")
    elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
    elif 'open dev' in query:
            codePath = "D:\\software\\Dev-Cpp\\devcpp.exe"
            os.startfile(codePath)
            speak("opening")
    elif 'open calculator'in query:
            codePath = ""
            os.startfile(codePath)
            speak("opening")
    elif 'shutdown' or 'shut down' in query:
            speak("shutting down the system")
            os.system("shutdown /s /t 1")

    
    
    
    
    
    