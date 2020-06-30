import pyttsx3
import datetime
import pyaudio
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes

engine=pyttsx3.init()
engine.say("Hi, I am Chitti, The robot")
engine.runAndWait()

def speak(audio,var):
    if var=="time":
        engine.say("The time is ")
    elif var=="date":
        engine.say("The date is ")
    engine.say(audio)
    engine.runAndWait()

def time():
    Time1=datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time1,"time")

def date():
    year=str(datetime.datetime.now().year)
    month=str(datetime.datetime.now().month)
    day=str(datetime.datetime.now().day)
    speak(day,"date")
    speak(month,"xx")
    speak(year,"xx")

def wishme():
    #str1=input("Enter your name :")
    str1="Srivatsa"
    speak("Welcome "+str1,"xx")
    hour=datetime.datetime.now().hour
    if hour>=16:
        speak("Good evening sir !","xx")
    elif hour>=12:
        speak("Good afternoon sir!","xx")
    else:
        speak("Good Morning Sir !","xx")
    time()
    #date

def takecomx():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1
        #audio=r.listen(source)
        audio=r.record(source,duration=4)
    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language='en-in')
        print(query)
        speak("You spoke : "+query,"xx")
    except Exception as e:
        print(e)
        speak("Say that again :","xx")
        return "None"
    return query

def takecom():
    str1 = str(input("Give your command sir !").lower())
    return str1


def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com', 587)
    #speak("Stage 1 done","xx")
    server.ehlo()
    #speak("Stage 2 done","xx")
    server.starttls()
    #speak("Stage 3 done","xx")
    server.login('srivatsakanukolanu@gmail.com','saiamma@1')
    server.sendmail('srivatsakanukolanu@gmail.com',to,content)
    server.close()

def searchinchrome(search1,type1):
    chromepath='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    if type1=='website':
        wb.get(chromepath).open_new_tab(search1 + '.com')
    else:
        search1=search1.replace(" ","+")
        #search1='https://www.google.com/'+search1
        wb.get(chromepath).open_new_tab(search1)

def playsongs():
    songs_dir='E:\\Audio Songs\\Ala Vaikuntapuramlo'
    songs=os.listdir(songs_dir)
    print(songs)
    speak("Sir, these songs are available. Which one you want to listen ?","xx")
    q=str(input("Enter song no :"))
    count=0
    for i in songs:
        if q in i:
            speak("Playing the song ...........","xx")
            print("Playing the song "+i+"..........")
            os.startfile(os.path.join(songs_dir,songs[count]))
        else:
            count+=1

def screenshot():
    img=pyautogui.screenshot()
    img.save("E:\\Python\\ss.png")

def cpu():
    usage=str(psutil.cpu_percent())
    speak('CPU is at'+usage,'xx')
    battery=psutil.sensors_battery()
    speak('battery is at','xx')
    speak(battery.percent,"xx")

def jokes():
    speak(pyjokes.get_joke(),"xx")

if __name__=="__main__":
    #wishme()
    speak("Sir, Give your command", "xx")
    #while 1:
        #takecomx()
    while True:
        str1=takecom().lower()
        if 'time' in str1:
            time()
        elif 'date' in str1:
            date()
        elif 'wikipedia' in str1:
            try:
                speak("searching....","xx")
                str1=str1.replace("wikipedia","")
                result=wikipedia.summary(str1,sentences=2)
                print(result)
                speak(result,"xx")
            except Exception as PageError:
                speak("Couldn't find the page sir. But I will show you the result on chrome","xx")
                searchinchrome(str1,'normal')
            except Exception as e:
                print(e)
                speak("Unknown Error","xx")
                continue

        elif 'send mail' in str1:
            try:
                speak("What message should I send","xx")
                content=takecom()
                to='srivatsakanukolanu@gmail.com'
                sendEmail(to,content)
                speak("Email sent","xx")
            except Exception as e:
                print(e)
                speak("unable to send","xx")
        elif 'search in chrome' in str1:
            speak("What should I search ?","xx")
            search=takecom().lower()
            if ' ' in search:
                searchinchrome(search,'data')
            else:
                searchinchrome(search,'website')

        elif 'play songs' in str1:
            playsongs()

        elif 'logout' in str1:
            os.system("shutdown -l")

        elif 'shutdown' in str1:
            os.system("shutdown /s /t 1")

        elif 'restart' in str1:
            os.system("shutdown /r /t 1")  

        elif 'remember that' in str1:
            speak("What should I remember ?","xx")
            data= takecom()
            speak("YOU said me to remember "+data,"xx")
            remember=open('data.txt','w')
            remember.write(data)
            remember.close()
        
        elif 'do you know that' in str1:
            remember=open('data.txt','r')
            x='you told me to remember that'+remember.read()
            speak(x,"xx")
        
        elif 'screenshot' in str1:
            screenshot()
            speak("Done !","xx")
        
        elif 'jokes' in str1:
            jokes()

        elif 'cpu' in str1:
            cpu()

        elif 'goodbye' or 'bye' in str1:
            speak("Thank you sir. Chitti at your service !","xx")
            break
        else:
            engine.say("Sorry sir ! Please come again ?")
            continue
        speak("Sir, what would you like to do now ?","xx")
