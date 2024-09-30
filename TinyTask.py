from tkinter import *
import pyautogui
import time

times = int(input("Interval of time between action = "))

def Tinytask():
    value = input.get()
    print(value)
    
    for i in range(len(value)):
        time.sleep(times)
        pyautogui.write(value[i])
        pyautogui.click()
    

window = Tk()
window.title("Password Generator")
window.geometry("720x480")
window.config(background="#000000")

input = Entry(window)
input.grid(row=2)
b_put = Button(window, text="Start", font="Courrier, 30", command=Tinytask)
b_put.grid(row=3)

window.mainloop()
