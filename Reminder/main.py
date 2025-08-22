import time 
from plyer import notification
while True:
    print("Notification on your desktop")
    notification.notify(title="Reminder to drink water", message="Its time to drink water")
    time.sleep(6)