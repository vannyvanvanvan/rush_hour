import copy
import time
from src.solver import Solver
import src.setup as setup

def run_beachmark(checks):
    print("Starting benchmark...")
    solvers = [
        (Solver.bfs, "BFS"),
        (Solver.dfs, "DFS"),
        
        (Solver.dijkstra, "Dijkstra"),
        (Solver.greedy, "Greedy"),
        (Solver.a_star, "A*"),
    ]
    
    # Signal that benchmarking has started
    checks["beachmark_started"] = True
    
    # Reset results when starting new benchmark
    setup.beachmark_results.clear()
    setup.current_beachmark_index = 0
    
    # Exerute all solvers in order
    for solver_func, name in solvers:
        print(f"Testing {name}...")
        # Updating the index
        setup.current_beachmark_index = solvers.index((solver_func, name))
        #time.sleep(0.1)
        
        start_time = time.time()
        
        try:
            # Creating a fresh copies for each of the solver
            temp_board = copy.deepcopy(setup.board)
            temp_blocks = copy.deepcopy(setup.blocks)
            
            moves = solver_func(temp_board, temp_blocks)
            duration = time.time() - start_time
            
            if moves:
                setup.beachmark_results.append({
                    "algorithm": name,
                    "moves": len(moves),
                    "duration": round(duration, 3)
                })
            else:
                setup.beachmark_results.append({
                    "algorithm": name,
                    "moves": "No solution",
                    "duration": round(duration, 3)
                })
                
        except Exception as e:
            print(f"Error in {name}: {e}")
            setup.beachmark_results.append({
                "algorithm": name,
                "moves": "Failed",
                "duration": "N/A"
            })

    print("Benchmark complete!")
    checks["beachmark_finished"] = True