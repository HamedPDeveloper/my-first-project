class Car:
    def __init__(self, model, max_speed, color, price):
        self.model = model
        self.max_speed = max_speed
        self.color = color
        self.price = price
        self.current_speed = 0

    def acc(self, value):
        self.current_speed += value
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

    def horn(self):
        print("Did Did")


class BMW(Car):
    def autopark(self):
        print("start auto park")


class Saipa(Car):
    def __init__(self, model, max_speed, color, price, air_bag):
        self.has_airbag = air_bag
        super(Saipa, self).__init__(model, max_speed, color, price)

    #override
    def horn(self):
        print("Bib Bib")

    def __str__(self):
        return "Saipa Motmaen"

    def __eq__(self, other):
        if not isinstance(other, Saipa):
            return False
        return self.model == other.model

    def __gt__(self, other):
        if (self.max_speed > other.max_speed):
            return True
        else:
            return False

    def __hash__(self):
        return 3*len(self.model)+self.max_speed//2

    def __getitem__(self, item):
        if item=='model':
            return self.model
class Ford(Car):
    pass


if __name__ == '__main__':
    s1 = Saipa("111", 400, 'white', 4000, True)
    s3 = Saipa("111", 200, 'white', 4000, True)
    s2 = Saipa("131", 350, 'black', 200000, True)
    print(s1 > s2)
    cars = set()
    cars.add(s1)
    cars.add(s2)
    cars.add(s3)
    print(s1.model)
    print(s1['model'])

