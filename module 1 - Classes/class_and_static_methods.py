class Car:

    def __init__(self,brand,color,wheels,doors):
        self.brand = brand
        self.color = color
        self.wheels = wheels
        self.doors = doors

    @classmethod
    def create_mercedez_car(cls,color,wheels,doors):
        return cls('mercedez',color,wheels,doors)

    @staticmethod
    def print_properties(instance):
        properties = instance.__dict__
        for property in properties:
            print(property,':',properties[property])

car1 = Car(brand='ferrari',color='red',wheels='4',doors=2)
car2 = Car.create_mercedez_car(color='gray',wheels=4,doors=4)

Car.print_properties(car1)
print('-'*100)
Car.print_properties(car2)


