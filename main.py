from tire import Tire
from car import Car

tire = Tire("soft")
car = Car(tire, fuel=100)

for lap in range(10):
    lap_time = car.compute_lap_time()
    
    print(f"Lap {lap+1}: Time = {lap_time:.2f}s | Grip = {tire.get_grip():.3f} | Fuel = {car.fuel}")

    car.update()
