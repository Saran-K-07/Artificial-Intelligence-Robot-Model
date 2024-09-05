#------------------------------------- Modules To Import -------------------------------------#

import pyttsx3
import os
import speech_recognition as sr
import openai
import pywhatkit
import pyautogui
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
import datetime
import threading
import time as Time

#------------------------------------- Voice Engine ------------------------------------------#

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#------------------------------------- ChatGPT Api Key ---------------------------------------#

openai.api_key = "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"

#------------------------------------- Tkinter Setup -----------------------------------------#

class WrappingLabel(tk.Label):
    '''a type of Label that automatically adjusts the wrap to the size'''
    def __init__(self, master=None, **kwargs):
        tk.Label.__init__(self, master, **kwargs)
        self.bind('<Configure>', lambda e: self.config(wraplength=self.winfo_width()))

root = tk.Tk()
root.attributes('-fullscreen',True)
root.title("AI Voice Bot")
label = WrappingLabel(root,font=("castellar",16))
label.pack(
    ipadx=50,
    ipady=250,
    expand=True
)

#------------------------------------- Functions ---------------------------------------------#

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        label.config(text='Listening....')
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        label.config(text='Wait for few seconds....')
        query = r.recognize_google(audio, language='en-in')
        label.config(text=f"""You said,"{query}." """)
        return query
    except Exception as e:
        print(e)
        speak('Please, Can you say it again?')
        return 'none'

def download_clicked():
    while True:
            query = takecommand().lower()
        
            if 'open browser' in query:
                path = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
                speak("Opening Browser!")
                os.startfile(path)

            elif 'open onedrive' in query:
                path = "C:\Program Files\Microsoft OneDrive\OneDrive.exe"
                speak("Opening Onedrive!")
                os.startfile(path)

            elif 'open notepad plus plus' in query:
                path = "C:/Program Files/Notepad++/notepad++.exe"
                speak("Opening Notepad Plus Plus!")
                os.startfile(path)

            elif 'open pdf editor' in query:
                path = "C:\Program Files\Tracker Software\PDF Editor\PDFXEdit.exe"
                speak("Opening PDF Editor!")
                os.startfile(path)

            elif 'open wordpad' in query:
                path = "C:\Program Files\Windows NT\Accessories\wordpad.exe"
                speak("Opening Wordpad!")
                os.startfile(path)
                
