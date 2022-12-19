import pyttsx3
import datetime
import speech_recognition as sr
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
'''print(voices[1].id)'''
engine.setProperty('voice',voices[1].id)


def speak (audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12 :
        speak('good morning')
    elif hour>=12 and hour < 18:
        speak('good after noon')
        
    else:
        speak('good evening')
        
    speak(' i am prototype sir , how may i help you')
def takecommand():
    r= sr.Recognizer()
    with sr.Microphone()as source:
        print('listening boss....')
        r.pause_threshold= 1
        audio=r.listen(source)
        
        
        
       
        
    try:
        print('recognizing...')
        quary=r.recognize_google(audio,language='en-in')
        print(f'user said: {query}\n')
        
        

if __name__ == "__main__":
    wishMe()
    takecommand()