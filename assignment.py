# TODO 1: Delete this and put a Doc String


from abc import ABC, abstractmethod


# TODO 2: Create an Abstract class called Rider with a ride and riders abstract method
# Note: It is a child class of ABC
class Rider(ABC):
    pass

# TODO 3: Create a class called Bicycle that implements Rider
# for ride method, it should return the string 'Human powered, not enclosed'
# for riders method, it should return the string '1 or 2 if tandem or a daredevil'
class Bicycle(Rider):
    pass


# TODO 4: Create a class called Motorcycle that implements Rider
# for ride method, it should return the string 'Engine powered, not enclosed'
# for riders method, it should return the string '1 or 2'
class Motorcycle(Rider):
    pass


# TODO 5: Create a class called Car that implements Rider
# for ride method, it should return the string 'Engine powered, enclosed'
# for riders method, it should return the string '1 plus comfortably'
class Car(Rider):
    pass



# Driver
if __name__ == "__main__":
    print("Creating Bicycle")
    bicycle = Bicycle()
    print(bicycle.ride())
    print(bicycle.riders())

    print("Creating Motorcycle")
    motorcycle = Motorcycle()
    print(motorcycle.ride())
    print(motorcycle.riders())

    print("Creating Car")
    car = Car()
    print(car.ride())
    print(car.riders())