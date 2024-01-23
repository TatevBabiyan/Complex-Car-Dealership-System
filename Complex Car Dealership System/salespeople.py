from abc import ABC, abstractmethod
from cars import *
from customers import *

class Sales_Operations(ABC):
    @abstractmethod
    def manage_car_inventory(self, make):
        pass

    @abstractmethod
    def view_sales_history(self):
        pass


class Sales_People(Sales_Operations):

    def manage_car_inventory(self, make):
        manageinventory = []
        for car in carsdict['Electric Cars']:
            if make.lower() in car['Make'].lower():
                manageinventory.append(car)

        for car in carsdict['Hybrid Cars']:
            if make.lower() in car['Make'].lower():
                manageinventory.append(car)
        return f"The Car {manageinventory} you have purchased!"


    def view_sales_history(self):
        return Customer.purchased_cars
