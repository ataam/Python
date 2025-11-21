class Vehicle:
    def __init__(self,producer, model, year):
        self.producer = producer
        self.model = model
        self.year = year
    def displayIfo(self):
        print(f"This is {self.producer} {self.model} {self.year} of production")

class Car(Vehicle):
    def __init__(self,producer,model,year,fuelTank = 100):
        super().__init__(producer,model,year)
        self.fuelTank = fuelTank
    def readyToStart(self):
        if self.fuelTank <= 30:
            print(f'Your level of fuel {self.fuelTank} is low, you need to refuel')
        else:
            print("lessgo")
    def displayIfo(self):
        print(f"This is {self.producer} {self.model} {self.year} of production, fuel tank is {self.fuelTank} % ")

class Bike(Car):
    def __init__(self,producer,model,year,fuelTank,type):
        super().__init__(producer, model, year,fuelTank)
        self.type = type
    def typeOfBike(self):
        print(f"Your bike {self.type}")
    def displayIfo(self):
        print(f"This is {self.producer} {self.model} {self.year} of production, you love {self.type}s bikes ")

class Plane(Vehicle):
    def __init__(self,producer,model,year,numberOfWings=2):
        super().__init__(producer, model, year)
        self.numberOfWings = numberOfWings
    def wingsOFPlane(self):
        if self.numberOfWings <= 1:
            print("Need to repair")
        else:
            print("Go into the sky")
    def readyToStart(self):
        if self.fuelTank <= 30:
            print(f'Your level of fuel {self.fuelTank} is low, you need to refuel')
        else:
            print("lessgo")
    def displayIfo(self):
        print(f"This is {self.producer} {self.model} {self.year} of production, you have {self.numberOfWings} wings ")

car1 = Car("Toyota","MX45",1965,29)
print(car1.__dict__)
car1.readyToStart()
car1.displayIfo()
print("------------------------------------------------")
bik1 = Bike("Yamaha","3rTwe",1997,31,"sport")
print(bik1.__dict__)
bik1.readyToStart()
bik1.typeOfBike()
bik1.displayIfo()
print("------------------------------------------------")
plane1 = Plane("Muga","3241Twe",2005,2)
print(plane1.__dict__)
plane1.wingsOFPlane()
plane1.displayIfo()


