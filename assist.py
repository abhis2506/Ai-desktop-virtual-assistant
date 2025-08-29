import speech_to_text
import text_to_speech
import datetime
import webbrowser
import os

def action(data):
    user_data = str(data).lower()

    if "what is your name" in user_data:
        text_to_speech.text_to_speech("My name is virtual assistant")
        return "My name is virtual assistant"

    elif "hello" in user_data or "hye" in user_data:
        text_to_speech.text_to_speech("Hey,! How can i help you")
        return "Hey,! How can i help you"

    elif "good morning" in user_data : 
        text_to_speech.text_to_speech("good morning!")
        return "good morning!"

    elif "how are you" in user_data:
        text_to_speech.text_to_speech("I'm doing great. How about you?")
        return "I'm doing great. How about you?"

    elif "fine" in user_data or "absolutely fine" in user_data:
        text_to_speech.text_to_speech("Glad to hear that")
        return "Glad to hear that"

    elif "time now" in user_data or "what is the time" in user_data or "time" in user_data:
        current_time = datetime.datetime.now()
        Time = f"{current_time.hour} Hour : {current_time.minute} Minute"
        text_to_speech.text_to_speech(Time)
        return Time

    elif "shut down" in user_data:
        text_to_speech.text_to_speech("ok sir")
        return "ok sir"


    elif "play music" in user_data:
        webbrowser.open("https://music.youtube.com/")
        text_to_speech.text_to_speech("YouTube music is now ready for you")
        return "YouTube music is now ready for you"

    elif "open youtube" in user_data:
        webbrowser.open("https://youtube.com/")
        text_to_speech.text_to_speech("YouTube.com is now ready for you")
        return "YouTube.com is now ready for you"

    elif "open google" in user_data:
        webbrowser.open("https://google.com/")
        text_to_speech.text_to_speech("Google.com is now ready for you")
        return "Google.com is now ready for you"
    
    elif "open irctc" in user_data:
        webbrowser.open("https://www.irctc.co.in/nget/train-search/")
        text_to_speech.text_to_speech("irctc is now ready for you")
        return "Irctc is now ready for you"
    
    
    elif "open calculator" in user_data:
        os.system("calc")
        text_to_speech.text_to_speech("Calculator")
        return "Calculator is now ready for you"
    
    elif "open notepad" in user_data:
        os.system("notepad")
        text_to_speech.text_to_speech("notepad")
        return "notepad is now ready for you"
    
    elif "open ms word" in user_data:
        os.system("start winword")
        text_to_speech.text_to_speech("ms word")
        return "ms word is now ready for you"
    
    elif "open paint" in user_data:
        os.system("mspaint")  # Opens Paint")
        text_to_speech.text_to_speech("paint")
        return "paint is now ready for you"



    else: 
        text_to_speech.text_to_speech("I am not able to understand")
        return "I am not able to understand"