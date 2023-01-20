# Python program demonstrate  
# abstract base class work   
from abc import ABC, abstractmethod  


class Car(ABC): 
    @abstractmethod 
    def mileage(self):   
        pass  
  
class Tesla(Car):   
    def mileage(self):   
        print("The mileage is 30kmph")   
class Suzuki(Car):   
    def mileage(self):   
        print("The mileage is 25kmph ")   
class Duster(Car):   
     def mileage(self):   
          print("The mileage is 24kmph ")   
  
class Renault(Car):
    def __init__(self):  
        print("You have to initiate/define the abstract method in this class! Other wise you get fucked up!")
    def mileage(self):   
          print("The mileage is 27kmph ") 
        
# Driver code   
t= Tesla ()   
t.mileage()   
  
r = Renault()   
r.mileage()   
  
s = Suzuki()   
s.mileage()   
d = Duster()   
d.mileage()  