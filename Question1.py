import time
timestamp = int(time.strftime('%H'))
print(timestamp)
if(timestamp>=0 and timestamp<=3):
    print("Midnight Sir!\n")
elif(timestamp>=18 and timestamp<24):
    print("Good Night Sir!")