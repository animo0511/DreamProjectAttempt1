import pyautogui
import time
import psutil
import webbrowser
import pygetwindow as gw
from open_website import browser_process_names

call_options = ["search for", "look up", "google", "find", "look for"]

# Register Chrome manually before using it
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))

def is_browser_running() -> str:
    for name, process in browser_process_names.items():
        for proc in psutil.process_iter(['name']):
            try:
                if process.lower() in proc.info['name'].lower():
                    return name  # returns browser name
            except:
                pass
    return None

def focus_browser_window() -> bool:
    for window in gw.getAllTitles():
        if "chrome" in window.lower() or "edge" in window.lower():
            try:
                win = gw.getWindowsWithTitle(window)[0]
                win.restore()
                win.activate()
                return True
            except:
                pass
    return False

def open_browser_by_name(name: str):
    if name.lower() == "chrome":
        webbrowser.get("chrome").open("https://www.google.com")
        time.sleep(5)  # Wait for Chrome to fully open (5 seconds)
    elif name.lower() == "edge":
        webbrowser.get("windows-default").open("https://www.bing.com")
        time.sleep(5)  # Wait for Edge to fully open (5 seconds)
    else:
        print("Unknown browser requested.")

def open_new_tab_in_browser():
    # Open a new tab using keyboard shortcuts (CTRL + T)
    pyautogui.hotkey('ctrl', 't')
    time.sleep(1)  # Wait a moment before typing

def search_web(command: str) -> str:
    command = command.lower()
    
    # extract query
    for call in call_options:
        if call in command:
            command = command.split(call)[-1].strip()
            break

    if command.strip() == "":
        return "What do you want me to search?"

    # Check if browser is running
    running_browser = is_browser_running()

    if not running_browser:
        print("No browser is currently open.")
        print("I'd like to open a browser to fulfill your request.")
        browser_choice = input("Please type your preferred browser (Chrome/Edge): ").lower()

        if browser_choice in ["chrome", "edge"]:
            print(f"Opening {browser_choice}...")
            open_browser_by_name(browser_choice)
            time.sleep(5)  # wait for it to launch

            if not focus_browser_window():
                return "Opened browser, but couldn’t focus on it."
        else:
            return "Invalid browser choice. Please try again."
    else:
        focus_browser_window()
        time.sleep(1)

    # Open a new tab in the browser before typing the search
    open_new_tab_in_browser()

    # Type search query and press Enter
    pyautogui.write(command, interval=0.05)
    pyautogui.press("enter")
    return f"Searching for '{command}'..."

print(search_web("luffy"))