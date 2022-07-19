import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit
import smtplib
import speech_recognition as sr
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def wishme():
    Time=int(datetime.datetime.now().hour)
    if(Time>=0 and Time<12):
        speak("Good Morning Sir")
    elif(Time>=12 and Time<18):
        speak("Good Afternoon Sir")
    else:
        speak("Good Night Sir")
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def sendemail(to,content):
    pass
def Naukar():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold=1
        #r.energy_threshold=300
        audio=r.listen(source)
    try:
        print("Recognizing.....")
        query=r.recognize_google(audio,language='en-in')
        print(f" You said: {query}\n")
        speak(query)
    except Exception as e:
        print("Sorry! Couldn't hear you.Please try once again ")
        speak("Sorry! Couldn't hear you.Please try once again ")
        return "o"
    return query
    def sendemail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('anshika25shi@gmail.com', '12345')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()
if __name__=='__main__':
    people={
        'Anshika':"anshikas@iitk.ac.in",
        'Navneet':"snavneet@iitk.ac.in"
    }
    speak(wishme())
    speak("How may I help you ?")
    while True:
        query=Naukar().lower()
    #speak("Hey smarty!!.What can I do for you ?")
        if 'wikipedia' in query:
          query.replace("wikipedia","")
          results=wikipedia.summary(query,sentences=2)
          speak("According to wikipedia, ")
          print(results)
          speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
            speak("Opening Youtube...Please wait")
            print("Opening Youtube...Please wait")
        elif 'open google' in query:
            webbrowser.open('google.com')
            speak("Opening Google..Please wait")
            print("Opening Google..Please wait")
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
            speak("Opening Stackoverflow...Please wait")
            print("Opening Stackoverflow...Please wait")
        elif 'play ' in query:
            query=query.replace("play","")
            speak("Playing...")
            speak(query)
            pywhatkit.playonyt(query)
        elif 'time' in query:
            Time=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {Time}")
            print(f"The time is {Time}")

        elif 'open code' in query:
            pathc='C:\\Users\Anshika Singh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            speak("Opening VS Code")
            print("Opening VS Code")
            os.startfile(pathc)
        # elif 'open adobe illustrator' or 'open illustrator' in query:
        #     pathc="C:\\Program Files\\Adobe\\Adobe Illustrator 2020\\Support Files\\Contents\\Windows\\Illustrator.exe"
        #     speak("Opening Adobe Illustrator..")
        #     print("Opening Adobe Illustrator..")
        #     os.startfile(pathc)
        elif 'open mookit' in query:
            speak("Opening Mookit....")
            print("Opening Mookit....")
            webbrowser.open("hello.iitk.ac.in")
        elif 'open photoshop' in query:
            speak("Opening Photoshop")
            print("Opening Photoshop")
            os.startfile("C:\\Program Files\\Adobe\\Adobe Photoshop 2020\\Photoshop.exe")
        elif 'send email' in query:
            query=query.replace("send email to","")
            speak("What should I send?")
            print("What should I send?")
            try:
              content=Naukar()  
              to=people[query]
              sendemail(to,content)
              speak("Your email has been sent")
              print("Your email has been sent")
            except Exception as e:
              print(e)
              speak("Your email has not been sent")
              print("Your email has not been sent")

                



        
        
