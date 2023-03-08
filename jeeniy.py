from cmath import e
from click import confirm
import pyttsx3
import datetime
import speech_recognition as sr
import smtplib
import pyautogui
import webbrowser as wb
from time import sleep
from secrets import senderemail, epwd, to
import wikipedia
import pywhatkit
import requests
from newsapi import NewsApiClient
import clipboard
import os
import pyjokes
import ctypes
import subprocess
import time as tt
import string
import random
import psutil
from nltk.tokenize import word_tokenize
from tkinter import *
#import tkvideo
#import imageio
from PIL import Image, ImageTk
from webbrowser import open
from sys import argv
from pyperclip import paste

# sr.Microphone.list_microphone_names()


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def getvoices(voice):
    voice = engine.setProperty('voice', voices[2].id)
    print(voices[2].id)
    # if(voice==0):
    #   engine.setProperty('voice', voices[0].id)
    # if(voice==1):
    #    engine.setProperty('voice', voices[1].id)
    # voice = 1
    getvoices(voice)


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is:")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("Today's date is:")
    speak(day)
    speak(month)
    speak(year)


""" def shutdown():
    return os.system("shutdown /s /t 1")

def restart():
    return os.system("shutdown /r /t 1")

def logout():
    return os.system("shutdown -l")


# tkinter object
master = Tk()

# background set to grey
master.configure(bg='light grey')

# creating a button using the widget
# Buttons that will call the submit function
Button(master, text="Shutdown", command=shutdown).grid(row=0)
Button(master, text="Restart", command=restart).grid(row=1)
Button(master, text="Log out", command=logout).grid(row=2)

mainloop() """


def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good morning Jeel, Jeeniy at your service")
    elif hour > 12 and hour < 18:
        speak("Good afternoon Jeel, Jeeniy at your service")
    elif hour > 18 and hour < 24:
        speak("Good evening Jeel, Jeeniy at your service")
    else:
        speak("Good night Jeel, Jeeniy at your service")


def wishme():
    # speak("Wishing you a nice day!")
    # time()
    # date()
    greeting()
    speak("Jeeniy at your service, please tell me how can I help you?")
    # speak("Heyy Jeelu, how're you doing?")


