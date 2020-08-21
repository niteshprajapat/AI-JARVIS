import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes

engine=pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def time():
    Time=datetime.datetime.now().strftime('%I:%M:%S')
    speak(Time)
    
def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak("current date is ")
    speak(date)
    speak(month)
    speak(year)
    
def wishme():
    speak("welcome back Sir!!")
    
    hour=datetime.datetime.now().hour
    
    if hour >=6 and hour <12:
        speak("Good Morning !!")
    elif hour >=12 and hour <18 :
        speak("Good Afternoon !!")
    elif hour >=18 and hour <=24 :
        speak("Good Evening !!")
    else:
        speak("Good Night !!")
        
    speak("JARVIS at your service! . How can I help you ?? ")

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold=1
        audio=r.listen(source)
    
    try:
        print("Recognising....")
        query=r.recognize_google(audio,"en=US")
        print(query)
        
    except Exception as e:
        print(e)
        speak("say that again please....")
        
        return "None"
    
    return query


def sendmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('enter your email address','enter your password')
    server.sendmail('',to,content)
    server.close()
    

def screenshot():
    img=pyautogui.screenshot()
    img.save("E:\screenshots data\ss.png")
    
    
def cpu():
    usage=str(psutil.cpu_percent())
    speak("CPU is at "+usage)
    
    battery=psutil.sensors_battery
    speak("Battery is at ")
    speak(battery.percent)

    
def jokes():
    speak(pyjokes.get_joke())
    

if  __name__ == "__main__" :
    
    wishme()
    
    while True:
        query=takecommand().lower()
        print(query)
        
        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            quit()
        elif "wikipedia" in query:
            speak("searching........")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            speak(result)
        elif "send email" in query:
            try:
                speak("what should I say !!")
                content=takecommand()
                to="enter recipient email address"
                sendmail(to,content)
            except Exception as e:
                speak(e)
                speak("Unable to sent the message !!")
        elif "search in chrome" in query:
            speak("What should I search ??")
            chromepath="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"
            search = takecommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")
            
        #elif "logout" in query:
            os.system("shutdown - l")
            
        #elif "shutdown" in query:
            os.system("shutdown /s /t 1")
            
        #elif "restart" in query:
            os.system("shutdown /r /t 1")
            
        elif "play songs" in query:
            song_dir="enter path of music album"
            songs=os.listdir(song_dir)
            os.startfile(os.path.join(song_dir,songs[0]))
            
        elif "remember that" in query:
            speak("what should I remember ??")
            data=takecommand()
            speak("you said me to remember",data)
            remember=open("data.txt","w")
            remember.write(data)
            remember.close()
            
        elif "do you know anything" in query:
            remember=open("data.txt","r")
            speak("you said me to remember that"+remember.read())
            
        elif "screenshot" in query:
            screenshot()
            speak("Done!!")
        
        elif "cpu" in query:
            cpu()
            
        elif "joke" in query:
            jokes()
