from pancakes import Pancake


class FlavoredPancake(Pancake):
    def __init__(self, shape: str, thickness: float, diameter: float, flavor: str):
        # Call to super to have all atrributes and methods
        super().__init__(shape, thickness, diameter)
        self.flavor = flavor


pancakeOne = FlavoredPancake("Circle", 2.0, 4, "Chocolate")
print(pancakeOne.flavor)