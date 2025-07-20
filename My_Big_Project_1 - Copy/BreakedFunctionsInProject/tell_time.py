# tell_time.py

import datetime

def tell_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M %p")  # Example: 05:23 PM
    return f"The current time is {current_time}"

if __name__ == "__main__":
    print(tell_time())
