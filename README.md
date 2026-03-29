# RouteAI
🛸 Autonomous Logistics Drone: AI Navigation System

A multi-layered AI agent designed to solve high-frequency pathfinding problems in industrial warehouse environments. This system implements Informed Search (A)* to achieve a rational, cost-effective navigation path from a Start node (Charging Dock) to a Goal node (Package Drop-off).
🏗️ System Architecture

This project is built using a Modular Design Pattern, separating the environment logic from the heuristic search engine to ensure scalability and clean code standards.
File	Component	Responsibility
config.py	Global Settings	Defines grid dimensions, static obstacles, and coordinate constants.
warehouse_env.py	Environment Layer	Manages the 2D grid state, obstacle mapping, and move validation.
drone_engine.py	Heuristic Engine	Implements the A* algorithm and Manhattan Distance math.
main_runner.py	System Controller	Orchestrates the simulation, triggers the solver, and renders the output.
🔬 Mathematical Framework

The agent operates as a Goal-Based Rational Agent. It evaluates every possible move using the weighted cost function:
f(n)=g(n)+h(n)

    g(n): The exact cost (steps taken) from the Start point to the current node n.

    h(n): The Heuristic—an estimated "Manhattan Distance" to the Goal, calculated as:
    ∣x1​−x2​∣+∣y1​−y2​∣

By combining these, the drone avoids "blind" searching (like BFS) and instead prioritizes nodes that mathematically minimize the total trip distance.
📊 Technical Results

    Algorithm Performance: Informed Search (A*).

    Search Space: 10x10 Grid (100 discrete nodes).

    Obstacle Handling: Static collision avoidance for non-passable shelf units (#).

    Path Optimality: The system guaranteed the shortest path with 100% accuracy during testing.

🚀 Deployment & Usage
1. Installation

No external libraries (like numpy or pandas) are required. The system runs on pure Standard Python 3.x.
2. Execution

Run the system controller to start the simulation:
Bash

python main_runner.py

3. Output Map Key

    S : Start Position (Logistics Dock)

    G : Goal Position (Delivery Target)

    # : Warehouse Shelves (Obstacles)

    * : Calculated Optimal Drone Path

Developer: [Friend's Name]

Reg No: [Friend's Registration Number]

Course: Introduction to Artificial Intelligence (AI)
