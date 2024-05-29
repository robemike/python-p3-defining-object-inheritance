from vehicle import Vehicle

class Car(Vehicle):
    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"
    pass

my_car = Car(24, 56)
print(my_car.wheel_size)
print(my_car.wheel_number)
print(my_car.fill_up_tank())
sound = my_car.go()
print(sound)