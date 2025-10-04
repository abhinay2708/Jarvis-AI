import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
from gtts import gTTS
import pygame
import os
import google.generativeai as genai

recogniser = sr.Recognizer()
engine = pyttsx3.init()

# 🔑 Configure Gemini API

genai.configure(api_key="AI.......Uk")


def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "hello.mp3"
    tts.save(filename)

    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove(filename)


def ask_gemini(question):
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(question)
        return response.text
    except Exception as e:
        return "Sorry, I could not get an answer right now."


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak("Sorry, I don't know that song.")
    else:
        # 🔹 If no fixed command, send question to Gemini
        print("Asking Gemini...")
        answer = ask_gemini(c)
        print("Gemini Answer:", answer)
        speak(answer)


if __name__ == "__main__":
    speak("Initializing Jarvis...")
    with sr.Microphone() as source:
        recogniser.adjust_for_ambient_noise(source, duration=1)
        while True:
            print("Say 'Jarvis' to wake me up...")
            try:
                audio = recogniser.listen(source, timeout=5, phrase_time_limit=5)
                word = recogniser.recognize_google(audio)
                print("You said:", word)

                if "jarvis" in word.lower():
                    speak("Yes, how can I help?")
                    # Now keep listening for commands until user says "exit"
                    while True:
                        print("Listening for command...")
                        try:
                            audio = recogniser.listen(source, timeout=5, phrase_time_limit=5)
                            command = recogniser.recognize_google(audio)
                            print("Command:", command)
                            if "exit" in command.lower():
                                speak("Okay, going back to sleep.")
                                break  # exit command mode, go back to wake word
                            else:
                                processCommand(command)
                        except sr.UnknownValueError:
                            print("Could not understand command.")
                        except sr.WaitTimeoutError:
                            print("Timeout: No command detected.")
                        except sr.RequestError as e:
                            print("API Error:", e)

            except sr.UnknownValueError:
                print("Could not understand wake word.")
            except sr.WaitTimeoutError:
                print("Timeout: No speech detected.")
            except sr.RequestError as e:
                print("API Error:", e)
