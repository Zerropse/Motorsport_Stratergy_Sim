# 🏁 Motorsport Strategy Simulator

A Python-based simulation of race strategy inspired by real-world motorsport (Formula 1).  
This project models tire degradation, fuel consumption, and pit stop strategies to determine the optimal race strategy.

---

## 🚀 Features

- 🛞 Tire degradation model (Soft, Medium, Hard)
- ⛽ Fuel consumption affecting lap time
- 🏁 Multi-lap race simulation
- 🛠️ Pit stop strategy system (0-stop, 1-stop, 2-stop)
- 🧠 Automatic best strategy selection
- 📊 Telemetry visualization:
  - Lap Time vs Lap
  - Tire Grip
  - Fuel Load

---

## 🧠 Simulation Logic

Lap time is calculated using:
lap_time = base_time + fuel_penalty - grip_bonus


- Fuel penalty increases lap time as fuel load increases  
- Grip bonus decreases lap time based on tire performance  
- Tire grip decreases over laps due to degradation  

---

## 📁 Project Structure

motorsport_strategy_sim/
│
├── tire.py # Tire model (grip & degradation)
├── car.py # Car model (fuel & lap time)
├── strategy.py # Race + pit stop strategy simulation
├── visualization.py # Graph plotting (matplotlib)
├── main.py # Entry point
└── README.md


---

## ⚙️ Installation

1. Clone the repository:

---

## ⚙️ Installation

1. Clone the repository:

git clone https://github.com/Zerropse/Motorsport_Stratergy_Sim.git
cd Motorsport_Stratergy_Sim

pip install matplotlib

▶️ Run the Project
python3 main.py


📊 Output
Terminal Output

Lap-by-lap simulation

Tire and fuel data

Pit stop events

Strategy comparison

Best strategy selection

Graphs

📈 Lap Time vs Lap

🛞 Tire Grip Degradation

⛽ Fuel Load Over Race
