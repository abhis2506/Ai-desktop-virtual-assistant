import speech_recognition as sr

def speech_to_text():
    r = sr.Recognizer()

    # Use the microphone as the source for input
    with sr.Microphone() as source:
        print("Listening... Please speak.")
        r.adjust_for_ambient_noise(source)  # Optional: helps reduce noise
        audio = r.listen(source)

    try:
        # Recognize speech using Google Web Speech API
        voice_data = r.recognize_google(audio)
        print(f"You said: {voice_data}")
        return voice_data

    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return None

    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None

