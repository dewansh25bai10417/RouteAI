from warehouse_env import WarehouseMap
from drone_engine import AStarEngine
import config

def run_simulation():
    print("--- Initializing Autonomous Logistics Drone System ---")
    
    # Initialize Environment
    env = WarehouseMap()
    env.setup_environment()
    
    # Initialize AI Engine
    engine = AStarEngine()
    path = engine.solve(env)
    
    # Overlay path on grid for visualization
    for r, c in path:
        if env.grid[r][c] not in ['S', 'G']:
            env.grid[r][c] = '*'
            
    # Display Result
    for row in env.grid:
        print(" ".join(row))
        
    print(f"\nOptimization Success!")
    print(f"Drone Path: {path}")
    print(f"Total Battery/Step Cost: {len(path)}")

if __name__ == "__main__":
    run_simulation()
