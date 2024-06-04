class Car():
   def __init__(self,make,model,year):
       self.make = make
       self.model = model
       self.year = year
       self.mileage = 0

   def describe(self):
       print(self.year+' '+self.make+' '+self.model)

   def get_mileage(self):
       print("这个车已经跑了"+str(self.mileage)+"公里！")

   def set_mileage(self,mileage):
       if self.mileage<mileage:
           self.mileage = mileage

   def add_mileage(self,mileage):
       if mileage>=0:
           self.mileage += mileage

car1 = Car('奥迪','K1','2010')
car1.describe()
car1.get_mileage()
##if car1.mileage <100:
##    car1.mileage=100
car1.set_mileage(100)
car1.set_mileage(50)
car1.get_mileage()
car1.add_mileage(10)
car1.get_mileage()