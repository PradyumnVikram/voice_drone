import speech_recognition as sr

r = sr.Recognizer()

directions = {"forward":1, "backward":2, "left":3, "right":4}

with sr.Microphone() as source:
    print("Adjusting for ambient noise...")
    r.adjust_for_ambient_noise(source, duration=1)
    
    print("Listening... Speak now!")
    audio = r.listen(source)
    
    print("Processing...")

try:
    text = r.recognize_google(audio)
    for direction in directions.keys():
        if direction in text.lower():
            print(directions[direction])
    
except sr.UnknownValueError:
    print("Sorry, could not understand the audio")
    
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")
