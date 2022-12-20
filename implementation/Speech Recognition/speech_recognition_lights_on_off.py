import speech_recognition as sr
import pyttsx3

# Initialize the speech recognition object
r = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Define a function to turn the lights off
def turn_lights_off():
    lights = "off"
    print("Lights are now " + lights)
    engine.say("Lights are now off")

# Define a function to turn the lights on
def turn_lights_on():
    lights = "on"
    print("Lights are now " + lights)
    engine.say("Lights are now on")

while True:
    # Listen for speech
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    # Convert the speech to text
    try:
        text = r.recognize_google(audio)
        print("You said: " + text)

        # If the recognized text is "turn off the lights", call the turn_lights_off function
        if text == "turn off the lights":
            turn_lights_off()
        # If the recognized text is "turn the lights on", call the turn_lights_on function
        elif text == "turn the lights on":
            turn_lights_on()
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Error processing request: " + e)

    # Speak the recognized text out loud
    # engine.say(text)
    engine.runAndWait()
