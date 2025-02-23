import time

print("Enter time in seconds: ")
a = int(input())
b = int(a/60)
c = int(a%60)

while a >= 0:
   a = a - 1
   if c > 0:
        c = c - 1
        print(b,":",c)
        time.sleep(1)
        print("\n"*100)

   if b > 0 and c == 0:
        b = b - 1
        c = c + 60

print("TIME ENDED")

    