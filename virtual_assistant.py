import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import dictionary

engine=pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def jarvisvoice(audio):
    engine.say(audio)
    engine.runAndWait()



def wish():
    h=int(datetime.datetime.now().hour)

    print("Time right now--->",h)
    if(h>=0 and h<12):
        jarvisvoice("Good Morning Utkarsh..... ")
    elif h>=12 and h<18:
         jarvisvoice("Good AfterNoon....... ")
    else:
        jarvisvoice("Good Evening Utkarsh....")

def takecommand():
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening Utkarsh........")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing.........")
        query= r.recognize_google(audio,language='en-in')
        print("Query",query)

    except Exception as e:
        print(e)
        print("Sorry Utkarsh!!,Say that again please.....")
        return "None"
    return query

wish()

status=True
while status:
    query=takecommand().lower()

    if "what is" in query or "who is" in query:
        jarvisvoice("Searching in Wikipedia....please wait")
        query=query.replace("wikipedia","")
        results=wikipedia.summary(query,sentences=1)
        print(results)
        jarvisvoice("According to wikipedia...")
        jarvisvoice(results)

    if "meaning of" in query or "what is the meaning of" in query:
        jarvisvoice("Utkarsh, please write in google....")
        webbrowser.open("google.com/meaning of ",query)

    elif "open google" in query:
        webbrowser.open("google.com")
    elif "open youtube" in query:
        webbrowser.open("youtube.com")
    elif "open gmail" in query:
        webbrowser.open("gmail.com")
    elif "open StudioYoutube " in query:
        webbrowser.open("studio.youtube.com")
    elif "open cartoon " in query:
        webbrowser.open("animix.com")
    elif "who are you" in query:
        jarvisvoice("Im? ,i am your assistant.")