while True:

    # voice = int(input("Press 1 for male and 2 for female respectively\n"))
    # speak(audio)
    # getvoices(voice)
    # wishme()

    def takeCommandCMD():
        query = input("Please tell me how can I help you?")
        return query


    def takeCommandMic():
        r = sr.Recognizer()
        my_mic = sr.Microphone(device_index=1)
        # with sr.Microphone() as source:
        with my_mic as source:
            # print(sr.Microphone.list_microphone_names())
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-IN")
            print(query)
        except Exception as e:
            print(e)
            speak("Say that again please!")
            return "None"
        return query


    # def sendEmail():
    #     server = smtplib.SMTP('smtp.gmail.com', 587)
    #     server.starttls()
    #     server.login(senderemail, epwd)
    #     server.sendmail(senderemail, to, "Hello, this is a test email by jeeniy")
    #     server.close()

    # sendEmail()

    def sendwhatsappmsg(phone_no, message):
        Message = message
        wb.open('https://web.whatsapp.com/send?phone=' + phone_no + '&text=' + Message)
        sleep(10)
        pyautogui.press('enter')


    def searchgoogle():
        speak('what should I search for?')
        search = takeCommandMic()
        wb.open('https://www.google.com/search?q=' + search)


    def news():
        newsapi = NewsApiClient(api_key='41b4a4269a2145b1950f51550906c136')
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
        name_img = f'C:\\Users\\jeelj\\Downloads\\AI Assistant\\screenshots\\{name_img}.png'
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
        newpass = ("".john(s[0:passlen]))
        print(newpass)
        speak(newpass)


    def flip():
        speak("okay, flipping a coin")
        coin = ['heads', 'tails']
        toss = []
        toss.extend(coin)
        random.shuffle(toss)
        toss = ("".join(toss[0]))
        print("I flipped the coin and you have got " + toss)
        speak("I flipped the coin and you have got " + toss)


    def roll():
        speak("okay, rolling a die for you")
        die = ['1', '2', '3', '4', '5', '6']
        roll = []
        roll.extend(die)
        random.shuffle(roll)
        roll = ("".join(roll[0]))
        print("I rolled a die and you have got " + roll)
        speak("I rolled a die and you have got " + roll)


    def cpu():
        usage = str(psutil.cpu_percent())
        speak("cpu is at" + usage)
        battery = psutil.sensors_battery()
        speak("battery is at" + battery.percent)


    """ video_name = "C:\\Users\\jeelj\\Downloads\\UI.mp4" #This is your video file path
    video = imageio.get_reader(video_name)

    def stream(label):

        for image in video.iter_data():
            frame_image = ImageTk.PhotoImage(Image.fromarray(image))
            label.config(image=frame_image)
            label.image = frame_image

    if __name__ == "__main__":
        root = tk.Tk()
        my_label = tk.Label(root)
        my_label.pack()
        thread = threading.Thread(target=stream, args=(my_label,))
        thread.daemon = 1
        thread.start()
        root.mainloop() """

    """ app = Tk()
    app.title('Video Player')

    Fcanvas = Canvas(bg="black", height=1000, width=1500)


    def snd1():
        os.system("C:\\Users\\jeelj\\Downloads\\UI.mp4")

    var = IntVar()

    rb1 = Radiobutton(app, text= "Play Video", variable = var, value=1, command=snd1)
    rb1.pack(anchor = W)
    Fcanvas.pack()
    app.mainloop()  """

    greeting()

    if __name__ == "__main__":
        # getvoices(1)
        # wishme()
        # wakeword = 'jeeniy' or 'genie' or 'jini' or 'ji' or 'ni'or 'jenie' or 'ne'
        while True:
            query = takeCommandMic().lower()
            # query = word_tokenize(query)
            print(query)
            if 'jeeniy' or 'genie' or 'jini' or 'ji' or 'ni' or 'jenie' or 'ne' in query:
                if 'time' in query:
                    time()
                elif 'date' in query:
                    date()
                    # elif 'my' in query:
                    # my()

                elif 'message' in query:
                    user_name = {
                        'John': '+919664578707',
                        'Neha': '+919913157226',
                        'Papa': '919898442515',
                        'Alisha': '+919104202210'
                    }
                    try:
                        speak("To whome you want to send the whatsapp message?")
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
                    speak('searching on wikipedia')
                    query = query.replace('wikipedia', '')
                    result = wikipedia.summary(query, sentences=2)
                    print(result)
                    speak(result)

                elif 'search' in query:
                    searchgoogle()

                elif 'youtube' in query:
                    speak('what should I search for on youtube?')
                    topic = takeCommandMic()
                    pywhatkit.playonyt(topic)

                elif 'weather' in query:
                    speak('which place weather update do you want')
                    city = takeCommandMic()
                    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=7caa16eaa3ac76b848610703251ee47b'
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

                elif 'how are you' in query:
                    speak("I am fine, Thank you")
                    speak("How are you?")

                elif 'shutdown system' in query:
                    speak("Hold On a Sec ! Your system is on its way to shut down")
                    shutdown()

                elif 'play music' in query or "play song" in query:
                    speak("Here you go with music")
                    # music_dir = "G:\\Song"
                    music_dir = "C:\\Users\\niyat\Music\\awakening-instrumental-1165.mp3"
                    songs = os.listdir(music_dir)
                    print(songs)
                    random = os.startfile(os.path.join(music_dir, songs[1]))

                elif "who made you" in query or "who created you" in query:
                    speak("I have been created by two bestfriends Niyati and jeel.")

                elif 'lock window' in query:
                    speak("locking the device")
                    ctypes.windll.user32.LockWorkStation()

                elif "write a note" in query:
                    speak("What should i write, sir")
                    note = takeCommandMic()
                    file = open('jarvis.txt', 'w')
                    speak("Should i include date and time")
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

                elif 'read' in query:
                    text2speech()

                elif 'covid' in query:
                    covid()

                elif 'open' in query:
                    os.system('explorer C://{}'.format(query.replace('Open', '')))

                elif 'open code' in query:
                    codepath = 'D:\\Program Files\\Microsoft VS Code\\Code.exe'
                    os.startfile(codepath)

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

                elif "where is" in query:
                    query = query.replace("where is", "")
                    location = query
                    speak("User asked to Locate")
                    speak(location)
                    wb.open("https://www.google.co.in/maps/place/" + location + "")
                    """ if len(argv)>1:
                        address = " ".join(argv[1:])
                    else:
                        address = paste()
                        open("http://www.google.com/maps/place/"+address) """

                elif 'offline' in query:
                    quit()
