import os
import ctypes
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
import re

shutdown_commands = [
    "shutdown the pc",
    "shut down the pc",
    "turn off the pc",
    "shutdown computer",
    "turn off computer",
    "power off",
    "shutdown now"
]

restart_commands = [
    "restart the pc",
    "reboot the pc",
    "restart computer",
    "reboot computer",
    "restart now",
    "reboot"
]

lock_commands = [
    "lock the screen",
    "lock pc",
    "lock computer",
    "lock it"
]

sleep_commands = [
    "put pc to sleep",
    "sleep now",
    "go to sleep",
    "sleep mode",
    "put computer to sleep"
]

bluetooth_on_commands = [
    "turn on bluetooth",
    "enable bluetooth",
    "bluetooth on"
]

bluetooth_off_commands = [
    "turn off bluetooth",
    "disable bluetooth",
    "bluetooth off"
]

volume_up_commands = [
    "increase volume",
    "volume up",
    "raise the volume",
    "turn up the volume"
]

volume_down_commands = [
    "decrease volume",
    "volume down",
    "lower the volume",
    "turn down the volume"
]



def shutdown_pc():
    print("System will shut down in 10 seconds...")
    os.system("shutdown /s /t 10")
    return "Shutdown command executed."

def restart_pc():
    print("System will restart in 10 seconds...")
    os.system("shutdown /r /t 10")
    return "Restart command executed."

def lock_pc():
    print("Locking the PC...")
    ctypes.windll.user32.LockWorkStation()
    return "Lock command executed."

def sleep_pc():
    print("Putting PC to sleep...")
    ctypes.windll.powrprof.SetSuspendState(False, True, True)
    return "Sleep command executed."

def turn_on_bluetooth():
    print("Turning on Bluetooth...")
    os.system('powershell -Command "Start-Service bthserv"')
    return "Bluetooth should now be ON."

def turn_off_bluetooth():
    print("Turning off Bluetooth...")
    os.system('powershell -Command "Stop-Service bthserv"')
    return "Bluetooth should now be OFF."

def change_volume(delta: float):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = ctypes.cast(interface, ctypes.POINTER(IAudioEndpointVolume))

    current_volume = volume.GetMasterVolumeLevelScalar()
    new_volume = max(0.0, min(1.0, current_volume + delta))
    volume.SetMasterVolumeLevelScalar(new_volume, None)

    print(f"Volume set to {int(new_volume * 100)}%")
    return f"Volume is now {int(new_volume * 100)}%"

def mute_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = ctypes.cast(interface, ctypes.POINTER(IAudioEndpointVolume))
    volume.SetMute(1, None)
    print("Muted.")
    return "Volume muted."

def unmute_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = ctypes.cast(interface, ctypes.POINTER(IAudioEndpointVolume))
    volume.SetMute(0, None)
    print("Unmuted.")
    return "Volume unmuted."

def set_volume_level(percent: int):
    if not (0 <= percent <= 100):
        return "Please specify a volume between 0 and 100."

    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = ctypes.cast(interface, ctypes.POINTER(IAudioEndpointVolume))

    scalar = percent / 100
    volume.SetMasterVolumeLevelScalar(scalar, None)
    print(f"Volume set to {percent}%")
    return f"Volume is now set to {percent}%"

def handle_system_command(command: str) -> str:
    command = command.lower()

    # Check if user wants to set specific volume level like "set volume to 40%"
    match = re.search(r"(set volume to|volume at|change volume to)\s*(\d+)", command)
    if match:
        vol_level = int(match.group(2))
        return set_volume_level(vol_level)

    if any(phrase in command for phrase in shutdown_commands):
        return shutdown_pc()

    elif any(phrase in command for phrase in restart_commands):
        return restart_pc()

    elif any(phrase in command for phrase in lock_commands):
        return lock_pc()
    
    elif any(phrase in command for phrase in sleep_commands):
        return sleep_pc()
    
    elif any(phrase in command for phrase in bluetooth_on_commands):
        return turn_on_bluetooth()

    elif any(phrase in command for phrase in        bluetooth_off_commands):
        return turn_off_bluetooth()
    
    elif any(phrase in command for phrase in volume_up_commands):
        return change_volume(0.1)

    elif any(phrase in command for phrase in volume_down_commands):
        return change_volume(-0.1)

    elif "unmute" in command:
        return unmute_volume()

    elif "mute" in command:
        return mute_volume()



    return "Command not recognized by system control module."

handle_system_command("unmute")