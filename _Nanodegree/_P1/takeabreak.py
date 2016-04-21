import time
import webbrowser

n = 1;

print ("This program started on" + time.ctime())
while(n < 4):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=vCadcBR95oU")
    n = n + 1
