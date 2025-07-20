import pyttsx3
import os
import time
import json
import queue
import pyaudio
import speech_recognition as sr
from vosk import Model, KaldiRecognizer
from website_commands import open_website
import tell_time
import cohere # Our ai model which we are using in this project 

# Initialize TTS engine
engine = pyttsx3.init()
recognizer = sr.Recognizer()

# Cohere API key
cohere_client = cohere.Client('ufpJH9hn2NU4j8GIQzr8eHdzTxT3ursxNXaNWlWF')

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Load Vosk model
if not os.path.exists("model"):
    print("❌ Vosk model not found! Please download and extract it into a folder named 'model'.")
    exit()

vosk_model = Model("model")
recognizer_vosk = KaldiRecognizer(vosk_model, 16000)

# Setup audio stream
audio_interface = pyaudio.PyAudio()
stream = audio_interface.open(format=pyaudio.paInt16, channels=1, rate=16000,
                              input=True, frames_per_buffer=8192)
stream.start_stream()

print("🔊 System initialized. Say 'Junior' to activate.")

def get_ai_responcse(prompt):
    # Function to get a responses from Cohere AI
    response = cohere_client.generate(
        model="command-xlarge-2022108",
        prompt=prompt,
        max_tokens=50,
        temperature=0.7,
        stop_sequences=["\n"]
    )
    return response.generations[0].text.strip()

while True:
    data = stream.read(4096, exception_on_overflow=False)

    if recognizer_vosk.AcceptWaveform(data):
        result = json.loads(recognizer_vosk.Result())
        text = result.get("text", "").lower()

        if text:
            print(f"\r🎧 Heard: {text}          ", end="")

            if "junior" in text:
                print("\n🟢 Wake word detected: Junior")
                speak("Yes sir")

                # Listen for next command using Google (for better accuracy)
                try:
                    with sr.Microphone() as source:
                        print("🎤 Awaiting your command...")
                        recognizer.adjust_for_ambient_noise(source, duration=0.5)
                        audio = recognizer.listen(source, phrase_time_limit=5)
                        command = recognizer.recognize_google(audio).lower()
                        print("🗣️ You said:", command)

                        if "open" in command:
                            response = open_website(command)
                            speak(response)

                        elif "time" in command:
                            response = tell_time.tell_time()
                            speak(response)

                        else:
                            ai_response = get_ai_responcse(command)
                            print("🤖 Cohere says:", ai_response)
                            speak(ai_response)


                            
                except sr.UnknownValueError:
                    speak("I didn't understand. Try again.")
                except sr.RequestError:
                    speak("Please check your internet connection.")
