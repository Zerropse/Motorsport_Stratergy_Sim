<h1 align="center">🏁 Motorsport Strategy Simulator</h1>

<p align="center">
  <b>🏎️ Race Strategy • Tire Modeling • Fuel Simulation • Data Visualization</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Matplotlib-Visualization-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge">
</p>

---

## 🚀 Overview

The **Motorsport Strategy Simulator** is a Python project that models real-world racing dynamics inspired by Formula 1.

It simulates:
- Tire degradation  
- Fuel consumption  
- Pit stop strategies  

and determines the **optimal race strategy** based on total race time.

---

## 🧠 Core Features

### 🛞 Tire Degradation Model
- Supports **Soft, Medium, Hard compounds**
- Grip decreases over laps
- Different degradation rates per compound

### ⛽ Fuel Model
- Fuel decreases every lap
- Higher fuel = slower lap times

### 🏁 Race Simulation
- Multi-lap race engine
- Dynamic lap time calculation
- Realistic performance trends

### 🛠️ Strategy Engine
- 0-stop strategy  
- 1-stop strategy  
- 2-stop strategy  
- Automatic **best strategy selection**

### 📊 Telemetry Visualization
- 📈 Lap Time vs Lap  
- 🛞 Tire Grip Degradation  
- ⛽ Fuel Load  

---

## 🧮 Simulation Formula

lap_time = base_time + fuel_penalty - grip_bonus


- Fuel penalty increases lap time  
- Grip bonus reduces lap time  
- Tire degradation reduces grip over time  

---

## 📁 Project Structure

motorsport_strategy_sim/
│
├── tire.py
├── car.py
├── strategy.py
├── visualization.py
├── main.py
└── README.md


---

## ⚙️ Installation

```bash
git clone https://github.com/Zerropse/Motorsport_Stratergy_Sim.git
cd Motorsport_Stratergy_Sim
pip install matplotlib
▶️ Run
python3 main.py
📊 Output
Terminal
Lap-by-lap simulation

Tire grip + fuel data

Pit stop events

Strategy comparison

Graphs
📈 Lap Time

🛞 Tire Grip

⛽ Fuel Load

🏆 Example Result
🏆 Best Strategy: 1-stop
🔥 Why This Project Stands Out
Combines physics + data modeling

Demonstrates optimization thinking

Simulates real motorsport decision-making

Structured like a real engineering system

🚀 Future Improvements
🌧️ Weather simulation

🚨 Safety car logic

📡 Real telemetry integration

🌐 Streamlit dashboard

🤖 AI-based strategy prediction

👨‍💻 Author
Kush Singh
🏎️ Motorsport Enthusiast
💻 AI/ML Engineer
🎯 Aspiring Race Strategy Engineer

<p align="center"> ⭐ If you like this project, consider giving it a star! </p> ```
