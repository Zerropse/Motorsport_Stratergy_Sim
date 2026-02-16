from tire import Tire
from car import Car
from race import Race

class StrategySimulator:
    def __init__(self, total_laps=30, pit_loss=20):
        self.total_laps = total_laps
        self.pit_loss = pit_loss

    def simulate(self, pit_laps=[], compound_sequence=["medium"]):
        """
        Simulate a race with pit stops
        """

        tire = Tire(compound_sequence[0])
        car = Car(tire, fuel=100)

        total_time = 0
        tire_index = 0

        for lap in range(1, self.total_laps + 1):

            # PIT STOP
            if lap in pit_laps:
                total_time += self.pit_loss

                tire_index += 1
                new_compound = compound_sequence[tire_index]
                car.tire = Tire(new_compound)

                print(f"\nLap {lap}: 🛠️ PIT STOP → New {new_compound.upper()} tires (+{self.pit_loss}s)\n")

            # GET DATA BEFORE UPDATE
            grip = car.tire.get_grip()
            fuel = car.fuel

            # LAP TIME
            lap_time = car.compute_lap_time()
            total_time += lap_time

            print(f"Lap {lap}: {lap_time:.2f}s | Grip={grip:.3f} | Fuel={fuel:.1f}")

            # UPDATE AFTER LAP
            car.update()
            
        return total_time

