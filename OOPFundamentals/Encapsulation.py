"""
Notes taken from: https://algomaster.io/learn/lld
Encapsulation = Data hiding + Controlled access 
Example: Payment Processor

In this example, a PaymentProcessor class accepts a card number and 
amount, but internally masks the card number to protect user privacy. 
Again, encapsulation allows us to hide implementation details while 
offering a clean interface.
"""

class PaymentProcessor:
    def __init__(self, card_number, amount):
        self.__card_number = self.__mask_card_number(card_number)
        self.__amount = amount
    
    def __mask_card_number(self, card_number):
       return "****-****-****-" + card_number[-4:]

    def process_payment(self):
       print(f"Processing payment of {self.__amount} for card {self.__card_number}")


if __name__ == "__main__":
   payment = PaymentProcessor("1234567812345678", 550.00)
   payment.process_payment()

