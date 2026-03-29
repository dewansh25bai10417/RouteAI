import config

class WarehouseMap:
    def __init__(self):
        self.size = config.GRID_SIZE
        self.grid = [['.' for _ in range(self.size)] for _ in range(self.size)]
        self.obstacles = config.OBSTACLES

    def setup_environment(self):
        for r, c in self.obstacles:
            self.grid[r][c] = '#'
        self.grid[config.START_POINT[0]][config.START_POINT[1]] = 'S'
        self.grid[config.GOAL_POINT[0]][config.GOAL_POINT[1]] = 'G'
        
    def is_valid_move(self, r, c):
        return 0 <= r < self.size and 0 <= c < self.size and self.grid[r][c] != '#'
