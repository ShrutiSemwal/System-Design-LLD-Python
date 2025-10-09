"""
Notes taken from: https://algomaster.io/learn/lld

1. Inheritance enables code reuse by letting you define common logic in a base class and then extend or specialize it in multiple derived classes.

2. When a class inherits from another:

-->The subclass inherits all non-private fields and methods of the superclass.
-->The subclass can override inherited methods to provide a different implementation.
-->The subclass can also extend the superclass by adding new fields and methods.
-->This allows for both reuse and customization.

3. Use inheritance when:

-->There is a clear "is-a" relationship
-->The parent class defines common behavior that should be shared
-->The child class does not violate the behavior expected from the parent

4. Avoid inheritance when:

-->The relationship is more of a "has-a" or "uses-a" (prefer composition)
-->You want to combine behaviors dynamically (use interfaces or strategy pattern)
-->You need flexibility or runtime switching between behaviors
"""

"""
Example: Car Hierarchy

"""

class Car:
    def __init__(self):
        self.make = None
        self.model = None
    
    def start_engine(self):
        print("Engine Started")

    def stop_engine(self):
        print("Engine Stopped")

#Specialized type of cars--> inherit the make, model, start_engine() and stop_engine()

class ElectricCar(Car):
    def charge_batter(self):
        print("Battery charging")

class GasCar(Car):
    def fill_tank(self):
        print("Filling gas tank")