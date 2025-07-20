import os

# Paths may vary by system — customize these for your PC
app_paths = {
    "chrome": "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",
    "vscode": "C:\\Users\\abc\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
    "notepad": "C:\\Windows\\notepad.exe",
    "calculator": "C:\\Windows\\System32\\calc.exe",
    "spotify": "C:\\Users\\abc\\Desktop\\Spotify.lnk",
    "discord" : "C:\\Users\\abc\\Desktop\\Discord.lnk",
    "chrome" : "C:\\Users\\abc\\Desktop\\Google Chrome.lnk",
    "blender" : "C:\\Users\\abc\\Desktop\\Blender.lnk",
    "anydesk" : "C:\\Users\\abc\\Desktop\\AnyDesk.lnk",
    "turbovpn" : "C:\\Users\\abc\\Desktop\\TurboVPN.lnk",
    "msedge" : "C:\\Users\\abc\\Desktop\\Microsoft Edge.lnk"

}

call_options = ["open", "launch", "start", "run"]

def open_app(command: str) -> str:
    command = command.lower()
    for call in call_options:
        if call in command:
            for app in app_paths:
                if app in command:
                    try:
                        os.startfile(app_paths[app])
                        return f"Launching {app.capitalize()}..."
                    except Exception as e:
                        return f"Failed to open {app}: {e}"
    return "Sorry, I couldn't recognize the app."

# Example testing
if __name__ == "__main__":
    print(open_app("open notepad"))
