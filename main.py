from tire import Tire
from car import Car
from race import Race
from strategy import StrategySimulator

tire = Tire("medium")
car = Car(tire, fuel=100)

race = Race(car, total_laps=30)

race.run()
race.summary()

sim = StrategySimulator(total_laps=30)

print("\n--- 0 STOP STRATEGY ---")
time_0 = sim.simulate(pit_laps=[], compound_sequence=["medium"])

print("\n--- 1 STOP STRATEGY ---")
time_1 = sim.simulate(pit_laps=[15], compound_sequence=["medium", "hard"])

print("\n--- 2 STOP STRATEGY ---")
time_2 = sim.simulate(pit_laps=[10, 20], compound_sequence=["soft", "medium", "hard"])

print("\n--- RESULTS ---")
print(f"0 Stop Time: {time_0:.2f}")
print(f"1 Stop Time: {time_1:.2f}")
print(f"2 Stop Time: {time_2:.2f}")
