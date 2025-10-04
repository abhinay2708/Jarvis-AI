# Jarvis AI – Voice-Activated Personal Assistant 🤖

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)](https://www.python.org/)
[![GitHub Repo Size](https://img.shields.io/github/repo-size/abhinay2708/jarvis-ai)](https://github.com/abhinay2708/jarvis-ai)
[![GitHub Stars](https://img.shields.io/github/stars/abhinay2708/jarvis-ai?style=social)](https://github.com/abhinay2708/jarvis-ai/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/abhinay2708/jarvis-ai?style=social)](https://github.com//jarvis-ai/network/members)
[![GitHub Issues](https://img.shields.io/github/issues/abhinay2708/jarvis-ai)](https://github.com/abhinay2708/jarvis-ai/issues)
[![License](https://img.shields.io/github/license/abhinay2708/jarvis-ai)](LICENSE)

---

## **Overview**

**Jarvis AI** is a Python-based voice assistant that can:  

- Recognize a wake word (“Jarvis”)  
- Execute voice commands to open websites and play music  
- Answer general questions using **Google Gemini API**  
- Provide real-time **text-to-speech responses**  

It combines **speech recognition, AI APIs, and automation** to create a personal assistant experience.

---

## **Features**

- Wake word detection: Say **“Jarvis”** to activate. 🎤  
- Open popular websites:
  - Google, YouTube, LinkedIn, Facebook  
- Play songs from a custom library 🎵  
- Ask **any question** and get answers via **Google Gemini API** 🤖  
- Continuous command listening until user says `"exit"`  
- Text-to-speech responses using **gTTS** 🔊  

---

## **Technologies Used**

- **Python 3.10**  
- **Pygame** – Audio playback  
- **SpeechRecognition** – Voice input  
- **PyAudio** – Microphone support  
- **gTTS** – Text-to-speech  
- **Google Gemini API** – AI question answering  
- **Requests** – API calls (optional)  
- **musiclibrary** – Custom song library  

---

Usage

Run the application:

python app.py


Say “Jarvis” to wake up the assistant.

Speak commands or ask questions:

"Open Google" → Opens Google in your browser

"Play Believer" → Plays the song from your library

"Who is the Prime Minister of India?" → Gemini answers

Say "exit" to stop command mode and return to wake word mode.

Project Structure
jarvis-ai/
│
├─ app.py               # Main application
├─ musiclibrary.py      # Custom song library
├─ requirements.txt     # Required Python packages
├─ README.md            # Project documentation
├─ LICENSE              # MIT License
└─ .venv/               # Virtual environment (optional)

Acknowledgements

Thanks to the Pygame, gTTS, SpeechRecognition, and Google Gemini communities.

Future Improvements

Add continuous conversation context

Integrate with Google Calendar, Gmail, and other tools

Add GUI interface using Tkinter or PyQt

Implement offline wake word detection for faster response
