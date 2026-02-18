from strategy import StrategySimulator
from visualization import plot_race


def run_all_strategies():
    sim = StrategySimulator(total_laps=30)

    print("\n--- 0 STOP STRATEGY ---")
    time_0, _, _, _ = sim.simulate(
        pit_laps=[],
        compound_sequence=["medium"]
    )
    

    print("\n--- 1 STOP STRATEGY ---")
    time_1, lap_times_1, grips_1, fuels_1 = sim.simulate(
        pit_laps=[15],
        compound_sequence=["medium", "hard"]
    )

    print("\n--- 2 STOP STRATEGY ---")
    time_2, _, _, _ = sim.simulate(
        pit_laps=[10, 20],
        compound_sequence=["soft", "medium", "hard"]
    )

    print("\n--- FINAL RESULTS ---")
    print(f"0 Stop Time: {time_0:.2f}s")
    print(f"1 Stop Time: {time_1:.2f}s")
    print(f"2 Stop Time: {time_2:.2f}s")

    results = {
        "0-stop": time_0,
        "1-stop": time_1,
        "2-stop": time_2
    }

    best = min(results, key=results.get)

    print(f"\n🏆 Best Strategy: {best} ({results[best]:.2f}s)")

    return lap_times_1, grips_1, fuels_1


def main():
    lap_times, grips, fuels = run_all_strategies()

    print("\n📊 Plotting telemetry...")
    plot_race(lap_times, grips, fuels)


if __name__ == "__main__":
    main()
