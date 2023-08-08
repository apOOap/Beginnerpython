from tkinter import *
from tkinter import ttk
import pyautogui as pg
import sys
import webbrowser

GUI = Tk()
GUI.title('โปรแกรมสั่งกดปฎิทิน')
GUI.geometry('500x300')

def Canlender(): #pyautogui.click(1830,1057) # ปฎิทิน
    pg.click(1830,1057)
    

B1 = Button(GUI,text='Callendar1',command=Canlender)
B1.pack(ipadx=20, ipady=20, pady=20)

B2 = ttk.Button(GUI,text='Callendar2',command=Canlender)
B2.pack(ipadx=20, ipady=10)

def Google():
    webbrowser.open('https://www.google.co.th')

B2 = ttk.Button(GUI,text='Google',command=Google)
B2.pack(ipadx=20, ipady=10)

GUI.mainloop()




 

