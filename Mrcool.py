import pyttsx3
import datetime
import wikipedia
import webbrowser
import pywhatkit
import pyjokes
import os
import pyautogui
import openai
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
openai.api_key = "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"



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('good  morning  chief')
    elif hour >= 12 and hour < 15:
        speak('good  afternoon  chief')
    elif hour >= 15 and hour < 19:
        speak('good  evening  chief')
    else:
        speak('hello  chief')


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print('Wait for few seconds....')
        query = r.recognize_google(audio, language='en-in')
        print('User >>>', query)
        return query
    except Exception as e:
        print(e)
        speak('Please, Can you say  it  again?')
        return "none"


if __name__ == "__main__":
    while True:
        query = takecommand().lower()
        if 'mr cool' in query:
            wishme()
            speak('i am ready  chief')
            speak("naan  enna  saiya  vendum  chief")
            while True:
                query = takecommand().lower()
                if "wikipedia" in query:
                    speak('searching  in  wikipedia')
                    query = query.replace('wikipedia', "")
                    results = wikipedia.summary(query, sentences=5, auto_suggest=False, redirect=True)
                    print(results)
                    speak(results)
                elif 'open youtube' in query:
                    webbrowser.open('youtube.com')
                elif 'open google' in query:
                    webbrowser.open('google.com')
                elif 'play' in query:
                    video = query.replace('play', '')
                    speak('playing' + video)
                    pywhatkit.playonyt(video)
                elif 'time' in query:
                    time = datetime.datetime.now().strftime('%I:%M %p')
                    print('The time is', time)
                    speak('the time is' + time)
                elif 'joke' in query:
                    joke = pyjokes.get_joke()
                    print(joke)
                    speak(joke)
                elif 'open chrome' in query:
                    path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk"
                    speak("opening chrome")
                    os.startfile(path)
                elif 'open python' in query:
                    path1 = 'C:\\Users\\WELCOME\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.10\\IDLE (Python 3.10 64-bit).lnk'
                    speak("opening python")
                    os.startfile(path1)
                elif 'quit' in query:
                    speak('turning off chief')
                    break
                elif 'exit' in query:
                    exit()
                elif "date" in query:
                    date = datetime.datetime.now().strftime("%d-%m-%Y")
                    print("The Date is", date)
                    speak('the date is' + date)
                elif 'your name' in query:
                    speak('i am Mister cool chief')
                elif 'thank you' in query:
                    speak('welcome  at your service chief')
                elif 'day' in query:
                    dt = datetime.datetime.now()
                    day = dt.strftime('%A')
                    print("The Day is", day)
                    speak('the day is' + day)
                elif 'maximize' in query:
                    speak('maximizing chief')
                    pyautogui.leftClick(938, 1056)
                elif 'minimise' in query:
                    speak('minimizing chief')
                    pyautogui.leftClick(1803, 13)
                elif 'shut down' in query:
                    speak('are you sure chief')
                    if 'yes' in query:
                        os.system('shutdown /s /t 5')
                        speak('shutting down in five seconds chief')
                elif 'restart' in query:
                    speak('are you sure chief')
                    if 'yes' in query:
                        os.system('shutdown /r /t 5')
                        speak('restarting in five seconds chief')
                elif 'none' not in query:
                    completion = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": "You are a helpful assistant."},
                            {"role": "user", "content": query}
                        ]
                    )
                    print(completion.choices[0].message.content)
                    speak(completion.choices[0].message.content)
