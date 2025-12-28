import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import time

# ---------------- SPEAK FUNCTION ----------------
def speak(text):
    print("Assistant:", text)
    engine = pyttsx3.init('sapi5')     # recreate engine every time
    engine.setProperty('rate', 170)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # 0 = male, 1 = female
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# ---------------- LISTEN FUNCTION ----------------
def take_command(timeout=5, phrase_time_limit=5):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.7)
        try:
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
        except Exception:
            return ""

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio, language="en-in")
        print("You said:", command)
        return command.lower()
    except:
        return ""

# ---------------- GREETING ----------------
def wish_me():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good Morning")
    elif hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am your voice assistant. How can I help you?")

# ---------------- MAIN PROGRAM ----------------
if __name__ == "__main__":
    wish_me()

    while True:
        command = take_command()

        if not command:
            continue

        if "time" in command:
            speak("The time is " + datetime.datetime.now().strftime("%H:%M:%S"))

        elif "date" in command:
            speak("Today's date is " + datetime.datetime.now().strftime("%d %B %Y"))

        elif "open google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif "open instagram" in command:
            speak("Opening instagram")
            webbrowser.open("https://www.instagram.com")

        elif "search" in command:
            speak("What should I search?")
            query = take_command(timeout=8, phrase_time_limit=6)

            if not query:
                speak("Please say it again")
                query = take_command(timeout=8, phrase_time_limit=6)

            if query:
                speak("Searching for " + query)
                webbrowser.open(f"https://www.google.com/search?q={query}")
            else:
                speak("Search cancelled")

        elif "bye" in command or "quit" in command:
            speak("Goodbye")
            break
