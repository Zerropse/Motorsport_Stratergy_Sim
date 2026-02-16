class Race:
    def __init__(self, car, total_laps=50):
        self.car = car
        self.total_laps = total_laps
        self.lap_times = []
        self.total_time = 0

    def run(self):
        """
        Simulate the race
        """
        for lap in range(self.total_laps):
            lap_time = self.car.compute_lap_time()

            grip = self.car.tire.get_grip()
            fuel = self.car.fuel

            self.lap_times.append(lap_time)
            self.total_time += lap_time

            print(f"Lap {lap+1}: {lap_time:.2f}s | Grip={grip:.3f} | Fuel={fuel:.1f}")

            self.car.update()


    def summary(self):
        print("\n--- Race Summary ---")
        print(f"Total Time: {self.total_time:.2f}s")
        print(f"Average Lap: {self.total_time / self.total_laps:.2f}s")
