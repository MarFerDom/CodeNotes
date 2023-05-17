import factory
from dataclasses import dataclass


@dataclass
class chicken():

    name: str = "Suzy"
    eggs_per_day: str = '10'

    def do(self) -> None:
        print(f"{self.name} the chicken goes cluck with {self.eggs_per_day} eggs per day")



@dataclass
class cow():

    name: str = "Brumhilda"
    milk_per_day: str = '10'

    def do(self) -> None:
        print(f"{self.name} the cow goes moo with {self.milk_per_day} liters of milk per day")



@dataclass
class sheep():

    name: str = "Poly"
    whool_per_day: str = '100'

    def do(self) -> None:
        print(f"{self.name} the sheep goes beh with {self.whool_per_day} grams of whool per day")



def register() -> None:
    factory.registerAnimal('cow', cow)
    factory.registerAnimal('chicken', chicken)
    factory.registerAnimal('sheep', sheep)