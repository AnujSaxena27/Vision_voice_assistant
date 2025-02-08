import pyttsx3 # type: ignore
import speech_recognition as sr  # type: ignore
import datetime
import wikipedia  # type: ignore
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!") 

    print("I am Vision Sir. Please tell me how may I help you")
    speak("I am Vision Sir. Please tell me how may I help you")       

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)  # Adjusting for background noise
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:   
        print("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:  # Keeps listening for new commands
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except wikipedia.exceptions.PageError:
                speak("Sorry, I could not find any information on Wikipedia.")
            except wikipedia.exceptions.DisambiguationError:
                speak("There are multiple results for this. Please be more specific.")

        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://google.com")

        elif 'play music' in query:
            music_dir = 'C:\\ppsproject\\songs'
            if os.path.exists(music_dir) and os.listdir(music_dir):  # Check if directory exists and has files
                songs = os.listdir(music_dir)
                print(songs)    
                os.startfile(os.path.join(music_dir, songs[0]))
            else:
                speak("Music folder is empty or does not exist.")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'exit' in query or 'quit' in query:
            speak("Goodbye, Sir!")
            break  # Exits the loop
