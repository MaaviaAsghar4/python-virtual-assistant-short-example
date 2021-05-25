import webbrowser
import wikipedia
import speech_recognition as sr
import pyttsx3

# Take voice command from user
def take_command():
    record = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        audio = record.listen(source)
        try:
            Query = record.recognize_google(audio,language='en-in')
            print(Query)
        except Exception:
            print(Exception)
            print("I didn't understand what you said")
            return
        except sr.UnknownValueError:
            print('Google Speech Recognition could not understand')
        except sr.RequestError as e:
            print('Request error from Google Speech Recognition')
        return Query

def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.say(audio)
    engine.runAndWait()

def user_query():
    while(True):
        query = take_command().lower()
        if "wikipedia" in query:
            speak("searching...")
            query = query.replace('search for','')
            query = query.replace('from wikipedia','')
            result = wikipedia.summary(query,sentences=4)
            speak(result)
        elif "open" in query:
            query = query.replace('open','')
            webbrowser.open(query)
        elif "search" in query:
            query = query.replace('search','')
            webbrowser.open('https://google.com/search?q=' + query)

if __name__ == "__main__":
    user_query()