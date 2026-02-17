class Car:
    def __init__(self, tire, fuel=100):
        self.tire = tire
        self.fuel = fuel  # kg
        self.base_time = 90  # seconds

    def compute_lap_time(self):
        grip = self.tire.get_grip()

        fuel_penalty = self.fuel * 0.03
        grip_bonus = grip * 2

        lap_time = self.base_time + fuel_penalty - grip_bonus
        return lap_time

    def update(self):
        self.tire.update()

        self.fuel -= 2
        if self.fuel < 0:
            self.fuel = 0
