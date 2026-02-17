import fastf1
import matplotlib.pyplot as plt
import os

# Create cache folder if not exists
if not os.path.exists("cache"):
    os.makedirs("cache")

fastf1.Cache.enable_cache("cache")


def load_real_race(year=2023, race="Bahrain", driver="VER"):
    session = fastf1.get_session(year, race, "R")
    session.load()

    laps = session.laps.pick_driver(driver)

    lap_times = laps["LapTime"].dt.total_seconds()
    compounds = laps["Compound"]

    return lap_times, compounds


def plot_real_data(lap_times):
    laps = list(range(1, len(lap_times) + 1))

    plt.figure("Real F1 Lap Times")
    plt.plot(laps, lap_times)
    plt.xlabel("Lap Number")
    plt.ylabel("Lap Time (s)")
    plt.title("Real F1 Lap Times")
    plt.grid()

    plt.show()
