class car:
    def __init__(self,make,model):
        self.__make=make     #Private attribute
        self.model= model    # Public attribute
    def get_make(self):
        return self.__make

    def set_make(self,new_make):
        self.__make=new_make
# creating an instanceoi of the class
my_car=car("BMW","D120")

#Accesing public attribute
print("car model",my_car.model)

#Accesing private attribute using geter method

print("Car make",my_car.get_make())

#update the setter
my_car.set_make("Honda")
print("Update car make ",my_car.get_make())
