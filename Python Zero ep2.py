import tkinter
import time
import math

GUI = tkinter.Tk()
name = 'Supachai'   # sting
lastname = 'Mahnmahy'   # sting
fullname = '{} {}'.format(name,lastname)

print('{} {}'.format(name,lastname))

print('ชื่อ {} นามสกุล {}'.format(name,lastname))
print('My name is {} {}'.format(name,lastname))

print(f'{name} {lastname}') # เท่สุด
print(f'ผมชื่อ {name} นามสกุล {lastname} ครับผม')

age = 15 # int
grade = 3.5 # float
print(f'อายุ {age} เกรดเฉลี่ย {grade:.2f} ') # ทศนิยม 2 ตำแหน่ง

for atk in range(21): # ตรวจ ATK จำนวน 20 คน
    print('ตรวจต ATK คนที่ {}'.format(atk))

atktest = 25    # ตรวจคนไข้ไปเรื่อยๆ จนเข้าเงื่อนไข
count = 0   # จำนวนรอบที่เติม
while atktest > 0:  # ถ้า atktest มากกว่า 0 ชิ้น
    print('เครื่องตรวจ ATK เหลือจำนวน {} ชิ้น'.format(atktest))
    atktest = atktest - 1 # หลังตรวจลบออก 1 ชิ้น
#time.sleep (0.5) 

    if atktest < 10 and count != 3: # ถ้า atktest เหลือ 10 ให้เติมได้ 3 รอบ
       atktest = atktest + 15  # ให้ใส่เพิ่มไป 15 ชิ้น
       print('เจ้าหน้าที่มาเติมอีก 15 ชิ้น')
       count = count + 1
       print('เจ้าหน้าที่เบิกเพิ่มไป {} รอบ'.format(count))    
    time.sleep (0.5) 

















