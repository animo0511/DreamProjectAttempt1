import time
import threading
from tkinter import Tk, Label
from plyer import notification
import simpleaudio as sa


def play_sound():
    try:
        wave_obj = sa.WaveObject.from_wave_file("C:\\Users\\abc\\Desktop\\file_example_WAV_10MG.wav")  # path to your sound file
        play_obj = wave_obj.play()
        play_obj.wait_done()
    except Exception as e:
        print("Error playing sound:", e)


def start_countdown(task, seconds):
    def countdown():
        nonlocal seconds
        while seconds >= 0:
            mins, secs = divmod(seconds, 60)
            label.config(text=f"{task}\n{mins:02d}:{secs:02d}")
            root.update()
            time.sleep(1)
            seconds -= 1

        root.destroy()

        # 🔔 Notify and sound
        notification.notify(
            title="⏰ Reminder!",
            message=f"Time for: {task}",
            timeout=5
        )
        play_sound()

    # Setup GUI
    root = Tk()
    root.title("Reminder")
    root.geometry("250x100")
    root.configure(bg="black")

    label = Label(root, text="", font=("Arial", 18), fg="lime", bg="black")
    label.pack(expand=True)

    countdown()
    root.mainloop()


def visual_reminder(task, minutes=1):
    seconds = int(minutes * 60)
    threading.Thread(target=start_countdown, args=(task, seconds)).start()


# 🧪 Example usage
visual_reminder("Take a break!", 0.1)  # runs for 6 seconds
