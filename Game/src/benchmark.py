import copy
import time
import tracemalloc
from src.solver import Solver

class Benchmark:
    def __init__(self):
        self.benchmark_results = []
        self.current_benchmark_index = 0
        self.peak_memory = 0
        self.algorithms = ["BFS", "DFS", "Dijkstra", "Greedy", "A*"]
        self.solvers = [
            (Solver.bfs, "BFS"),
            (Solver.dfs, "DFS"),
            (Solver.dijkstra, "Dijkstra"),
            (Solver.greedy, "Greedy"),
            (Solver.a_star, "A*"),
        ]
        self.memory_tracking = False 
        
    
    def toggle_memory_tracking(self):
        self.memory_tracking = not self.memory_tracking
        return self.memory_tracking
    
    def get_memory_tracking_status(self):
        return self.memory_tracking
        
   # Reset benchmark results and index
    def reset_results(self):
        self.benchmark_results.clear()
        self.current_benchmark_index = 0
        
    # Get the name of the current algorithm
    def get_current_algorithm(self):
        if 0 <= self.current_benchmark_index < len(self.algorithms):
            return self.algorithms[self.current_benchmark_index]
        return "Unknown"
    
     # Run benchmarks for all solvers
    def run_benchmark(self, checks, board, blocks):
        print("Starting benchmark...")
        checks["benchmark_started"] = True
        self.reset_results()
        
        # Execute all solvers in order
        for solver_func, name in self.solvers:
            print(f"Testing {name}...")
            self.current_benchmark_index = self.solvers.index((solver_func, name))
            temp_board = copy.deepcopy(board)
            temp_blocks = copy.deepcopy(blocks)
            start_time = time.time()            
            try:
                peak_memory_mb = "Not tracked"
                if self.memory_tracking:
                    tracemalloc.start()
                moves, nodes_explored = solver_func(temp_board, temp_blocks)
                if self.memory_tracking:
                    peak_memory = tracemalloc.get_traced_memory()[1]
                    print(f"Peak memory usage: {peak_memory / (1024 * 1024)} MB")
                    peak_memory_mb = peak_memory / (1024 * 1024)
                    tracemalloc.stop()
                    
                duration = time.time() - start_time
                
                
                if moves:
                    self.benchmark_results.append({
                        "algorithm": name,
                        "moves": len(moves),
                        "nodes_explored": nodes_explored,
                        "duration": round(duration, 3),
                        "peak_memory_mb": peak_memory_mb
                    })
                    
                else:
                    self.benchmark_results.append({
                        "algorithm": name,
                        "moves": "No solution",
                        "nodes_explored": "N/A",
                        "duration": round(duration, 3),
                        "peak_memory_mb": peak_memory_mb
                    })
                    
            except Exception as e:
                print(f"Error in {name}: {e}")
                self.benchmark_results.append({
                    "algorithm": name,
                    "moves": "err",
                    "nodes_explored": "err",
                    "duration":"err",
                    "peak_memory_mb": "err"
                })

        print("Benchmark complete!")
        checks["benchmark_finished"] = True