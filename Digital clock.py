#19th program-Digital clock
import time
while True:
    t=time.strftime("%H:%M:%S")
    print(t,end="\r")
    time.sleep(1)
    
