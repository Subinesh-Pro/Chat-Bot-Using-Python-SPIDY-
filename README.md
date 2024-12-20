# SPIDY - Voice Assistant

## Overview
SPIDY is a Python-based voice assistant created by students at A I H T. It is capable of performing various tasks like searching the web, telling the time, sending emails, controlling the computer, and much more. The assistant responds to voice commands and is designed to make tasks easier for users.

---

## Features

### Voice Commands:
- **Wikipedia Search**: Search Wikipedia articles.
- **Open Websites**: Open websites like YouTube, Google, Stack Overflow, etc.
- **Music**: Open Spotify and play music.
- **Time**: Tell the current time.
- **Send Email**: Send an email via Gmail.
- **News**: Get the latest news from Times of India.
- **Weather**: Get weather information from OpenWeatherMap.
- **Jokes**: Tell jokes using the pyjokes library.
- **Python IDE**: Open an online Python IDE.
- **Shutdown, Restart, and Lock**: Perform system shutdown, restart, or lock the computer.
- **Change Background**: Change the wallpaper.
- **Write and Show Notes**: Write notes and show them.
- **Message Sending**: Send SMS using Twilio's API.

### Functionalities:
1. **Text-to-Speech**: SPIDY speaks to the user using `pyttsx3`.
2. **Speech Recognition**: SPIDY listens to user commands using `speech_recognition`.
3. **Web Browsing**: SPIDY can search on Google and open URLs using `webbrowser`.
4. **Email Service**: SPIDY can send emails using Gmail’s SMTP server.
5. **News API Integration**: Fetches the latest news from Times of India.
6. **Weather API Integration**: Provides current weather information using OpenWeatherMap API.
7. **SMS Service**: Sends SMS via Twilio's API.

---

## Requirements

Before running the project, make sure you have the following Python libraries installed:
1. `pyttsx3` - for text-to-speech conversion
2. `speech_recognition` - for recognizing speech
3. `wikipedia` - for searching Wikipedia
4. `pyjokes` - for telling jokes
5. `pywin32` - for Windows-specific functionality
6. `requests` - for sending HTTP requests
7. `smtplib` - for sending emails via Gmail
8. `twilio` - for sending SMS messages
9. `wolframalpha` - for calculating mathematical expressions
10. `webbrowser` - for opening websites
11. `ctypes` - for system operations like locking the workstation
12. `shutil` - for interacting with system files
13. `winshell` - for managing the recycle bin
14. `feedparser` - for RSS feed parsing
15. `time` and `datetime` - for time-related operations
16. `json` - for handling JSON data from APIs

### Installation
To install the required libraries, you can use `pip`:

```bash
pip install pyttsx3 speech_recognition wikipedia pyjokes pywin32 requests smtplib twilio wolframalpha webbrowser ctypes shutil winshell feedparser
