import speech_recognition as sr
import numpy as np
r = sr.Recognizer()

drone_coordinate = np.array([0,0,3])

directions = {"forward":np.array([1,0,0]), "backward":np.array([-1,0,0]), "left":np.array([0,1,0]), "right":np.array([0,-1,0])}

def return_coordinates():
    drone_coordinate = np.array([0,0,3])

    directions = {"forward":np.array([1,0,0]), "backward":np.array([-1,0,0]), "left":np.array([0,1,0]), "right":np.array([0,-1,0])}

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
                drone_coordinate = directions[direction]
        return drone_coordinate
        
    except sr.UnknownValueError:
        return np.zeros(3)
        
    except sr.RequestError as e:
        return np.zeros(3)
