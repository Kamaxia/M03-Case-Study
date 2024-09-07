class Vehicle():
    def __init__(self, type):
        self.type = type
    class Automobile():
        def __init__(self, year, make, model, doors, roof):
            self.year = year
            self.make = make
            self.model = model
            self.doors = doors
            self.roof = roof

vehType = input("Firstly, please enter the type of vehicle you are entering: ")
carYear = input("Next, enter the year your car was made: ") 
carMake = input("Next, enter the make of your car: ") 
carModel = input("Next, enter the model your car is: ") 
carDoors = input("Next, enter the number of doors your car has: ") 
carRoof = input("Next, enter the kind of roof you have: ")

userVeh = Vehicle(vehType)
userCar = userVeh.Automobile(carYear, carMake, carModel, carDoors, carRoof)

print("Vehicle type: ", userVeh.type)
print("Year: ", userCar.year)
print("Make: ", userCar.make)
print("Model: ", userCar.model)
print("Number of Doors: ", userCar.doors)
print("Type of Roof: ", userCar.roof)