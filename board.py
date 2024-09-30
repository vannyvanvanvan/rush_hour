class Board:
    def __init__(self):
        self.board = [
            ["X", "X", "X", "X", "X", "X"],
             ["X", "X", "X", "X", "X", "X"],
              ["X", "X", "X", "X", "X", "X"],
               ["X", "X", "X", "X", "X", "X"],
                ["X", "X", "X", "X", "X", "X"],
                 ["X", "X", "X", "X", "X", "X"],
        ]
        
    def display(self):
        #P rints the board to the console 
        for row in self.board:
            print(" ".join(row))
        print("============")  # Add a blank line after the board is printed
        
    
    def exit_check(self):
        # Exit check if the red car is in the array[5][3]
        exit_x = 5  
        exit_y = 2  
        return self.board[exit_y][exit_x] == "R"