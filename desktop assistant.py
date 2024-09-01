import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install SpeechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


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

    speak("Greetings I am Alex Sir. Please tell me how may I help you")


def takeCommand():
    # Takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print(e)
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


def takeNotes(note):
    # Save the note to a text file and open it in Notepad
    file_name = "notes.txt"
    with open(file_name, "a") as file:
        file.write(note + "\n")
    os.startfile(file_name)  # Open the file in Notepad


def searchGoogle(query):
    # Search the specified query on Google
    webbrowser.open(f"https://www.google.com/search?q={query}")


def searchYouTube(query):
    # Search the specified query on YouTube
    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")


if __name__ == "__main__":
    wishMe()
    while True:
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

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Visual Studio\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to siddhesh' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "siddheshghadi0908mail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email")

        elif 'take notes' in query:
            speak("What would you like me to note down?")
            note = takeCommand()
            takeNotes(note)
            speak("I have made a note of that.")

        elif 'search google' in query:
            speak("What should I search on Google?")
            search_query = takeCommand()
            searchGoogle(search_query)

        elif 'search youtube' in query:
            speak("What should I search on YouTube?")
            search_query = takeCommand()
            searchYouTube(search_query)
