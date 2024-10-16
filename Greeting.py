import time
ts=time.strftime('%H:%M:%S')
h=int(time.strftime('%H'))
print(ts)
if(h<12):
    print(time.strftime('%H'))
else:
    print(int(time.strftime('%H'))-12)

print(time.strftime('%M'))
print(time.strftime('%S'))
if(h>12):
    print("pm")
else:
    print("am")
if(h<12):
    print("Good Morning,Sir!")
elif(h>=12 and h<18):
    print("Good Evening,Sir!")
else:
    print("Good Night,Sir!")

print("Wishing you all the best")