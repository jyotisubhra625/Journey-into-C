'''WAP which reminds you to drink water every hour or two .
Your pogram can either beep or send desktop notification for a specific O.S.'''


import plyer
import time
import os

def drink_water_reminder():
    while True:
        plyer.notification.notify(title="Drink Water", message="Drink water", timeout=10) # type: ignore
        print("Press CTRL+C to stop the reminder")
        time.sleep(3600)  # Wait for 1 hour

if __name__ == "__main__":
    try:
        drink_water_reminder()
    except KeyboardInterrupt:
        print("Reminder stopped")
        os._exit(0)  # Exit the script
