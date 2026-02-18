<h1 align="center">🏁 MOTORSPORT STRATEGY SIMULATOR</h1>

<p align="center">
  <b>Race Strategy Engine • Performance Modeling • Telemetry Simulation</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/F1-INSPIRED-E10600?style=for-the-badge">
  <img src="https://img.shields.io/badge/PYTHON-3.x-black?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/STATUS-RACE_READY-success?style=for-the-badge">
</p>

---

## 🟥 SYSTEM OVERVIEW

A high-performance **race strategy simulation system** inspired by Formula 1 engineering workflows.

This engine models:
- Tire degradation dynamics  
- Fuel load impact  
- Lap time performance  
- Pit stop strategy optimization  

The system evaluates multiple strategies and outputs the **fastest race configuration**.

---

## 🏎️ PERFORMANCE MODEL

### 🛞 Tire Dynamics
- Compound types: **SOFT / MEDIUM / HARD**
- Grip decay over race distance
- Performance reset after pit stop

### ⛽ Fuel Load System
- Progressive fuel burn
- Direct impact on lap time

### ⏱️ Lap Time Engine
lap_time = base_time + fuel_penalty - grip_bonus


### 🛠️ Strategy Simulation
- 0 STOP
- 1 STOP
- 2 STOP  
→ Evaluates total race time  
→ Selects optimal strategy  

---

## 📊 TELEMETRY OUTPUT

The system generates real-time race telemetry:

- 📈 Lap Time Evolution  
- 🛞 Tire Grip Degradation  
- ⛽ Fuel Consumption Curve  

---
## 📁 ARCHITECTURE

```bash
motorsport_strategy_sim/
│
├── tire.py            # Tire physics model
├── car.py             # Vehicle performance model
├── strategy.py        # Strategy + pit logic
├── visualization.py   # Telemetry visualization
├── main.py            # Execution engine
```
---

## ⚙️ DEPLOYMENT
```bash
git clone https://github.com/Zerropse/Motorsport_Stratergy_Sim.git
cd Motorsport_Stratergy_Sim
pip install matplotlib
```
---
## ▶️ EXECUTION
```bash 
python3 main.py
```
---

## 🏁 RACE OUTPUT
--- STRATEGY ANALYSIS ---
0 STOP:   XXXX s
1 STOP:   XXXX s
2 STOP:   XXXX s

🏆 OPTIMAL STRATEGY: 1-STOP
---

## 🧠 ENGINEERING INSIGHT

- Early laps → fuel-limited performance  
- Mid stint → peak lap times  
- Late stint → tire degradation impact  
- Pit stop → performance reset vs time loss tradeoff  

---

## 🔥 FUTURE DEVELOPMENT

- 🌧️ Dynamic weather modeling  
- 🚨 Safety car simulation  
- 📡 Real-world telemetry integration  
- 🌐 Interactive strategy dashboard  
- 🤖 AI-based strategy optimization  

---

## 👨‍💻 DRIVER / DEVELOPER

Kush Singh
AI/ML Engineer • Full Stack Developer • Motorsport Enthusiast

“Data decides races.”
---
## 👨‍💻 IMAGES OF THE PROJECT RESULTS
The Data Result.
<p align="center">
  <img width="1029" height="583" alt="Table_Strat" src="https://github.com/user-attachments/assets/ca10de64-3eb7-4148-bef2-1b1c09db8a62" />
  <img width="287" height="179" alt="Result" src="https://github.com/user-attachments/assets/ed268090-387e-4506-b62d-67a09f7a17a8" />
</p>
The Graphs.
<p align="center">
  <img width="641" height="482" alt="lap_time" src="https://github.com/user-attachments/assets/36b41ac5-8776-465b-86a5-df4cc080d361" />
  <img width="638" height="506" alt="grip" src="https://github.com/user-attachments/assets/efd02965-6e34-4a3e-8764-9f3e7cae857d" />
  <img width="640" height="479" alt="fuel" src="https://github.com/user-attachments/assets/14b158ba-5df3-4516-9643-b4ea17773d88" />
</p>

