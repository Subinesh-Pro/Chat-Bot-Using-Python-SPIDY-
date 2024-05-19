import subprocess
from telnetlib import EC
import wolframalpha
import pyttsx3
import json
import speech_recognition as sr
import threading
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
import win32com.client as wincl
from urllib.request import urlopen
import sys
import smtplib
import feedparser

# Initialize the pyttsx3 engine
engine = pyttsx3.init('sapi5')

# Get and set the voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Use voices[0] for the first voice

# Set the speaking rate (speed) and volume
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)

# Define the speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Define the slowprint function
def slowprint(text, delay=0.1):
    for char in text + '\n':
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

# Define the function to print slowly and speak simultaneously
def speak_and_print(text, delay=0.1):
    # Print the text slowly to the console
    slowprint(text, delay)
    # Speak the text
    speak(text)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak_and_print("Happy Morning Sir!")
    elif hour >= 12 and hour < 18:
        speak_and_print("Good Afternoon Sir!")
    else:
        speak_and_print("Good Evening Sir!")
    
    assname = "SPIDY AT FIELD"
    speak_and_print("SPIDY AT FIELD")
    speak_and_print("I am your voice Assistant")
    speak_and_print(assname)

def username():
    speak_and_print("can I know your name")
    uname = input()
    if uname:
        speak_and_print(f"Welcome sir, {uname}")
    columns = shutil.get_terminal_size().columns

    print("__________________________________________________________________________________________________________________".center(columns))
    print(f"Welcome, {uname}".center(columns))
    print("__________________________________________________________________________________________________________________".center(columns))

    speak_and_print("What can I do for you?")

def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        speak_and_print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        speak_and_print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # Enable low security in gmail
    server.login('your email id', 'your email password')
    server.sendmail('your email id', to, content)
    server.close()

