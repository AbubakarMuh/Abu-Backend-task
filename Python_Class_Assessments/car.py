'''
Question 1:
Write a python class Car with attribute for brand and color, and a method 
start_engine that prints "Engine Started"
'''

class Car:
    
    def __init__(self, brand , colour):
        self.brand = brand
        self.colour = colour
        
    def start_engine(self):
        print (f"Engine Started successfully")

car_brand = Car("Lexus", "Ash")
print(f"Car brand type is: {car_brand.brand}")
print(f"Car color type is: {car_brand.colour}")
car_brand.start_engine()



# To run my code: python3 Python_Class_Assessment/car.py