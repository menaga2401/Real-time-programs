#16th program-Stopwatch
import time
start=time.time()
input("Press Enter to stop the stopwatch...")
end=time.time()
total=end-start
print("Time taken:",round(total,2),"seconds")
