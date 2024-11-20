import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import webbrowser
import os

engine = pyttsx3.init()

def talk(text):
    """Converts text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listens to the user's voice input and converts it to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            voice = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            command = recognizer.recognize_google(voice)
            return command.lower()
        except sr.UnknownValueError:
            talk("Sorry, I didn't catch that. Can you repeat?")
            return "none"
        except sr.RequestError:
            talk("Sorry, there seems to be an issue with the speech recognition service.")
            return "none"
        except Exception as e:
            talk(f"An error occurred: {e}")
            return "none"

def execute_command(command):
    """Executes the command based on user input."""
    if "play" in command:
        song = command.replace("play", "").strip()
        talk(f"Playing {song} on YouTube.")
        pywhatkit.playonyt(song)

    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        talk(f"The current time is {time}.")

    elif "open google" in command:
        talk("Opening Google.")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        talk("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")

    elif "search for" in command:
        search_query = command.replace("search for", "").strip()
        talk(f"Searching for {search_query}.")
        pywhatkit.search(search_query)

    elif "shut down" in command or "exit" in command:
        talk("Goodbye! Have a nice day.")
        exit()

    else:
        talk("Sorry, I don't understand that command.")

def main():
    talk("Hello! I am your voice assistant. How can I help you today?")
    while True:
        command = listen()
        if command != "none":
            execute_command(command)

if __name__ == "__main__":
    main()
