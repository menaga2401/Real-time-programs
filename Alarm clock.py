#18th program-Alarm clock
import time
import winsound
alarm_time=input("Enter alarm time (HH:MM):")
while True:
    current_time=time.strftime("%H:%M")

    if current_time==alarm_time:
        print("Wake up! Alarm ringing!")
        winsound.Beep(1000,3000)
        break

    time.sleep(1)
    

            
