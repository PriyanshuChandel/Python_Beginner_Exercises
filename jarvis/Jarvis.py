UserFile = open('configuration.csv', 'r').readlines()
EmailFile = open('contacts.csv', 'r').readlines()
UserDatabase = {}
for user_and_email in EmailFile:
    UserDatabase[user_and_email.split(',')[0].lower().strip()] = user_and_email.split(',')[1].strip()

import datetime  # To check current time
from time import sleep  # To manage sleep
from pyttsx3 import init  # To use sapi and its properties to get list of installed voices
from speech_recognition import Recognizer, Microphone  # To use voice engine to recognize voice
from webbrowser import open  # To access browser
from os import listdir, startfile, path  # To use system properties
from random import randint  # To generate random number
from subprocess import Popen, PIPE, STDOUT  # To run window commands
from smtplib import SMTP  # To access SMTP to send emails
from email.mime.text import MIMEText  # To format so can use subject, etc

engine = init('sapi5')
voices = engine.getProperty('voices')
# print(voices)  # It will show you all the available voices
# print(voices[2].id) # it will show you the id of voice like david, jeera etc
engine.setProperty('voice', voices[2].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme(name):
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning")
    elif 12 <= hour < 18:
        speak("Good Afternoon")
    else:
        speak('Good Evening')
    speak(f"Hello {name} I'm your personal assistant, how may I assist you")


def takeCommand():
    """It takes microphone input from user and return string output"""
    r = Recognizer()
    with Microphone() as source:
        print('Listening...')
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1  # It is required to modify so user can take 1 seconds between two words he speaks
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-In')
        print(f'user said: {query}\n')

    except Exception as e:
        print(e)
        print('\nSay that again please...')
        return "None"
    return query


def launch_application(appname):
    command1 = Popen(['powershell.exe', 'get-StartApps', '| Format-List'], shell=True, stdout=PIPE, stderr=STDOUT,
                     close_fds=True)
    output_command1 = (command1.stdout.read()).split(b'\r\n\r\n')
    application_dict = {}
    for application in output_command1:
        if application != b'':
            list1 = application.split(b'Name  : ')[1].split(b'\r\nAppID : ')
            key = list1[0]
            if b' \r\n        ' in list1[1]:
                val = list1[1].replace(b' \r\n        ', b'')
            else:
                val = list1[1]
            application_dict[key.strip().lower()] = val
    application_id = application_dict.get(appname.encode())
    if application_id.startswith(b'{'):
        new_application_id = application_id.rsplit(b'\\', 1)[1]
        command2 = Popen(['start', f'{new_application_id.decode()}'], shell=True, stdin=PIPE, stdout=PIPE,
                         stderr=STDOUT, close_fds=True)
    else:
        command3 = Popen(['powershell.exe', f'explorer shell:appsfolder\\{application_id.decode()}'], shell=True,
                         stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)


def sendmail(to, content):
    email = UserFile[1].split(',')[1].strip()
    email = UserFile[2].split(',')[1].strip()
    server = SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(user=email, password=password)
    server.sendmail(email, to, content.as_string())
    server.close()


if __name__ == "__main__":
    name = UserFile[0].split(',')[1].strip()
    wishme(name)
    print("1.Ask 'hey open xxxxx' to browse on internet.i.e 'hey open gmail'.\n2.Ask 'play audio' to play audio "
          "songs.\n3.Ask 'what is the time' for current time.\n4.Ask 'start xxxx' to run any application.\n5.Ask 'send "
          "email to xxxx' to send email to someone.\n6.Ask 'quite' to exit the program\n")
    while True:
        query = takeCommand().lower()
        # logics for execution based on query
        if 'hey' in query:
            open(f"{query.split(' ', 2)[2]}.com")
        elif 'play audio' in query:
            music_dir = UserFile[3].split(',')[1].strip()
            speak('playing audio')
            songs = [song for song in listdir(music_dir) if song.endswith('.mp3')]
            startfile(path.join(music_dir, songs[randint(0, len(songs) - 1)]))
        elif 'the time' in query:
            strtime = datetime.datetime.now()
            speak(f'Sir, The time is {strtime.hour} hours {strtime.minute} minutes and {strtime.second} seconds')
        elif 'start' in query:
            appname = query.split(' ', 1)[1].lower()
            speak(f'launching {appname}')
            try:
                launch_application(appname)
                sleep(8)
                speak(f'{appname} launched')
            except Exception as e:
                print(e)
                speak(f'launching of {appname} failed because of the error')
        elif 'send email' in query:
            recipient_name = query.split(' ', )[-1].lower()
            try:
                recipient_email = UserDatabase.get(query.split(' ', )[-1].lower())
                if recipient_email is not None:
                    speak(f'What should I mention in body')
                    content = MIMEText(takeCommand())
                    speak(f'What should I mention in the subject')
                    content['Subject'] = takeCommand()
                    sendmail(recipient_email, content)
                    speak(f'email has been sent to {recipient_name} successfully')
                else:
                    speak(f'f{recipient_name} not found in contact list')
            except Exception as e:
                print(e)
                print(f'Email cannot sent to {recipient_name} due to above reason')
        elif 'quit' in query:
            speak('Bye, see you again')
            exit()