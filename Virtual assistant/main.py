import speech_recognition as sr  # recognise speech
import playsound  # to play an audio files
from gtts import gTTS  # google text to speech
import random
from time import ctime  # get time details
import webbrowser  # open browser
import ssl
import certifi
import time
import os  # to remove created audio files
from PIL import Image
import subprocess
import pyautogui  # screenshot
import pyttsx3
import bs4 as bs
import urllib.request
import datetime
import cv2
from cv2 import cv2
from requests import get
from bs4 import BeautifulSoup
import pywhatkit as kit
import pyjokes
import requests
from pywikihow import search_wikihow
import psutil
import speedtest
import winsound
import datefinder
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from GUI import Ui_GUI
import sys
class person:
    name = ''

    def setName(self, name):
        self.name = name


class asis:
    name = ''

    def setName(self, name):
        self.name = name

# listen for audio and convert it to text:
def record_audio(ask=""):
    with sr.Microphone() as source:  # microphone as source
        if ask:
            engine_speak(ask)
        audio = r.listen(source, 5, 5)  # listen for the audio via source
        print("Done Listening")
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio,language="en-in")  # convert audio to text
        except sr.UnknownValueError:  # error: recognizer does not understand
            engine_speak('I did not get that')
        except sr.RequestError:
            engine_speak('Sorry, the service is down')  # error: recognizer is not connected
        print(">>", voice_data.lower())  # print what user said
        return voice_data.lower()
def record_audio1(ask=""):
    with sr.Microphone() as source:  # microphone as source
        if ask:
            engine_speak(ask)
        audio = r.listen(source, 5, 5)  # listen for the audio via source
        print("Done Listening")
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio,language="en-in")  # convert audio to text
        except sr.UnknownValueError:  # error: recognizer does not understand
            print("I did not het that")
        except sr.RequestError:
            print('Sorry, the service is down')  # error: recognizer is not connected
        print(">>", voice_data.lower())  # print what user said
        return voice_data.lower()

def there_exists(terms,voice_data):
    for term in terms:
        if term in voice_data:
            return True

def alarm(text):
    dtime = datefinder.find_dates(text)
    for ti in dtime:
        print(ti)
    stringA = str(ti)
    timeA = stringA[11:]
    hourA = timeA[:-6]
    hourA = int(hourA)
    minA  = timeA[3:-3]
    minA = int(minA)
    while True:
        if hourA == datetime.datetime.now().hour:
            if minA == datetime.datetime.now().minute:
                engine_speak("Please wake up sir")
                print("alarm is running")
                winsound.PlaySound("abc",winsound.SND_ALIAS)
            elif minA>datetime.datetime.now().minute:
                break

#def engine_speak(text):
#    text = str(text)
#    engine.say(text)
#    engine.runAndWait()


r = sr.Recognizer()  # initialise a recogniser





# get string and make a audio file to be played
def engine_speak(audio_string):
    audio_string = str(audio_string)
    tts = gTTS(text=audio_string, lang='en')  # text to speech(voice)
    r = random.randint(1, 20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file)  # save as mp3
    playsound.playsound(audio_file)  # play the audio file
    print(asis_obj.name + ":", audio_string)  # print what app said
    os.remove(audio_file)  # remove audio file
#Function for wishing you
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        engine_speak("good morning ")
    elif hour>12 and hour<18:
        engine_speak("good afternoon")
    else:
        engine_speak("good evening")
# function for fetching news
#def news():

