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
    
def App():
    window = Tk()
    
    window.title("Password Generator")
    window.geometry("720x480")
    window.config(background="#000000")
    
    label = Label(window, text="TinyTask, Press the keys to repeat in the entry.", width=720, fg="white", bg="black", font="700")
    label.pack()
    
    frame = Frame(window, bg="black", width=700, height=460)
    frame.pack(expand=YES)

    input = Entry(frame)
    input.pack()
    b_put = Button(frame, text="Start", font="Courrier, 30", command=Tinytask)
    b_put.pack(expand=YES)

    window.mainloop()
    
App()
