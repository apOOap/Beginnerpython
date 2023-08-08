# GUI-calculator.py

from tkinter import * # ใช้ User interface
from tkinter import ttk, messagebox # popup เด้งขึ้นมา


###### 1
GUI = Tk() # ทีตัวใหญ่ เคตัวเล็ก
GUI.title('โปรแกรมคำนวณราคาหมู')
GUI.geometry('700x600')

###### 3
bg = PhotoImage(file='car.png')
bg = PhotoImage(file= r'D:\Python Note\Picture\car.png')

BG = Label(GUI, image=bg)
BG.pack() 

###### 2 ข้อความบน GUI
L = Label(GUI,text='กรุณากรอกจำนวนปลา (กิโลกรัม)',font=(None,20))
L.pack() ###### ให้ติดกับ GUI หลัก

######### 4 เพิ่มช่องกรอกจำนวนสินค้า
v_quantity = StringVar() # เป็นตัวแปรที่ใช้เก็บข้อความเมื่อพิมพ์เสร็จแล้ว
E1 = ttk.Entry(GUI, textvariable=v_quantity, font=(None,20)) # เพิ่มช่องกรอกจำนวนสินค้า
E1.pack()

def Cal(): ######## 6 popup เด้ง
	try: # try ดักข้อความ error
		quan = float(v_quantity.get()) #float แปลงเป็นเลข ทศนิยม
		calc = quan * 39 # 39 บาทต่อกิโล ใส่สูตรคำนวณ
		messagebox.showinfo('ราคาทั้งหมด','ราคาปลาทั้งหมด {} บาท'.format(calc) ) ######## 6 popup เด้ง
		v_quantity.set('')
		E1.focus() # กลับไปที่ช่องกรอกข้อมูล
	except: # ถ้า error ให้แจ้งเตือน
		messagebox.showwarning('กรอกผิด','กรุณากรอกเฉพาะตัวเลขเท่านั้น')
		v_quantity.set('1')
		E1.focus() # กลับไปที่ช่องกรอกข้อมูล

######### 5 ปุ่มกดชื่อ คำนวณ
B = ttk.Button(GUI, text='คำนวณ',command=Cal) # ปุ่มชื่อ คำนวณ
B.pack(ipadx=30,ipady=20,pady=20) #ipadx ขยายความกว้าง x/y

GUI.mainloop() # เพื่อให้โปรแกรมรันตลอดเวลา