def respond(voice_data):
    # 1: greeting
    if there_exists(['hey', 'hi', 'hello'],voice_data):
        greetings = ["hey, how can I help you" + person_obj.name, "hey, what's up?" + person_obj.name,
                     "I'm listening" + person_obj.name, "how can I help you?" + person_obj.name,
                     "hello" + person_obj.name]
        greet = greetings[random.randint(0, len(greetings) - 1)]
        engine_speak(greet)

   # 2: name
    if there_exists(["what is your name", "what's your name", "tell me your name"],voice_data):
        if person_obj.name:
            engine_speak("whats with my name ")
        else:
            engine_speak("i dont know my name . what's your name?")

    if there_exists(["my name is"],voice_data):
        person_name = voice_data.split("is")[-1].strip()
        engine_speak("okay, i will remember that " + person_name)
        person_obj.setName(person_name)  # remember name in person object

    if there_exists(["your name should be"],voice_data):
        asis_name = voice_data.split("be")[-1].strip()
        engine_speak("okay, i will remember that my name is " + asis_name)
        asis_obj.setName(asis_name)  # remember name in asis object

    # 3: greeting
    if there_exists(["how are you", "how are you doing"],voice_data):
        engine_speak("I'm very well, thanks for asking " + person_obj.name)

    # 4: time
    if there_exists(["what's the time", "tell me the time", "what time is it"],voice_data):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = hours + " hours and " + minutes + "minutes"
        engine_speak(time)

    # 5: search google
    if there_exists(["search for"],voice_data) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for" + search_term + "on google")

    # 6: search youtube
    if there_exists(["youtube"],voice_data):
        search_term = voice_data.split("for")[-1]
        url = "https://www.youtube.com/results?search_query=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term + "on youtube")
        choice = record_audio("Do you want to play a video of my choice regarding this term")
        print(choice)
        if  there_exists(["ok"],choice):
            kit.playonyt(search_term)
        else:
            engine_speak("Okay as you wish")

    # 7: get stock price
    if there_exists(["stock price of"],voice_data):
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term + " on google")

    # search for music
    if there_exists(["play music"],voice_data):
        search_term = voice_data.split("for")[-1]
        url = "https://open.spotify.com/search/" + search_term
        webbrowser.get().open(url)
        engine_speak("You are listening to" + search_term + "enjoy sir")
    # search for amazon.com
    if there_exists(["amazon.com"],voice_data):
        search_term = voice_data.split("for")[-1]
        url = "https://www.amazon.in" + search_term
        webbrowser.get().open(url)
        engine_speak("here is what i found for" + search_term + "on amazon.com")

    # make a note
    if there_exists(["make a note"],voice_data):
        search_term = voice_data.split("for")[-1]
        url = "https://keep.google.com/#home"
        webbrowser.get().open(url)
        engine_speak("Here you can make notes")

    # open instagram
    if there_exists(["open instagram", "want to have some fun time"],voice_data):
        search_term = voice_data.split("for")[-1]
        url = "https://www.instagram.com/"
        webbrowser.get().open(url)
        engine_speak("opening instagram")

    # open twitter
    if there_exists(["open twitter"],voice_data):
        search_term = voice_data.split("for")[-1]
        url = "https://twitter.com/"
        webbrowser.get().open(url)
        engine_speak("opening twitter")

    # 8 time table
    if there_exists(["show my time table"],voice_data):
        im = Image.open(r"D:\WhatsApp Image 2019-12-26 at 10.51.10 AM.jpeg")
        im.show()

    # 9 weather
    if there_exists(["weather", "tell me the weather report", "whats the condition outside"],voice_data):
        search_term = voice_data.split("for")[-1]
        url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temp = data.find("div",class_="BNeawe").text
        engine_speak(f" The cureent weather is {temp}")

    # open gmail
    if there_exists(["open my mail", "gmail", "check my email"],voice_data):
        search_term = voice_data.split("for")[-1]
        url = "https://mail.google.com/mail/u/0/#inbox"
        webbrowser.get().open(url)
        engine_speak("here you can check your gmail")

    # 10 stone paper scisorrs

    if there_exists(["game"],voice_data):
        voice_data = record_audio("choose among rock paper or scissor")
        moves = ["rock", "paper", "scissor"]

        cmove = random.choice(moves)
        pmove = voice_data

        engine_speak("The computer chose " + cmove)
        engine_speak("You chose " + pmove)
        # engine_speak("hi")
        if pmove == cmove:
            engine_speak("the match is draw")
        elif pmove == "rock" and cmove == "scissor":
            engine_speak("Player wins")
        elif pmove == "rock" and cmove == "paper":
            engine_speak("Computer wins")
        elif pmove == "paper" and cmove == "rock":
            engine_speak("Player wins")
        elif pmove == "paper" and cmove == "scissor":
            engine_speak("Computer wins")
        elif pmove == "scissor" and cmove == "paper":
            engine_speak("Player wins")
        elif pmove == "scissor" and cmove == "rock":
            engine_speak("Computer wins")

    # 11 toss a coin
    if there_exists(["toss", "flip", "coin"],voice_data):
        moves = ["head", "tails"]
        cmove = random.choice(moves)
        engine_speak("The computer chose " + cmove)

    # 12 calc
    if there_exists(["plus", "minus", "multiply", "divide", "power", "+", "-", "*", "/"],voice_data):
        opr = voice_data.split()[1]

        if opr == '+':
            engine_speak(int(voice_data.split()[0]) + int(voice_data.split()[2]))
        elif opr == '-':
            engine_speak(int(voice_data.split()[0]) - int(voice_data.split()[2]))
        elif opr == 'multiply':
            engine_speak(int(voice_data.split()[0]) * int(voice_data.split()[2]))
        elif opr == 'divide':
            engine_speak(int(voice_data.split()[0]) / int(voice_data.split()[2]))
        elif opr == 'power':
            engine_speak(int(voice_data.split()[0]) ** int(voice_data.split()[2]))
        else:
            engine_speak("Wrong Operator")

    # 13 screenshot
    if there_exists(["capture", "my screen", "screenshot"],voice_data):
        name = record_audio('What will be the name of the screenshot file')
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save('C:/Users/Admin/Pictures/'+name+'.png')
        engine_speak('The task is done')

    # 14 to search wikipedia for definition
    if there_exists(["definition of"],voice_data):
        definition = record_audio("what do you need the definition of")
        url = urllib.request.urlopen('https://en.wikipedia.org/wiki/' + definition)
        soup = bs.BeautifulSoup(url, 'lxml')
        definitions = []
        for paragraph in soup.find_all('p'):
            definitions.append(str(paragraph.text))
        if definitions:
            if definitions[0]:
                engine_speak('im sorry i could not find that definition, please try a web search')
            elif definitions[1]:
                engine_speak('here is what i found ' + definitions[1])
            else:
                engine_speak('Here is what i found ' + definitions[2])
        else:
            engine_speak("im sorry i could not find the definition for " + definition)

    #14 NOtepad
    if there_exists(["open notepad","notepad"],voice_data):
        npath = "C:\\Windows\\system32\\notepad.exe"
        os.startfile(npath)
        engine_speak("there you go notepad is open")
    #15 command prompt
    if there_exists(["command prompt","open command prompt","open cmd","cmd"],voice_data):
        os.system("start cmd")
        engine_speak("it is open")
    #16 opening camera
    if there_exists(["open the camera","open the webcam","camera","wencam","open camera","open webcam"],voice_data):
        cam = cv2.VideoCapture(0)
        while True:
            ret, img= cam.read()
            cv2.imshow("webcam",img)
            k = cv2.waitKey(50)
            if k==27:
                break;
        cam.release()
        cv2.destroyAllWindows()
    #17 for geting the io address
    if there_exists(["ip address","ip"],voice_data):
        ip = get("https://api.ipify.org").text
        engine_speak(f"your IP address is {ip}")

    #18 Sending whats app messages
    if there_exists(["send whatsapp message"],voice_data):
        num = record_audio("whom do you want to send")
        who = num
        what = record_audio("what do you want to send")
        ms = what
        kit.sendwhatmsg("+919819108402","this is a test message",2,25)


    #19 to tell a joke
    if there_exists(["joke","funny"],voice_data):
        joke  = pyjokes.get_joke()
        engine_speak(joke)

    #20 shutdown and restart the laptop
    if there_exists(["shutdown","shutdown the pc","shutdown the system"],voice_data):
        os.system("shutdown /s /t s")
    if there_exists(["restart", "restart the pc", "restart the system"],voice_data):
        os.system("shutdown /r /t s")
    #21 for sweitching windows
    if there_exists(["switch","switch the windows","change the windows"],voice_data):
        pyautogui.keyDown('alt')
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.keyUp('alt')

    #22 news
    if there_exists(['tell me the news','what is the news today','what are the headlines today'],voice_data):
        engine_speak('Please wait while i get the news')
        #news()
    #23 for getting the location
    if there_exists(['where are we','where am i '],voice_data):
        engine_speak('wait let me check')
        try:
            ipAdd = requests.get('https://api.ipify.org').text
            print(ipAdd)
            url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
            geo_requests = requests.get(url)
            geo_data = geo_requests.json()
            city = geo_data['city']
            country = geo_data['country']
            engine_speak(f"I think we are in {city} city of {country}")
        except Exception as e:
            engine_speak("Sorry i am unable to find the location")

    #24 For instagram checks
    if there_exists(['instagram','open instagram'],voice_data):
        engine_speak("enter the user name:")
        name = input("Enter username here:")
        webbrowser.open(f"www.instagram.com/{name}")

    #25 for reading
    #26 to hide a file using voice
    if there_exists(['hide all files','hide files'],voice_data):
        os.system("attrib +h /s /d")
        engine_speak("Sir all the files in this folder are hidden")
    #27 to make file visible
    if there_exists(['make files visible','visible'],voice_data):
        os.system("attrib -h /s /d")
        engine_speak("Sir all files have been made visible")
    #28 to how to mod
    if there_exists(["activate how to mod"],voice_data):
        engine_speak("how to do mode is activated")
        while True:
          how = record_audio("what do you want to search")
          try:
                if "exit" in how or "close" in how:
                    engine_speak("Okay sir,how to mode is closed")
                    break
                else:
                    max_result = 1
                    how_to = search_wikihow(how, max_result)
                    assert len(how_to) == 1
                    how_to[0].print()
                    engine_speak(how_to[0].summary)
          except Exception as e:
                engine_speak("Sorry sir,I am not able to find this")
    #29 to check the battery
    if there_exists(["how much battery is remaining","battery percentage"],voice_data):
        battery  = psutil.sensors_battery()
        percentage = battery.percent
        engine_speak(f"Sir our system have {percentage} percent present battery")
        if percentage>=75:
            engine_speak("We have adequate amount of enery to keep going")
        elif percentage>=40 and percentage<75:
            engine_speak("I think it would be suitable to find a charging point")
        elif percentage>=15 and percentage< 40:
            engine_speak("We dont have enough power plaese charge the system")
        elif percentage<15:
            engine_speak("The system is about to die plaese charge it")
    #30 to test internet speed
    if there_exists(['test internet speed','bandwith speed'],voice_data):
        st = speedtest.Speedtest()
        ul = st.download()
        dl = st.upload()
        engine_speak(f"Sir we have {ul} per bit downloading speed and {dl} per bit uploading speed")
    #31 to control volume
    if there_exists(['volume up','raise volume','increase volume'],voice_data):
        pyautogui.press("volumeup")
    if there_exists(['volume down','lower the volume','decrease volume'],voice_data):
        pyautogui.press("volumedown")
    if there_exists(['mute','silence'],voice_data):
        pyautogui.press("volumenute")

    #32 to set an alaram
    if there_exists(["alarm","ping"],voice_data):
       engine_speak("Sir please enter the time you would like to set the alarm ")
       al = input("Enter time here:")
       alarm(al)


    #33 to exit
    #if there_exists(['sleep','exit','Take a nap'],voice_data):
     #   engine_speak("We could continue more but anyways byee,have a nice day")
      #  exit()
    #34 Introduce
    if there_exists(['who are you','what are you'],voice_data):
        engine_speak("Hi ,i am Trinity your Desktop assistant i can search and do task for you all you have do is ask")
    #35 Features
    if there_exists(['features'],voice_data):
        engine_speak("I have more than 25 features within me and is currently under development for furthur improvement")




