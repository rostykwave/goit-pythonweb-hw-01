from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, make, model, region_spec):
        self.make = make
        self.model = model
        self.region_spec = region_spec

    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model} ({self.region_spec}): Engine started")

class Motorcycle(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model} ({self.region_spec}): Motor started")

class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model):
        pass

    @abstractmethod
    def create_motorcycle(self, make, model):
        pass

class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "US Spec")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "US Spec")

class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "EU Spec")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "EU Spec")

if __name__ == "__main__":
    us_factory = USVehicleFactory()
    eu_factory = EUVehicleFactory()

    us_car = us_factory.create_car("Ford", "Mustang")
    us_car.start_engine()

    us_motorcycle = us_factory.create_motorcycle("Harley-Davidson", "Sportster")
    us_motorcycle.start_engine()

    eu_car = eu_factory.create_car("Toyota", "Corolla")
    eu_car.start_engine()

    eu_motorcycle = eu_factory.create_motorcycle("Ducati", "Panigale")
    eu_motorcycle.start_engine()