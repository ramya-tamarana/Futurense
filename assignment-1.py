import time
import pyautogui
from tkinter import filedialog
from datetime import datetime
import os
r=int(input())
for i in range(r+1,0,-1):
    for j in range(0,i-1):
        print("*", end=' ')
    time.sleep(2)    
    print(" ")

s=int(input())
for i in range(s):
    for j in range(s):
        if(i==0 or i==s-1 or j==0 or j== s-1):
            print('*', end = '  ')
        else:
            print(' ', end = '  ')
    time.sleep(2)        
    print()
m=pyautogui.screenshot()
count_time=datetime.now().replace(microsecond=0)
print(type(count_time))
Format='%y_%b_%d_%H_%M_%S'
new_time=datetime.strftime(count_time,Format)
file_name='square'+new_time+'.png'
m.save(file_name)

    
