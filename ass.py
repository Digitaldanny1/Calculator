# Assignment 1: Superhero Class with Inheritance
class Superhero:
    def __init__(self, name, power_level, secret_identity):
        self._name = name  # Encapsulation with protected attribute
        self._power_level = power_level
        self._secret_identity = secret_identity
        self._is_active = True

    def use_power(self):
        if self._is_active:
            return f"{self._name} is using their powers at level {self._power_level}!"
        return f"{self._name} is currently inactive."

    def reveal_identity(self):
        return f"{self._name}'s secret identity is {self._secret_identity}."

    def toggle_active_status(self):
        self._is_active = not self._is_active
        return f"{self._name} is now {'active' if self._is_active else 'inactive'}."

class FlyingSuperhero(Superhero):
    def __init__(self, name, power_level, secret_identity, flight_speed):
        super().__init__(name, power_level, secret_identity)
        self.flight_speed = flight_speed

    def use_power(self):  # Override parent method
        if self._is_active:
            return f"{self._name} soars through the sky at {self.flight_speed} mph!"
        return super().use_power()

# Activity 2: Polymorphism with Vehicles
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        pass  # To be overridden by subclasses

class Car(Vehicle):
    def move(self):
        return f"The {self.brand} {self.model} is driving on the road."

class Plane(Vehicle):
    def move(self):
        return f"The {self.brand} {self.model} is flying in the sky."

class Boat(Vehicle):
    def move(self):
        return f"The {self.brand} {self.model} is sailing on the water."

# Example usage
if __name__ == "__main__":
    # Assignment 1: Testing Superhero classes
    hero = Superhero("Captain Thunder", 85, "Alex Reed")
    flying_hero = FlyingSuperhero("Sky Blazer", 90, "Sam Carter", 300)
    
    print(hero.use_power())
    print(hero.reveal_identity())
    print(hero.toggle_active_status())
    print(hero.use_power())
    print(flying_hero.use_power())
    print(flying_hero.toggle_active_status())
    print(flying_hero.use_power())

    # Activity 2: Testing Vehicle polymorphism
    car = Car("Toyota", "Camry")
    plane = Plane("Boeing", "747")
    boat = Boat("Yamaha", "WaveRunner")
    
    vehicles = [car, plane, boat]
    for vehicle in vehicles:
        print(vehicle.move())