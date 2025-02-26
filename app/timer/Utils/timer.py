import time
def timer(time=10):
     b = int(time/60)
     c = int(time%60)

     while time >= 0:
          time = time - 1
          if c > 0:
               c = c - 1
               print(b,":",c)
               time.sleep(1)
               print("\n"*100)

          if b > 0 and c == 0:
               b = b - 1
               c = c + 60

          print("TIME ENDED")

