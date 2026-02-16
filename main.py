from tire import Tire

tire = Tire("soft")

for lap in range(10):
    print(f"Lap {lap+1}: Grip = {tire.get_grip():.3f}")
    tire.update()