time.sleep(1)

person_obj = person()
asis_obj = asis()
asis_obj.name = 'Kim'
engine = pyttsx3.init()

 

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    def run(self):
        self.TASKECEcution()


    def TASKECEcution(self):
        while(1):
          self.voice_data = record_audio1("")
          if there_exists(["wake up","trinity"],self.voice_data):
            wish()
            while (1):
                voice_data = record_audio("Listening")# get the voice # input
                if there_exists(["sleep","rest"],voice_data):
                    engine_speak("Okay ,but feel free to call me when you need ")
                    break
                else:
                    print("Done")
                    print("Q:", voice_data)
                    respond(voice_data)  # respond
startexecution = MainThread() 
class MAIN(QMainWindow):
    def  __init__(self):
      super().__init__()
      self.ui = Ui_GUI()
      self.ui.setupUi(self)
      self.ui.pushButton.clicked.connect(self.startTask)
      self.ui.pushButton_2.clicked.connect(self.close)
    def startTask(self):
        self.ui.movie = QtGui.QMovie("C:/projects(python)/Virtual assistant/image/82ab4698e35dbb487566f3cec0503f04.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startexecution.start()
    def  showTime(self):
        current_time = QTime.currentTime()
        now = QDate.currentDate()
        label_time = current_time.toString("hh:mm:ss")
        label_date = now.toString(Qt.ISODate)  
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)
app = QApplication(sys.argv)
trinity = MAIN()
trinity.show()
exit(app.exec_())