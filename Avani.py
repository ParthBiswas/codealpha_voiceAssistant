import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Avani Sir. Please tell me how may I help you")     
    


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("ok sir!")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("okey sir!")
            
        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com/")
            speak("ok sir!")

            
        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com/")
            speak("ok Sir!")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")  
            speak("ok Sir!")
            
        elif 'open linkedin' in query:
            webbrowser.open("https://www.linkedin.com/feed/")   
            speak("ok Sir!")
            
        elif 'open utu' in query:
            webbrowser.open("https://uktech.ac.in/en")   
            speak("ok Sir!")
            
        elif 'open github' in query:
            webbrowser.open("https://github.com/explore")   
            speak("ok Sir!")
            
        elif 'open flipkart' in query:
            webbrowser.open("https://www.flipkart.com/")   
            speak("ok Sir!")
            
        elif 'open link' in query:
            webbrowser.open("https://in.indeed.com/?r=us")  
            speak("ok Sir!")
            
             
        elif 'open naukri' in query:
            webbrowser.open("https://www.naukri.com/mnjuser/homepage")   
            speak("Ok Sir")


        elif 'play music' in query:
            music_dir = 'D:\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("ok Sir!")
            
        elif 'open movies' in query:
            music_dir = 'D:\Movies'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("ok Sir!")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

    

        elif 'email to Parth Sir' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "#"    
                sendEmail(to, content)
                speak("Email has been sent! Sir")
            except Exception as e:
                print(e)
                speak("Sorry my friend bhai.")
