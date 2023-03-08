import ctypes
import subprocess
from cmath import e
from click import confirm
import psutil
import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import smtplib
from pymsgbox import password
from secrets import senderemail, epwd, to
import pyautogui
import webbrowser as wb
from time import sleep
import wikipedia
import pywhatkit
import requests
from newsapi import NewsApiClient
import clipboard
import os

import pyjokes
import time as tt
import string
import random
import win32com.client as wincl
from nltk.tokenize import word_tokenize

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def getvoices(voice):
    voices = engine.getProperty('voices')
    print(voices[2].id)
    # if voice == 1:
    #     engine.setProperty('voice', voices[0].id)
    #     speak("Hello, This is Jarvis mode of Jeeniy")
    #
    # if voice == 2:
    #     engine.setProperty('voice', voices[2].id)
    #     speak("Hello, This is Friday mode of Jeeniy")


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

def greet():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("good morning Niyati!!")
    elif hour >= 12 and hour < 18:
        speak("good afternoon Niyati!!")
    elif hour >= 18 and hour < 24:
        speak("good evening Niyati!!")

def wishme():
    speak("welcome back Jeel!!")
    greet()
    speak("jeeniy at your service, please tell me how can i help you?")
#wishme()


# while True:
#     voice = int(input("Press 1 for male voice\nPress 2 for female voice"))
# #     speak(audio)
#     getvoices(voice)

def takeCommandCMD():
    query= input("please tell me how can i help you?\n")
    return query

def takeCommandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language ="en-IN")
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please")
        return "None"
    return query

# def sendEmail():
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.starttls()
#     server.login(senderemail, epwd)
#     server.sendmail(senderemail, to, 'Hello this is Niyati just to check email function using Jeeniy reply me back in wp.')
#
# sendEmail()

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login('20dit086@charusat.edu.in', 'nhp@2601')
    server.sendmail('20dit086@charusat.edu.in', to, content)
    server.close()

def sendwhatsappmsg(phone_no, message):
    Message = message
    wb.open('https://web.whatsapp.com/send?phone=' + phone_no + '&text=' + Message)
    sleep(10)
    pyautogui.press('enter')

def searchGoogle():
    speak("What should i search for you?")
    search = takeCommandMic()
    wb.open('https://www.google.com/search?q='+search)

def news():
    newsapi = NewsApiClient(api_key ='b99cefc40c4e4dd693b3993c19b6a9c8')
    speak('what news do you want')
    topic = takeCommandMic()
    data = newsapi.get_top_headlines(q=topic,
                                     language='en',
                                     page_size=5)

    newsdata = data['articles']
    for x, y in enumerate(newsdata):
        print(f'{x}{y["description"]}')
        speak((f'{x}{y["description"]}'))

    speak("these were the updates for now")

def text2speech():
        text = clipboard.paste()
        print(text)
        speak(text)

def covid():
        r = requests.get('https://coronavirus-19-api.herokuapp.com/all')
        data = r.json()
        covid_data = f'Confirmed cases : {data["cases"]}\n Deaths : {data["deaths"]} \n Recovered {data["recovered"]}'
        print(covid_data)
        speak(covid_data)

def screenshot():
    name_img = tt.time()
    name_img = f'C:\\Users\\niyat\\PycharmProjects\\JeeNiy(AI ASSISTANT)\\screenshots\\{name_img}.png'
    img = pyautogui.screenshot(name_img)
    img.show()

def password():
        s1 = string.ascii_uppercase
        s2 = string.ascii_lowercase
        s3 = string.digits
        s4 = string.punctuation

        passlen = 8
        s = []
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        s.extend(list(s4))

        random.shuffle(s)
        newpass = ("".me(s[0:passlen]))
        print(newpass)
        speak(newpass)

def flip():
    speak("okay sir, flipping a coin for you")
    coin = ['heads','tails']
    toss = []
    toss.extend(coin)
    random.shuffle(toss)
    toss = ("".join(toss[0]))
    print(("I flipped the coin and you got "+toss))
    speak("I flipped the coin and you got"+toss)

def roll():
    speak("okay sir, rolling a die for you")
    die = ['1','2','3','4','5','6']
    roll =[]
    roll.extend(die)
    random.shuffle(die)
    roll = ("".join(roll[0]))
    print(("I rolled a die and you got " +roll))
    speak("I rolled a die and you got" +roll)

def cpu():
    usage = str(psutil.cpu_percent())
    print('CPU is at' + usage)
    speak('CPU is at' +usage)
    battery = psutil.sensors_battery()
    # print("Battery is at" +battery)
    speak('Battery is at')
    speak(battery.percent)

