# Healthy programmer alarm reminder.
# water.mp3, eye.mp3 and physical.mp3 copied in project folder.
# tut50_logfile created in project folder.
"""
play water alarm after every 27 min and take input from user to stop.
play eye alarm after every 30 min and take input from user to stop.
play physucal alarm after every 45 min and take input from user to stop.
after user input log the history in a file with date/time stamp.
"""
from pygame import mixer
from time import time
from datetime import datetime
def musicloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.set_volume(10)
    mixer.music.play(-1)
    while(True):
        inp = input().lower()
        if inp == stopper:
            mixer.music.stop()
            break
        else:
            print("Enter valid input to stop alarm.")
def logging(msg):
    f = open("tut50_logfile.txt", "a")
    f.write(f"{datetime.now()} {msg}\n")


if __name__ == '__main__':
    initial_water_time = time()
    initiial_eye_time = time()
    initial_physicalexercisse_time = time()
    water_duration_sec = 27*60 #in seconds
    eye_duration_sec = 30*60    #in seconds
    phye_duration_sec = 45*60   #inseconds
    while(True):
        if time() - initial_water_time > water_duration_sec:
            print("Water drinking time\nDon't make me fool enter 'Drank' if you really did.:\n")
            musicloop('water.mp3', "drank")
            initial_water_time = time()
            logging("Water drank")
            print("Well Done, Your water intake logged successfully!")
        if time() - initiial_eye_time > eye_duration_sec:
            print("Eye exercise time\nDon't make me fool enter 'Eydone' if you really did.:\n")
            musicloop('eye.mp3', 'eydone')
            initiial_eye_time = time()
            logging("Eye exercise done")
            print("Well Done, Your Eye exercise logged successfully!")
        if time() - initial_physicalexercisse_time > phye_duration_sec:
            print("Physical exercise time\nDon't make me fool enter 'Pydone' if you really did.:\n")
            musicloop('physical.mp3', "pydone")
            initial_physicalexercisse_time = time()
            logging("Physical exercise done")
            print("Well Done, Your Physical exercise logged successfully!")
