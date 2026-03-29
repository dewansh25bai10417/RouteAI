import heapq
import config

class AStarEngine:
    @staticmethod
    def get_heuristic(pos, goal):
        # Manhattan Distance formula
        return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])

    def solve(self, env):
        start = config.START_POINT
        goal = config.GOAL_POINT
        
        pq = [(0, start)]
        came_from = {start: None}
        cost_g = {start: 0}

        while pq:
            current = heapq.heappop(pq)[1]
            if current == goal: break

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                neighbor = (current[0] + dr, current[1] + dc)
                if env.is_valid_move(neighbor[0], neighbor[1]):
                    new_cost = cost_g[current] + 1
                    if neighbor not in cost_g or new_cost < cost_g[neighbor]:
                        cost_g[neighbor] = new_cost
                        f_score = new_cost + self.get_heuristic(neighbor, goal)
                        heapq.heappush(pq, (f_score, neighbor))
                        came_from[neighbor] = current
        return self.reconstruct_path(came_from, goal)

    def reconstruct_path(self, came_from, goal):
        path = []
        curr = goal
        while curr:
            path.append(curr)
            curr = came_from.get(curr)
        return path[::-1]
