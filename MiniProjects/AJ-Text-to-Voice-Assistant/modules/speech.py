from datetime import datetime
import pyttsx3


# Initilize the speech engine

engine = pyttsx3.init()

def speak(text):
    """Print a message and speak it aloud"""

    print(f"AJ :{text}")

    engine.say(text)
    engine.runAndWait()



# greeting 

def greet_user():
    """Greet the user based on the current time"""
    hour = datetime.now().hour

    if 5<= hour <12:
        speak("Good Morning , Sir . AJ is ready to help you.")

    elif 12<=hour <17:
        speak("Good afternoon, Sir. How can I help you?")

    elif 17<=hour <21:
        speak("Good evening, Sir. How I help you?")
    else:
        speak(" Hello , Sir Aj is ready to assist you.")
        
                    
