class Tire:
    def __init__(self, compound="medium"):
        self.compound = compound.lower()
        self.age = 0

        if self.compound == "soft":
            self.base_grip = 1.0
            self.deg_rate = 0.05
        elif self.compound == "medium":
            self.base_grip = 0.9
            self.deg_rate = 0.03
        elif self.compound == "hard":
            self.base_grip = 0.8
            self.deg_rate = 0.015
        else:
            raise ValueError("Invalid compound")

    def get_grip(self):
        grip = self.base_grip - (self.age * self.deg_rate)
        return max(grip, 0.5)

    def update(self):
        self.age += 1