if __name__ == '__main__':
    # Clear the console screen
    clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
    clear()

    wishMe()
    username()

    while True:

        query = takeCommand().lower()

        if 'wikipedia' in query:
            try:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=3)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                print(e)
                speak("i coundn't get the topic...can you tell the topic with more clearity and command the topic with the word wikipedia")


        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("https://www.google.co.in/url")

        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("https://stackoverflow.com/")

        elif 'music' in query or 'play music' in query:
            speak("Here you go to Spotify\n")
            webbrowser.open(("https://open.spotify.com/"))


        elif 'the time' in query or 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            speak_and_print(strTime)
            print()



        elif 'send a mail' in query:
            try:
                speak("sure sir, i may send mail from the mail i d of spidysubin46@gmail.com")
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                server.login('spidysubin46@gmail.com', 'hyuu cgds lmoq vjzb')

                speak("What should I say in the email?")
                content = takeCommand()
                subject = "Subject of the email"
                body = content
                msg = f"Subject: {subject}\n\n{body}"

                speak("To whom should I send the email?")
                to =int()
                server.sendmail('spidysubin@gmail.com', to, msg)
                server.close()

                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")





        elif 'how are you' in query:
            speak("I am good, Thank you for asking")
            speak("How are you, dued")



        elif 'fine' in query or "good" in query or "doing well"in query:
            speak("It's good to know that your doing well")


        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query


        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assname = takeCommand()
            speak("Thanks for naming me")


        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)


        elif 'exit' in query or 'quit' in query:
            speak("Thanks for giving me your time")
            exit()


        elif "who made you" in query or "who created you" in query:
            speak("I have been created by a i h t students")


        elif 'joke' in query:
            speak(pyjokes.get_joke())
        elif 'news' in query:

            try:
                jsonObj = urlopen("https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=timesofIndiaApikey")
                data = json.load(jsonObj)
                i = 1

                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============''' + '\n')

                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:

                print(str(e))


        elif "calculate" in query:
            app_id = "QW23R8-E5PAH2UQQ4"
            try:
                client = wolframalpha.Client(app_id)
                indx = query.lower().split().index('calculate')
                query = query.split()[indx + 1:]
                query = ' '.join(query)
                res = client.query(query)
                answer = next(res.results).text
                print("The answer is " + answer)
                speak("The answer is " + answer)
            except Exception as e:
                print("An error occurred:", str(e))
                speak("Sorry, I couldn't perform the calculation. Please try again.")



        elif 'search' in query or 'play' in query:

            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)

        elif "who i am" in query:
            speak("If you talk then definitely your human.")

        elif "why you came to world" in query:
            speak("Thanks to a i h t students. further It's a secret")

        elif 'python' in query:
            speak("opening python I D L E ")
            webbrowser.open("https://www.programiz.com/python-programming/online-compiler/")

        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")

        elif "who are you" in query:
            speak("I am your virtual assistant created by a i h t students")

        elif 'reason for you' in query:
            speak("I was created as a Minor project by a i h t students ")

        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,
                                                       1,
                                                       "Location of wallpaper",
                                                       1)
            speak("Background changed successfully")

        elif 'open chrome' in query:
            application = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(application)


        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled")

        elif "don't listen" in query or "stop listening" in query:
            speak("For how much time (in seconds) do you want to stop Spidy from listening to commands?")
            duration_text = takeCommand()

            try:
                duration = int(duration_text)
                print("Duration:", duration, "seconds")
            except ValueError:
                speak("Sorry, I couldn't understand the duration. Please provide a valid number of seconds.")


        elif 'where is' in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.com/maps/@12.2075335,79.6389814,15z?entry=ttu" + location + "")

        elif "camera" in query or "take a photo" in query:
            EC.capture(0, "spidy Camera ", "img.jpg")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            try:
                speak("What should I write on?")
                note = takeCommand()
                file = open('spidy.txt', 'w')
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime," :- ")
                file.write(note)
            except Exception as e:
                print("unable to write")

        elif "show note" in query:
            speak("Showing Notes")
            file = open("spidy.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif "to update spidy" in query:
            speak("After downloading file please replace this file with the downloaded one")
            url = '# url after uploading file'
            r = requests.get(url, stream=True)

            with open("Voice.py", "wb") as Pypdf:

                total_length = int(r.headers.get('content-length'))

                for ch in progress.bar(r.iter_content(chunk_size=2391975),
                                       expected_size=(total_length / 1024) + 1):
                    if ch:
                        Pypdf.write(ch)


        elif "spidy" in query:

            wishMe()
            speak("spidy is here for you at anytime")
            speak(assname)

        elif "climate" in query:

            api_key = "your_api_key_here"

            base_url = "http://api.openweathermap.org/data/2.5/weather?"

            speak("City name")
            print("City name:")
            city_name = takeCommand()

            complete_url = base_url + "appid=" + api_key + "&q=" + city_name

            response = requests.get(complete_url)

            if response.status_code == 200:
                x = response.json()
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]

                print("Temperature (in kelvin unit) = " + str(current_temperature))
                print("Atmospheric pressure (in hPa unit) = " + str(current_pressure))
                print("Humidity (in percentage) = " + str(current_humidity))
                print("Description = " + str(weather_description))
            else:
                speak("City Not Found")


        elif "send message" in query:
            try:
               account_sid ='ACbb8f83dcbe97ce48ae9740d694c356ad'
               auth_token = '19820e3250b109f2268b2b77853f80ec'

               client = Client(account_sid, auth_token)
               recipient_number =input("Enter the recipient's phone number (in E.164 format, e.g., +1234567890): ")
               message_content =input("Enter the message you want to send: ")

               message = client.messages.create(body=message_content,from_='9087352282',to=recipient_number)

               print("Message SID:", message.sid)
            except Exception as e:
                print("can't send message")

        elif "what is wikipedia" in query:
            webbrowser.open("wikipedia.com")

        elif "Good Morning" in query:
            speak("A warm" + query)
            speak("How are you sir")
            speak(assname)

        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about, may be you should give me some time")

        elif "how are you" in query:
            speak("I'm fine, glad you me that")

        elif "i love you" in query:
            speak("It's hard to understand")

        elif "what is" in query or "who is" in query:
            client = wolframalpha.Client("QW23R8-E5PAH2UQQ4")
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No results")