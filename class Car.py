class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} едет.')

    def stop(self):
        print(f'{self.name} стоит.')

    def turn(self, direction):
        print(f'Машина повернула {direction}.')

    def show_speed(self):
        print(f'{self.name} едет со скоростью {self.speed} км/час.')


class TownCar(Car):

    def show_speed(self):
        print(f'{self.name} едет со скоростью {self.speed} - CКОРОСТЬ ПРЕВЫШЕНА!' if self.speed > 60\
              else f"{self.name} едет со скоростью {self.speed}.")


class WorkCar(Car):

    def show_speed(self):
        print(f'{self.name} едет со скоростью {self.speed} - CКОРОСТЬ ПРЕВЫШЕНА!' if self.speed > 60\
              else f"{self.name} едет со скоростью {self.speed}.")

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed,color, name, is_police )


class SportCar(Car):
    def go(self):
        print(f'{self.name} мчится.')

towncar = TownCar(80, 'red', 'Toyota')
towncar.show_speed()
