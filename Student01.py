class Student: # Class คุณสมบัติ ลักษณะเฉพาะ ยี่ห้อ สีรถ รุ่น
    def __init__(self,name,lastname,gender,age): # ลักษณะหรือคุณสมบัติของนักเรียน
        self.name = name
        self.lastname = lastname
        self.gender = gender
        self.age = age

    # Method ขับ เบรค เลี้ยว 
    def study(self):    # (self) นำไปใช้งาน เ 
        print(f'{self.name} กำลังเรียนช่างเชื่อม')

    def testcode(self):    # (self) นำไปใช้
        print(f'{self.name} {self.lastname} กำลังเรียนเขียนโปรแกรม')

    def studyEng(self):    # (self) นำไปใช้
        print(f'{self.name} กำลังเรียนพิเศษภาษาอังกฤษ')

    def sir(self):
        if self.gender == 'ชาย':
            sir = 'ครับ'
            callme = 'ผม'
        else:
            sir = 'ค่ะ'
            callme = 'หนู'
        print(f'สวสัดี {sir} {callme} ชื่อ {self.name} {self.lastname}')



class SpStudent(Student):
    """ นักเรียนพิเศษ """
    def __init__(self,name,lastname,gender,age,parent):
        super(SpStudent, self).__init__(name,lastname,gender,age)
        self.parent = parent

    def hello(self, person='เพื่อน'):
        if  person == 'เพื่อน':
            print('เฮ้ย ว่างัยมึง..')
        else:
            print('เดินหนีดีกว่า ไม่อยากคุย')

       
        
class Teacher:
    def __init__(self,name,lastname,age,subject,gender): # ลักษณะหรือคุณสมบัติของครู
        self.name = name
        self.lastname = lastname
        self.age = age
        self.subject = subject 
        self.gender = gender 

    def teach(self):
        if self.gender == 'ชาย':
            sir = 'ครับ'
            callme = 'นาย'
        else:
            sir = 'ค่ะ'
            callme = 'ดิฉัน'
        print(f'สวัสดี {sir} {callme} ชื่อ {self.name} {self.lastname} สอนวิชา{self.subject}') 
       
    def lineup(self):
        print('นักเรียนตอนนี้เวลา 8.30 ได้แวลาเข้าเรียน')
                                     
if __name__ == '__main__':

    student1 =Student('โอเล่','มั่นหมาย','ชาย','21')
    student2 =Student('โอปอ','มั่นหมาย','หญิง','20')
    student3 =Student('โอนิว','มั่นหมาย','หญิง','10')
    Teacher1 =Teacher('Mark','Zuckerberg','57','ภาษาอังกฤษ','ชาย')
    Teacher2 =Teacher('สมศรี','ป้านทอง','25','ภาษาไทย','หญิง')
    Teacher3 =Teacher('Bill','Gateง','35','เขียนโปรแกรม Python','ชาย')

    print(student1.name)     # print name ของ นร.1
    #print(student1.lastname)
    #print(Teacher1.subject)  # print subject ของ ครู 1


    student1.study()       # นร.1 เรียกใช้ function study
    #Teacher1.teach()       # ครู 1 เรียกใช้ function teach
    #student1.study()       # นร.1 เรียกใช้ function study
    #Teacher3.teach()
    student3.testcode()
    #Teacher3.teach()

    student3.studyEng()    

    print('--------8.00-------')
    Teacher3.lineup()
    Teacher2.teach()
    print('ใครเป็นห้วหน้า')
    student1.sir()
    student2.sir()
    student3.sir()

   




    





    


    






    


    
    

    



