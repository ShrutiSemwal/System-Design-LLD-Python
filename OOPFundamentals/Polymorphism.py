"""
Notes taken from: https://algomaster.io/learn/lld

1. Polymorphism allows the same method name or interface to exhibit different behaviors depending on the object that is invoking it.

2. Polymorphism lets you call the same method on different objects, and have each object respond in its own way.

3. You write code that targets a common type, but the actual behavior is determined by the concrete implementation.

4. Why Polymorphism Matters
--> Encourages loose coupling: You interact with abstractions (interfaces or base classes), not specific implementations.
--> Enhances flexibility: You can introduce new behaviors without modifying existing code, supporting the Open/Closed Principle.
--> Promotes scalability: Systems can grow to support more features with minimal impact on existing code.
--> Enables extensibility: You can “plug in” new implementations without touching the core business logic.

"""
"""
TWO TYPES OF POLYMORPHISM:
"""
#1. Compile-time Polymorphism (Static Binding)

"""
Also known as method overloading, this occurs when:

-->You have multiple methods with the same name in the same class.
-->Each method has a different parameter list (number, type, or order).
-->The method to call is determined by the compiler at compile time.
"""

#Achieving similar behaviour using default arguments or type checking.
class Calculator:
    def add(self, *args):
        """
        Adds numbers. Supports:
        - 2 integers
        - 2 floats
        - 3 integers
        """
        if not args:
            raise ValueError("At least two numbers are required")
        return sum(args)

calc = Calculator()

print(calc.add(2, 3))
print(calc.add(2.5, 3.5))       
print(calc.add(1, 2, 3))

#2. Runtime Polymorphism (Dynamic Binding)
"""
Also known as method overriding, this happens when:

-->A subclass overrides a method defined in its superclass or interface.
-->The method to invoke is determined at runtime, based on the actual object type.
"""

#Designing a system that sends notifications (email, SMS, push notif.)

#Common Interface
from abc import ABC, abstractmethod

class NotificationSender(ABC):
    @abstractmethod
    def send_notification(self, message):
        pass

#Implementing it in multiple ways
class EmailSender(NotificationSender):
    def send_notification(self, message):
        print("Sending EMAIL:", message)

class SmsSender(NotificationSender):
    def send_notification(self, message):
        print("Sending SMS:", message)

class PushSender(NotificationSender):
    def send_notification(self, message):
        print("Sending PUSH notification:", message)
    
#Helper function (module-level, outside classes)
# def notify_user(sender, message):
#     sender.send_notification(message)

# NotificationService manages sending notifications
class NotificationService:
    def __init__(self, sender: NotificationSender):
        self.sender = sender  # Has-a relationship

    def notify_user(self, message):
        self.sender.send_notification(message)

#Usage
if __name__ == "__main__":
    email_sender = EmailSender()
    sms_sender = SmsSender()
    push_sender = PushSender()

    email_service = NotificationService(email_sender)
    sms_service = NotificationService(sms_sender)
    push_service = NotificationService(push_sender)

    email_service.notify_user("Your order has been shipped!")
    sms_service.notify_user("Your OTP is 123456")
    push_service.notify_user("Your Order is added to shipment!")