#            elif 'open teams' in query:
#                path = "C:\Program Files (x86)\Teams Installer\Teams.exe"
#                speak("Opening Teams!")
#                os.startfile(path)
                
            elif 'open turbo vpn' in query:
                path = "C:\Program Files (x86)\TurboVPN\TurboVPNLauncher.exe"
                speak("Opening Turbo VPN!")
                os.startfile(path)
                
            elif 'open vlc' in query:
                path = "C:\Program Files (x86)\VideoLAN\VLC\vlc.exe"
                speak("Opening VLC!")
                os.startfile(path)
                
            elif 'open capcut' in query:
                path = "C:/Users/saran kishore/AppData/Local/CapCut/Apps/CapCut.exe"
                speak("Opening CapCut!")
                os.startfile(path)
                
            elif 'open wps office' in query:
                path = "C:/Users/saran kishore/AppData/Local/Kingsoft/WPS Office/ksolaunch.exe"
                speak("Opening WPS Office!")
                os.startfile(path)
                
            elif 'open media player' in query:
                path = "C:\\Users\\saran kishore\\AppData\\Local\\Microsoft\\WindowsApps\\MediaPlayer.exe"
                speak("Opening Media Player!")
                os.startfile(path)
                
            elif 'open skype' in query:
                path = "C:\\Users\\saran kishore\\AppData\\Local\\Microsoft\\WindowsApps\\Skype.exe"
                speak("Opening Skype!")
                os.startfile(path)
                
            elif 'open spotify' in query:
                path = "C:\\Users\\saran kishore\\AppData\\Local\\Microsoft\\WindowsApps\\Spotify.exe"
                speak("Opening Spotify!")
                os.startfile(path)
                
            elif 'open powershell' in query:
                path = "C:\\Windows\\SysWOW64\\WindowsPowerShell\\v1.0\\powershell.exe"
                speak("Opening Powershell!")
                os.startfile(path)

            elif 'open settings' in query:
                path = "C:\WINDOWS\System32\control.exe"
                speak("Opening Settings!")
                os.startfile(path)

            elif 'open whatsapp' in query:
                path = "https://web.whatsapp.com/"
                speak("Opening Whatsapp!")
                os.startfile(path)

            elif 'open youtube' in query:
                path = "https://www.youtube.com/"
                speak("Opening Youtube!")
                os.startfile(path)

            elif 'open google' in query:
                path = "https://www.google.com/"
                speak("Opening Google!")
                os.startfile(path)

            elif 'open facebook' in query:
                path = "https://www.facebook.com/"
                speak("Opening Facebook!")
                os.startfile(path)

            elif 'open instagram' in query:
                path = "https://www.instagram.com/"
                speak("Opening Instagram!")
                os.startfile(path)

            elif 'open amazon' in query:
                path = "https://www.amazon.in/"
                speak("Opening Amazon!")
                os.startfile(path)

            elif 'open meesho' in query:
                path = "https://www.meesho.com/"
                speak("Opening Meesho!")
                os.startfile(path)

            elif 'open twitter' in query:
                path = "https://twitter.com/"
                speak("Opening Twitter!")
                os.startfile(path)

            elif 'open linkedin' in query:
                path = "https://www.linkedin.com/"
                speak("Opening Linked In!")
                os.startfile(path)

            elif 'open wikipedia' in query:
                path = "https://www.wikipedia.com/"
                speak("Opening Wikipedia!")
                os.startfile(path)

            elif 'open tamil wikipedia' in query:
                path = "https://ta.wikipedia.org/"
                speak("Opening Tamil Wikipedia!")
                os.startfile(path)

            elif 'open maths solver' in query:
                path = "https://mathsolver.microsoft.com/en?ref=msn"
                speak("Opening Math Solver!")
                os.startfile(path)

            elif 'open' and 'website' in query:
                query = query.replace('open',' ')
                query = query.replace('website',' ')
                path = f"https://www.bing.com/search?q={query}"
                speak(f"Opening {query}!")
                os.startfile(path)
                
            elif 'what is your name' in query:
                speak("My name is Mr.Cool.")
                
            elif "exit" in query:
                speak("See you again soon!")
                label.config(text="Restart the program to run")

            elif 'time' in query:
                time = datetime.datetime.now().strftime('%I:%M %p')
                label.config(text='The time is' + time)
                speak('The Time is' + time)

            elif "date" in query:
                date = datetime.datetime.now().strftime("%d-%m-%Y")
                label.config(text="The Date is" + date)
                speak('The Date is' + date)

            elif 'day' in query:
                dt = datetime.datetime.now()
                day = dt.strftime('%A')
                label.config(text="The Day is" + day)
                speak('The Day is' + day)

            elif 'your name' in query:
                speak('I am Mister Cool. How can I assist you today?')
                
            elif 'minimise' in query:
                speak('Minimizing the Window')
                pyautogui.leftClick(1983,23)

            elif 'close' in query:
                speak('Closing the Window')
                pyautogui.leftClick(2117,9)
                
            elif 'play' in query:
                video = query.replace('play', '')
                speak('playing' + video)
                pywhatkit.playonyt(video)

#            elif 'shut down' in query:
#                os.system('shutdown /s /t 5')
#                speak('Shutting Down in five seconds')
                
