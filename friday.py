import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os

friday = pyttsx3.init()
voice = friday.getProperty('voices')
newVoiceRate = 145
friday.setProperty('rate',newVoiceRate)
friday.setProperty('voice', voice[1].id)

def speak(audio):
    print('F.R.I.D.A.Y : ' + audio)
    friday.say(audio)
    friday.runAndWait()

def time():
    time = datetime.datetime.now().strftime("%H:%M %p")
    speak(time)
# speak('Hello Youtube')

def welcome():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak('Good Morning,sir')
    if hour >= 12 and hour < 18:
        speak('Good afternoon ,sir')
    if hour >= 18 and hour <= 24:
        speak('Good evening,sir')
    if hour < 6:
        speak('Good evening,sir')
    speak("How can I help you?")

def command():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold = 2
        audio = c.listen(source)
    try:
        query = c.recognize_google(audio, language="en")
        print("Quoc Cuong : " + query)
    except sr.UnknownValueError:
        print("Please repeat or typing the command")
        query = str(input('Your order is: '))
    return query
if __name__ == "__main__":
    welcome()
    while True:
        query = command().lower()
        if "google" in query:
            speak("What should I search, boss?")
            search = command().lower()
            url = f"https://google.com/search?q={search}"
            wb.get().open(url)
            speak(f"Here is your {search} on Google")
        if "youtube" in query:
            speak("What should I search, boss?")
            search = command().lower()
            url = f"https://youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f"Here is your {search} on Youtube")
        if "open video" in query:
            file = r"E:\Downloads\Marvels.Iron.Fist.S02E10.A.Duel.of.Iron.1080p.NF.WEB-DL.Atmos.DDP5.1.HDR.HEVC (1).mkv"
            speak("Sure, enjoy your video, boss")
            os.startfile(file)
        if "time" in query:
            time()
        if "quit" in query:
            speak("Friday is quiting sir. Goodbye boss")
            quit()