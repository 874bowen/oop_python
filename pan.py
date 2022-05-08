class Pancake:
    number_of_pancakes = 0

    def __init__(self):
        print("I am constructed")

    def add_pancake(self):
        self.number_of_pancakes = self.number_of_pancakes + 1
        print("Number of pancakes now ", self.number_of_pancakes)

    def __del__(self):
        print("I am destroyed")


pancakeOne = Pancake()
pancakeTwo = Pancake()
pancakeThree = Pancake()
pancakeOne.add_pancake()
pancakeOne.add_pancake()
pancakeOne.add_pancake()