from cars import *
from descriptor import Descriptor

class Customer:
    name = Descriptor()
    contact_information = Descriptor()
    purchased_cars = []

    def __init__(self, name, contact_information):
        self._name = name
        self._contact_information = contact_information

    def register_as_user(self):
        if len(self._name) >= 5 and self._name.isalpha() and len(self._contact_information) == 9 and self._contact_information[0] == '0' and self._contact_information.isdigit():
            return "Successful Registration"
        raise ValueError("Enter Valid Data")

    def search_car(self, make):
        for car in carsdict['Electric Cars']:
            if make.lower() in car['Make'].lower():
                return car

        for car in carsdict['Hybrid Cars']:
            if make.lower() in car['Make'].lower():
                return car

    def purchase_car(self, make):
        for car in carsdict['Electric Cars']:
            if make.lower() in car['Make'].lower():
                Customer.purchased_cars.append(car)

        for car in carsdict['Hybrid Cars']:
            if make.lower() in car['Make'].lower():
                Customer.purchased_cars.append(car)

        return f"The Car you have purchased: {Customer.purchased_cars}"