if __name__ == "__main__":
    getvoices(2)
    #wishme()
    greet()
    speak("Hello my name is jeeniy")
    greet()
    while True:
        query = takeCommandMic().lower()
        print(query)
        if 'jeeniy' or 'genie' or 'jini' or 'ji' or 'ni' or 'jenie' or 'ne' in query:
            if 'time' in query:
                time()
            elif 'date' in query:
                date()

            elif 'send a mail' in query:
                try:
                    speak("What should I say?")
                    content = takeCommandMic()
                    speak("whom should i send")
                    to = input()
                    sendEmail(to, content)
                    speak("Email has been sent !")
                except Exception as e:
                    print(e)
                    speak("I am not able to send this email")

            elif 'email to niyati' in query:
                try:
                    speak("What should I say?")
                    content = takeCommandMic()
                    to = "niyatishah2601@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent !")
                except Exception as e:
                    print(e)
                    speak("I am not able to send this email")

            elif 'how are you' in query:
                speak("I am fine, Thank you")
                speak("How are you, Sir")

            elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')

            elif "where is" in query:
                query = query.replace("where is", "")
                location = query
                speak("User asked to Locate")
                speak(location)
                wb.open("https://www.google.co.in/maps/place/" + location + "")


            elif 'play music' in query or "play song" in query:
                speak("Here you go with music")
                # music_dir = "G:\\Song"
                music_dir = "C:\\Users\\niyat\\music"
                songs = os.listdir(music_dir)
                print(songs)
                random = os.startfile(os.path.join(music_dir, songs[1]))

            elif 'message' in query:
                user_name = {
                    'Niya': '+919924477991',
                    'Hp': '+919426920533',
                    'Riya Charusat': '+917016115532'
                }
                try:
                    speak("To whom you want to send the whatsapp message?")
                    name = takeCommandMic()
                    phone_no = user_name[name]
                    speak("What is the message?")
                    message = takeCommandMic()
                    sendwhatsappmsg(phone_no, message)
                    speak("Message has been sent")
                except Exception as e:
                    print(e)
                    speak("Unable to send the message")

            elif 'wikipedia' in query:
                speak("searching...")
                query = query.replace("wikipedia"," ")
                result = wikipedia.summary(query, sentences = 2)
                print(result)
                speak(result)

            elif 'search' in query:
                searchGoogle()

            elif 'youtube' in query:
                speak("What to search on Youtube?")
                topic = takeCommandMic()
                pywhatkit.playonyt(topic)

            elif 'weather' in query:
                speak('which place weather update do you want')
                city = takeCommandMic()
                url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=3c72af663c1061dfc4137aa1159763fb'
                res = requests.get(url)
                data = res.json()
                weather = data['weather'][0]['main']
                temp = data['main']['temp']
                desc = data['weather'][0]['description']
                temp = round((temp - 32) * 5 / 9)
                print(weather)
                print(temp)
                print(desc)
                speak(f'weather in {city} is like')
                speak('Temperature : {} degree celcius'.format(temp))
                speak('weather is {}'.format(desc))

            elif 'news' in query:
                news()

            elif "who made you" in query or "who created you" in query:
                speak("I have been created by two bestfriends Niyati and jeel.")


            elif 'open youtube' in query:
                speak("Here you go to Youtube\n")
                wb.open("youtube.com")

            elif 'open google' in query:
                speak("Here you go to Google\n")
                wb.open("google.com")

            elif 'open stackoverflow' in query:
                speak("Here you go to Stack Over flow.Happy coding")
                wb.open("stackoverflow.com")

            elif 'read' in query:
                text2speech()

            elif 'covid' in query:
                covid()

            elif 'open' in query:
                os.system('explorer C://{}'.format(query.replace('Open', '')))

            # elif 'pycharm code' in query:
            #     codepath = 'C:\\Users\\niyat\\PycharmProjects\\Code.exe'
            #     os.startfile(codepath)

            elif 'joke' in query:
                jokes = pyjokes.get_joke()
                print(jokes)
                speak(jokes)

            elif 'screenshot' in query:
                screenshot()

            elif 'remember' in query:
                speak("what should I remember")
                data = takeCommandMic()
                speak("you said me to remember that" + data)
                remember = open('data.txt', 'w')
                remember.write(data)
                remember.close()

            elif 'do you know anything' in query:
                remember = open('data.txt', 'r')
                speak("you told me to remember that" + remember.read())

            elif 'password' in query:
                password()

            elif 'flip' in query:
                flip()

            elif 'roll' in query:
                roll()

            elif 'cpu' in query:
                cpu()



            elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()

            elif "write a note" in query:
                speak("What should i write, sir")
                note = takeCommandMic()
                file = open('jarvis.txt', 'w')
                speak("Sir, Should i include date and time")
                snfm = takeCommandMic()
                if 'yes' in snfm or 'sure' in snfm:
                    strTime = datetime.datetime.now().strftime("% H:% M:% S")
                    file.write(strTime)
                    file.write(" :- ")
                    file.write(note)
                else:
                    file.write(note)

            elif "show note" in query:
                speak("Showing Notes")
                file = open("jarvis.txt", "r")
                print(file.read())
                speak(file.read(6))

            elif 'offline' in query:
                quit()