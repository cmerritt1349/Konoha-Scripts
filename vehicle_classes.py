class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display(self):
        print("\n--- Vehicle Information ---")
        print(f"Vehicle type: {self.vehicle_type}")
        print(f"Year:         {self.year}")
        print(f"Make:         {self.make}")
        print(f"Model:        {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")
        print("---------------------------")

# Get user input
print("Welcome! Please enter your car's information.")

year = input("Enter the year: ")
make = input("Enter the make: ")
model = input("Enter the model: ")
doors = input("Enter the number of doors (2 or 4): ")
roof = input("Enter the type of roof (solid or sun roof): ")

# Create Automobile object - vehicle type is always "car"
my_car = Automobile("car", year, make, model, doors, roof)

# Display the result
my_car.display()