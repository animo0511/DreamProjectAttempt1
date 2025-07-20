import webbrowser
import speech_recognition as sr

recognizer = sr.Recognizer()

# Map keywords to URLs
website_map = {
    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com",
    "github": "https://www.github.com",
    "stackoverflow": "https://stackoverflow.com",
    "gmail": "https://mail.google.com"
}

def open_website(command):
    for key in website_map:
        if key in command:
            webbrowser.open(website_map[key])
            return f"Opening {key}..."
    return "Sorry, I don't recognize that website."

# Voice input listener
def listen_and_open():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for website command...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)

        if "junior" in command and "open" in command:
            response = open_website(command)
            print(response)
        else:
            print("No valid website command detected.")

    except sr.UnknownValueError:
        print("Could not understand the audio.")
    except sr.RequestError:
        print("Speech service is unavailable.")

# Run the function if this file is executed directly
if __name__ == "__main__":
    listen_and_open()
