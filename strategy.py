from tire import Tire
from car import Car

class StrategySimulator:
    def __init__(self, total_laps=30, pit_loss=20):
        self.total_laps = total_laps
        self.pit_loss = pit_loss

    def simulate(self, pit_laps=[], compound_sequence=["medium"]):

        tire = Tire(compound_sequence[0])
        car = Car(tire, fuel=100)

        total_time = 0
        tire_index = 0

        lap_times = []
        grips = []
        fuels = []

        for lap in range(1, self.total_laps + 1):

            # PIT STOP
            if lap in pit_laps:
                total_time += self.pit_loss

                tire_index += 1
                new_compound = compound_sequence[tire_index]
                car.tire = Tire(new_compound)

                print(f"\nLap {lap}: 🛠️ PIT STOP → {new_compound.upper()} (+{self.pit_loss}s)\n")

            # DATA
            grip = car.tire.get_grip()
            fuel = car.fuel
            lap_time = car.compute_lap_time()

            # STORE
            lap_times.append(lap_time)
            grips.append(grip)
            fuels.append(fuel)

            total_time += lap_time

            print(f"Lap {lap}: {lap_time:.2f}s | Grip={grip:.3f} | Fuel={fuel:.1f}")

            car.update()

        return total_time, lap_times, grips, fuels
