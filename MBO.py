



class Gameboard:
    def __init__(self, grid_size):
       self.grid_size = grid_size
    def show_board(self):
        grid_size = 6
        board = [["•" for _ in range(grid_size)] for _ in range(grid_size)]
        print(board)
        print("\n")
        print(" |" + "|".join(str(i) for i in range(1, grid_size + 1)) + "|")  # Column numbers

        for i, row in enumerate(board, start=1):
            print(f"{i}|{'|'.join(row)}|")
gb = Gameboard(6)
gb.show_board()

# class Ship:
#     def __init__(self, position, coords, ):