#            elif 'restart' in query:
#                os.system('shutdown /r /t 5')
#                speak('Restarting in five seconds')
            
            elif "chairman of avp" in query:
                speak("The Chairman of AVP Institutions is Rotarian Major Donor PDG A Karthikeyan")
            
            elif "principal of avp" in query:
                speak("The Principal of AVP School is Mrs Priyaraja")             
            
            elif "coordinator of avp" in query:
                speak("The Coordinator of AVP School is Mrs Abithabanu")

            elif "treasurer of avp" in query:
                speak("The Treasurer of AVP School is Mrs Latha Karthikeyan")             
            
            elif "founder of avp" in query:
                speak("The Founder of AVP School is Thiru A P Arul Jothi")             
            
            elif "created you" in query:
                path = "C:/Users/saran kishore/Jupyter Lab/creator.jpg"
                os.startfile(path)
                speak("I was created by a team of students and teachers of avp school")
                Time.sleep(5)
                pyautogui.leftClick(2117,9)

            elif "latha" in query:
                label.config(text="She is working in AVP School. She is handling the subject Tamil")
                speak("She is working in AVP School. She is handling the subject Tamil")

            elif "selvi" in query:
                label.config(text="She is working in AVP School. She is handling the subject Tamil")
                speak("She is working in AVP School. She is handling the subject Tamil")

            elif "ester" in query:
                label.config(text="She is working in AVP School. She is handling the subject Tamil")
                speak("She is working in AVP School. She is handling the subject Tamil")

            elif "prathiba" in query:
                label.config(text="She is working in AVP School. She is handling the subject English")
                speak("She is working in AVP School. She is handling the subject English")

            elif "dominic" in query:
                label.config(text="He is working in AVP School. He is handling the subject English")
                speak("He is working in AVP School. He is handling the subject English")

            elif "duraisamy" in query:
                label.config(text="He is working in AVP School. He is handling the subject English")
                speak("He is working in AVP School. He is handling the subject English")

            elif "radhakrishanan" in query:
                label.config(text="He is working in AVP School. He is handling the subject English")
                speak("He is working in AVP School. He is handling the subject English")

            elif "jabekumar" in query:
                label.config(text="He is working in AVP School. He is handling the subject English")
                speak("He is working in AVP School. He is handling the subject English")

            elif "n karthikeyan" in query:
                label.config(text="He is working in AVP School. He is handling the subject Mathematics")
                speak("He is working in AVP School. He is handling the subject Mathematics")

            elif "nagarathinam" in query:
                label.config(text="She is working in AVP School. She is handling the subject Mathematics")
                speak("She is working in AVP School. She is handling the subject Mathematics")

            elif "tamilselvan" in query:
                label.config(text="He is working in AVP School. He is handling the subject Physics")
                speak("He is working in AVP School. He is handling the subject Physics")

            elif "vijaykumar" in query:
                label.config(text="He is working in AVP School. He is handling the subject Physics")
                speak("He is working in AVP School. He is handling the subject Physics")

            elif "sivakumar" in query:
                label.config(text="He is working in AVP School. He is handling the subject Chemistry")
                speak("He is working in AVP School. He is handling the subject Chemistry")

            elif "vanaja" in query:
                label.config(text="She is working in AVP School. She is handling the subject Chemistry")
                speak("She is working in AVP School. She is handling the subject Chemistry")

            elif "nithya" in query:
                label.config(text="She is working in AVP School. She is handling the subject Computer Science and Computer Application")
                speak("She is working in AVP School. She is handling the subject Computer Science and Computer Application")

            elif "bhavani" in query:
                label.config(text="She is working in AVP School. She is handling the subject Computer Science and Computer Application")
                speak("She is working in AVP School. She is handling the subject Computer Science and Computer Application")

            elif "swetha" in query:
                label.config(text="She is working in AVP School. She is handling the subject Computer Science")
                speak("She is working in AVP School. She is handling the subject Computer Science")

            elif "location of school" in query:
                label.config(text="Our school is situated in the northern part of the hosiery town where the famous historical temple located at Thirumuruganpoondi. This place is famous for sculptures also. Our school is located behind the Thirumuruganpoondi temple and about 1.5 kms from Tirupur and Avinashi Main Road. Aathupalayam, Chettipalayam, Kalampalayam, Pooluvapatti are the villages situated near our school")
                speak("Our school is situated in the northern part of the hosiery town where the famous historical temple located at Thirumuruganpoondi. This place is famous for sculptures also. Our school is located behind the Thirumuruganpoondi temple and about 1.5 kms from Tirupur and Avinashi Main Road. Aathupalayam, Chettipalayam, Kalampalayam, Pooluvapatti are the villages situated near our school")

            elif "head boy" in query:
                label.config(text="The Headboy of our school is Jayasurya of Class 12th B")
                speak("The Headboy of our school is Jayasurya of Class 12th B")

            elif "head girl" in query:
                label.config(text="The Headgirl of our school is Sowkavi of Class 12th E")
                speak("The Headgirl of our school is Sowkavi of Class 12th E")

            elif "school" and "strength" in query:
                label.config(text="Our school contains 3000 approx.")
                speak("Our school contains 3000 approx.")

            elif "what" and "the story" in query:
                label.config(text="Today is our edu expo. We welcome you all. You can learn more from our projects.")


            elif "none" not in query:
                completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=[{"role": "system", "content": "You are a helpful assistant."},{"role": "user", "content": query}])
                label.config(text=completion.choices[0].message.content)
                speak(completion.choices[0].message.content)

            else:
                break
                
#------------------------------------- Execution of Program ----------------------------------#

threading.Thread(target=download_clicked).start()

if __name__ == "__main__":
    while True:
      root.mainloop()
      threading.Thread(target=download_clicked).join()
        
#------------------------------------- End of the Program ------------------------------------#
