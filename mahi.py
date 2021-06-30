import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12 :
        speak("good afternoon")

    elif hour>=12 and hour<18:
        speak("good afternoon")

    else:
        speak("good evening")

    speak("i am maahi the assistant. please tell me how may i help you")

def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening........")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing......")
        query = r.recognize_google(audio, language='en-in')
        print(f'user said: {query}\n')

    except Exception as e:
        print("say that again please......")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('dhaktakataka@gmail.com', 'huihui1029') # I created a new gmail account for testing purpose and will never use it for any other purpose
    server.sendmail('pasayatanurag@gmail.com',to,content)
    server.close()

if __name__ == '__main__':
        wishMe()
        while True:
            query = takecommand().lower()

            if 'wikipedia' in query:
                speak('searching Wikipedia....')
                query = query.replace('wikipedia','')
                results = wikipedia.summary(query, sentences=2)
                speak('Accourding to wikipedia')
                print(results)
                speak(results)

            elif 'open youtube' in query:
                webbrowser.open("youtube.com")

            elif "open google" in query:
                webbrowser.open("google.com")

            elif "open instagram" in query:
                webbrowser.open("instagram.com/direct/inbox")

            elif 'play music' in query:
                music_dir = 'F:\\songsssss\\ayushzzz'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"the time is {strTime}")

            elif 'pycharm' in query:
                pycharm = "D:\\pycharm\\PyCharm Community Edition 2020.3.5\\bin\\pycharm64"
                os.startfile(pycharm)

            elif 'email to anurag' in query:
                try:
                    speak("what should i say?")
                    content = takecommand()
                    to = "pasayatanurag@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent")
                except Exception as e:
                    print(e)
                    speak("uhh ohh, i am sorry sir but i am unable to send the email")
