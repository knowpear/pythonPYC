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

car1 = Car('奥迪','K1','2010')
car1.describe()
car1.get_mileage()