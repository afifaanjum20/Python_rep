from abc import ABC,abstractmethod

class Defence(ABC):
    def mat(self):
        print("euipment=materials")
    @abstractmethod
    def area(self):
        pass
class Airforce(Defence):
    def area(self):
        print("airforce area =Air")

class Navy(Defence):
    def area(self):
        print("navy area = Sea")

class Land(Defence):
    def area(self):
        print("Land area = Land")


        
# ar=Airforce()
# ar.area()
# ar.mat()
ld=Land()
ld.mat()
ld.area()

