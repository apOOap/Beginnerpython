class Car: # Class คุณสมบัติ ลักษณะเฉพาะ ยี่ห้อ สีรถ รุ่น

    brand = None 
    year = None 
    year = None 
    fuel = None 
    status = None 

    def __init__(self,brand='Toyota',year=2022,fuel=10,status=True): # ตั้งค่า default
        self.brand = brand
        self.year = year
        self.fuel = fuel
        self.status = True

    def checkstatus(self): 
        if self.status == True:            
            print(f'{self.brand} {self.year}ผ่านการทดสอบ')
        else:
            print(f'{self.brand} {self.year}ไม่ผ่านการทดสอบ')

    def drive(self):   
        print('กำลังทดสอบขับ')

if __name__ == '__main__':

    car01 =Car('Toyota','2022','50','True')
    car02 =Car('Benz','2020','30','False')

    car01.drive()
    car02.checkstatus()

   




    

   




    





    


    






    


    
    

    



