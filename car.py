class Car:
    def __init__(self, tire, fuel=100):
        self.tire = tire
        self.fuel = fuel  # in kg
        self.base_time = 90  # base lap time in seconds

    def compute_lap_time(self):
        """
        Calculate lap time based on fuel and tire grip
        """
        grip = self.tire.get_grip()

        fuel_penalty = self.fuel * 0.03
        grip_bonus = grip * 2

        lap_time = self.base_time + fuel_penalty - grip_bonus

        return lap_time

    def update(self):
        """
        Update car state after each lap
        """
        self.tire.update()

        # fuel burn per lap
        self.fuel -= 5  # burn 5 kg of fuel per lap
        if self.fuel < 0:
            self.fuel = 0
