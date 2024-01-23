from descriptor import Descriptor

carsdict = {}

class Electric_Cars:
    make = Descriptor()
    model = Descriptor()
    price = Descriptor()

    def __init__(self):
        self._make = ['Fiat', 'Mercedes-Benz', 'Volvo']
        self._model = ['500', 'EQS', 'XC40 Recharge']
        self._price = [15000, 34000, 54000]

    def electric_cars(self):
        carsdict['Electric Cars'] = []
        for make, model, price in zip(self._make, self._model, self._price):
            car_info = {"Make": make, "Model": model, "Price": f'{price}$'}
            carsdict['Electric Cars'].append(car_info)
        return carsdict


class Hybrid_Cars:
    make = Descriptor()
    model = Descriptor()
    price = Descriptor()

    def __init__(self):
        self._make = ['Toyota', 'Kia', 'Chrysler']
        self._model = ['Prius', 'Sportage Hybrid', 'Pacifica Hybrid']
        self._price = [15000, 34000, 54000]

    def hybrid_cars(self):
        carsdict['Hybrid Cars'] = []
        for make, model, price in zip(self._make, self._model, self._price):
            car_info = {"Make": make, "Model": model, "Price": f'{price}$'}
            carsdict['Hybrid Cars'].append(car_info)
        return carsdict
