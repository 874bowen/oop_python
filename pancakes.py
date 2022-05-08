class Pancake:
    def __init__(self, shape: str, thickness: float, diameter: float):
        print("A pancake created")
        # Run validations to the received args
        assert thickness >= 0, f"Thickness {thickness} is not greater than or equal to zero!"
        assert diameter >= 0, f"Diameter {diameter} is not greater than or equal to zero!"
        # Assign to self object
        self.shape = shape
        self.thickness = thickness
        self.diameter = diameter

    def cook(self):
        return "Pancake is being cooked"


pancakeOne = Pancake("Circle", 2.0, 4)
pancakeTwo = Pancake("Oval", 1.56, 3)
pancakeThree = Pancake("Circle", 2.0, 3.4)


print(pancakeOne.diameter)
print(pancakeTwo.cook())