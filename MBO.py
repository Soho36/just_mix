import random
class Config:
    grid_size = 6
class Gameboard:
    def show_board(self):
        board = [["•" for _ in range(Config.grid_size)] for _ in range(Config.grid_size)] # board as a list in the list
        # print("\n")
        print("  " + "|".join(list(map(str, range(1, Config.grid_size + 1))))) # board header
        n = 0       # board cells and row numbers
        for i in board:
            n += 1
            print(n, "|".join(i))
    def place_ship(self, ship):
        x, y = ship.startpont
        size = ship.size


gbrd = Gameboard()
gbrd.show_board()


class Ship:
    def __init__(self, size):   #initializes ship with a given size
        self.size = size
        self.startpoint = None
        self.orientation = None

    def generate_ship_randomly(self):       #generate starting point and orientation
        self.startpoint = (random.randint(1, Config.grid_size), random.randint(1, Config.grid_size))
        self.orientation = random.choice(["vertical", "horizontal"])

ship1 = Ship(3)
ship2 = Ship(2)
ship3 = Ship(1)
ship1.generate_ship_randomly()
ship2.generate_ship_randomly()
ship3.generate_ship_randomly()
