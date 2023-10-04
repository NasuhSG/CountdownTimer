import time
def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer)
        time.sleep(0.5)
        seconds -= 1
    print("Time is up!")


seconds = int(input("Enter a number in seconds: "))

countdown(seconds)

