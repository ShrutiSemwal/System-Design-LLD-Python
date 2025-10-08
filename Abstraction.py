"""
Notes taken from: https://algomaster.io/learn/lld/encapsulation
1. Abstraction is about creating a simplified view of a system that highlights the essential features while suppressing the irrelevant details.

2. Although closely related, abstraction and encapsulation serve distinct purposes and work at different levels:
-->Encapsulation hides the internal state and data of an object while Abstraction hides the internal implementation logic of an object
-->Encapsulation focuses on how data is stored and protected while Abstraction focuses on what the object does (not how)

3. In Object-Oriented Programming (OOP), abstraction is implemented using language features that allow developers to define what an object 
should do without specifying how it does it.
a) Abstract Classes
b) Interfaces
c) Public APIs

"""

"""
ABSTRACT CLASSES EXAMPLE:

Abstract classes define a common blueprint for a family of classes. They may include:

-->Abstract methods (declared but not implemented)
-->Concrete methods (fully implemented)
-->Fields and constructors shared across subclasses
They are useful when:
-->Multiple classes share some behavior or state
-->You want to provide a default implementation but enforce subclasses to override specific behaviors
"""

from abc import ABC, abstractmethod

#Abstract class
class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand
    
    @abstractmethod
    def start(self):
        pass

    def display_brand(self):
        print("Brand:", self.brand)

#Subclass implementing the abstract method
class Car(Vehicle):
    def __init__(self, brand):
        super().__init__(brand)
    
    def start(self):
        print("Car is starting!")


"""
Interfaces EXAMPLE:

An interface is a pure abstraction. It defines a contract that a class 
must fulfill but doesn’t provide any implementation. Interfaces are ideal 
when you want to enforce a consistent API across unrelated classes.

In the example given below-
-->The interface Printable provides a uniform way to interact with all 
printers, regardless of how they implement the print() method.
-->It abstracts the printing logic from the user—they only care that the 
document gets printed.
"""

class Document:
    def __init__(self, content):
        self.__content = content
    
    def  get_content(self):
        return self.__content

class Printable(ABC):
    @abstractmethod
    def print(self, document):
        pass

#Concrete implementation of Printable
class PDFPrinter(Printable):
    def print(self, document):
        print("Printing PDF:", document.get_content())

class InkjetPrinter(Printable):
    def print(self, document):
        print("Printing via Inkjet:", document.get_content())


"""
Public APIs EXAMPLE:

Even when you're not using abstract classes or interfaces, abstraction 
is achieved through clean, public APIs that expose only what's necessary.

In the example given below-
-->Users call connect() and query()
-->Internal methods like openSocket() and authenticate() are 
abstracted away and hidden behind a simple interface
"""    

class DatabaseClient:
    def connect(self):
        # ...
        pass

    def query(self, sql):
        # ...
        pass

    def __open_socket(self):
        # internal logic
        pass

    def __authenticate(self):
        # internal logic
        pass

"""
Example: A Payment Gateway offering pay(), abstracting card verification and fraud checks
"""    

from abc import ABC, abstractmethod

# Abstract class representing a generic Payment Gateway
class PaymentGateway(ABC):

    # Template method — defines the general payment flow
    def pay(self, amount):
        self.verify_card()
        self.fraud_check()
        self.process_payment(amount)
        print("Payment completed successfully!\n")

    @abstractmethod
    def verify_card(self):
        """Subclasses must implement card verification logic"""
        pass

    @abstractmethod
    def fraud_check(self):
        """Subclasses must implement fraud detection logic"""
        pass

    @abstractmethod
    def process_payment(self, amount):
        """Subclasses must implement payment logic"""
        pass


# Concrete implementation of PaymentGateway for Credit Cards
class CreditCardPayment(PaymentGateway):

    def verify_card(self):
        print("Verifying credit card details...")

    def fraud_check(self):
        print("Performing fraud check using transaction history...")

    def process_payment(self, amount):
        print(f"Charging ₹{amount} to the credit card.")


# Another example: UPI Payment
class UPIPayment(PaymentGateway):

    def verify_card(self):
        print("Verifying UPI ID and linked bank account...")

    def fraud_check(self):
        print("Checking UPI transaction limits and risk flags...")

    def process_payment(self, amount):
        print(f"Transferring ₹{amount} via UPI.")


# Client code
if __name__ == "__main__":
    print("---- Credit Card Payment ----")
    payment1 = CreditCardPayment()
    payment1.pay(5000)

    print("---- UPI Payment ----")
    payment2 = UPIPayment()
    payment2.pay(750)
