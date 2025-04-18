import openai
import speech_recognition as sr
import pyttsx3
import subprocess
import os
import requests
from playsound import playsound
from dotenv import load_dotenv
load_dotenv()




openai.api_key = os.getenv("OPENAI_API_KEY")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
engine = pyttsx3.init()



def speak(text):
    voice_id = "21m00Tcm4TlvDq8ikWAM"

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }

    data = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        with open("jarvis_output.mp3", "wb") as f:
            f.write(response.content)
        playsound("jarvis_output.mp3")
        os.remove("jarvis_output.mp3")
    else:
        print("Error with ElevenLabs API:", response.text)

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "Sorry, I didn’t catch that."
    except sr.RequestError:
        return "Speech service unavailable."

def get_gpt_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful voice assistant named Jarvis."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

# 🧠 Function to handle simple automation commands
def run_command(command):
    command = command.lower()

    if "open chrome" in command:
        speak("Opening Chrome.")
        subprocess.Popen("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
    
    elif "open code" in command or "open vs code" in command:
        speak("Opening Visual Studio Code.")
        subprocess.Popen("C:\\Users\\Jleon\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

    elif "create folder" in command:
        folder_name = command.replace("create folder", "").strip()
        path = os.path.join(os.getcwd(), folder_name)
        os.makedirs(path, exist_ok=True)
        folder_location = os.path.basename(os.getcwd())  # Get just the current folder name
        speak(f"I created the folder {folder_name} in the {folder_location} folder.")
        
    elif any(phrase in command for phrase in ["search google for", "look up", "find information about"]):
        # Normalize input
        if "search google for" in command:
            query = command.split("search google for")[-1].strip()
        elif "look up" in command:
            query = command.split("look up")[-1].strip()
        elif "find information about" in command:
            query = command.split("find information about")[-1].strip()
        else:
            query = ""

        if query:
            speak(f"Searching Google for {query}")
            search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
            os.startfile(search_url)
        else:
            speak("What would you like me to search for?")


    elif "play music" in command:
        music_path = "C:\\Users\\Jleon\\Music\\your_song.mp3"  # Change to a real file
        os.startfile(music_path)

    else:
        speak("I don't know how to do that yet.")

# 🔁 Main loop
WAKE_WORD = "hey jarvis"

while True:
    print("Waiting for wake word...")
    command = listen().lower()
    print(f"You said: {command}")

    if WAKE_WORD in command:
        speak("Yes?")
        command = listen().lower()
        print(f"Command: {command}")

        if command in ["exit", "quit", "goodbye"]:
            speak("Goodbye!")
            break

        # These keywords trigger automation
        automation_triggers = [
            "open", 
            "create", 
            "play", 
            "search google for", 
            "look up", 
            "find information about"
        ]

        if any(trigger in command for trigger in automation_triggers):
            run_command(command)
        else:
            reply = get_gpt_response(command)
            print(f"Jarvis: {reply}")
            speak(reply)
