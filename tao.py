import time

def sawaddee():         # function ชื่อ sawaddee
	print('สวัสดีครับ')    # คำสั่งให้ สวัสดีครับ
sawaddee()              #  เรียกใช้ function sawaddee

def sawaddeemak():
	for i in range(10):
		print('sawaddeemak')
sawaddeemak()

def sawaddee02(name='คุณลูกค้า'):   # บังคับให้ใส่ข้อมูล
		print(f'{name} สบายดีมั๊ย')
sawaddee02('สมชาย')

def sawaddee02(name='คุณลูกค้าครับ'):   # บังคับให้ใส่ข้อมูล แทนด้วยค่า ค่า default
		print(f'{name} สบายดีมั๊ย')
sawaddee02()

########################
import turtle
tao = turtle.Pen()	#ดึงความสามรถปากกา
tao.shape('turtle')	#แปลงร่างเป็นเต่า
   
def Recrangle():	# วาดสี่เหลี่ยม
    for i in range(4):
        tao.fd(100)
        tao.left(90)
            
Recrangle()
tao.clear()

def Go(x,y):		#ย้ายตำแหน่ง
	tao.penup()		#ยกปากกาขึ้น
	tao.goto(x,y)
	tao.pendown()	#กดปากกา

Go(200,200)
Recrangle()
Go(150,150)
Recrangle()

def circle():	# วงกลม
    for i in range(10):
        tao.circle(50)
        tao.left(36)
	
Go(50,-50)
circle()
















	
	


		
