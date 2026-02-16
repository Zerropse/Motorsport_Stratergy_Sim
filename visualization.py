import matplotlib.pyplot as plt

def plot_race(lap_times, grips, fuels):
    laps = list(range(1, len(lap_times) + 1))

    # 🪟 Window 1: Lap Time
    plt.figure("Lap Time")
    plt.plot(laps, lap_times)
    plt.xlabel("Lap Number")
    plt.ylabel("Lap Time (s)")
    plt.title("Lap Time vs Lap")
    plt.grid()

    # 🪟 Window 2: Tire Grip
    plt.figure("Tire Grip")
    plt.plot(laps, grips)
    plt.xlabel("Lap Number")
    plt.ylabel("Grip")
    plt.title("Tire Grip Degradation")
    plt.grid()

    # 🪟 Window 3: Fuel Load
    plt.figure("Fuel Load")
    plt.plot(laps, fuels)
    plt.xlabel("Lap Number")
    plt.ylabel("Fuel (kg)")
    plt.title("Fuel Load Over Race")
    plt.grid()

    # ✅ Show ALL windows together
    plt.show()
