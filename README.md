# RouteAI
#  RouteAI: AI Logistics Navigation System

A modular AI-driven pathfinding system designed for industrial warehouse optimization. This project simulates a **Goal-Based Rational Agent** that navigates a 10x10 grid to find the most efficient route from a Charging Dock to a Delivery Target.

---

## System Architecture
This project follows a professional **Modular Design Pattern**, separating environment logic from the search engine.

| File | Component | Responsibility |
| :--- | :--- | :--- |
| `config.py` | **Configuration** | Defines grid size, obstacle coordinates, and start/goal points. |
| `warehouse_env.py`| **Environment** | Manages the grid state and validates agent movement. |
| `drone_engine.py` | **AI Engine** | Implements the **A* Search Algorithm** and Manhattan Heuristics. |
| `main_runner.py`  | **Controller** | The execution script that runs the simulation and renders the map. |

---

## 🔬 How the AI "Thinks"
The agent utilizes **Informed Search (A*)** to prioritize paths that mathematically minimize travel distance. It evaluates every move using the function:

$$f(n) = g(n) + h(n)$$

* **$g(n)$**: The actual cost (steps) taken from the Start to the current position.
* **$h(n)$**: The **Manhattan Distance** heuristic, estimating the remaining distance to the Goal:
  $$|x_{goal} - x_n| + |y_{goal} - y_n|$$

---

## Getting Started

### 1. Prerequisites
Ensure you have **Python 3.x** installed. No external libraries (like `numpy`) are required as this uses standard Python data structures.

### 2. Running the Simulation
    Navigate to the project directory and run the controller:
    python main_runner.py
    Making sure all the files are in the same folder

# 3. Understanding the Output

    S : Start Point (Logistics Dock)

    G : Goal Point (Package Target)

    # : Static Obstacles (Warehouse Shelves)

    * : The Optimal Path calculated by the AI

Project Observations

    Optimality: The agent consistently finds the shortest path while avoiding all 11+ static obstacles.

    Efficiency: By using a heuristic, the agent reduces the search space significantly compared to uninformed methods like BFS.

    Rationality: The agent demonstrates "perfect rationality" within this discrete, static environment.

Developed by: [Friend's Name]

Reg No: [Friend's Registration Number]

Course: Introduction to AI | B.Tech AIML
