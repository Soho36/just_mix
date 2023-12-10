from random import randint


class BoardExceptions(Exception):
    pass


class OutOfBoard(BoardExceptions):
    def __str__(self):
        return 'Вы стреляете за пределы доски, попробуйте снова!'


class BoardUsedException(BoardExceptions):
    def __str__(self):
        return 'Неправильное расположение корабля, попробуйте снова!'


class BoardUsed(BoardExceptions):
    def __str__(self):
        return 'Вы уже стреляли сюда, попробуйте снова!'


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Dot({self.x}, {self.y})"


class Battleship:
    def __init__(self, long, nose: Dot, napravlenie):
        self.long = long
        self.nose = nose
        self.napravlenie = napravlenie
        self.hp = long

    @property
    def dots(self):
        dots_list = []
        for i in range(self.long):
            if self.napravlenie == 1:
                x = self.nose.x + i
                y = self.nose.y
            else:
                x = self.nose.x
                y = self.nose.y + i
            dots_list.append(Dot(x, y))
        return dots_list

    def shooten(self, shot):
        return shot in self.dots


class Board:
    def __init__(self):
        self.table = [['•' for _ in range(6)] for _ in range(6)]
        self.ship_types = []
        self.hid = False
        self.counter_list = []
        self.dead = 0

    def __str__(self):
        res = ""
        res += "   | 1 | 2 | 3 | 4 | 5 | 6 |"
        for i, row in enumerate(self.table):
            res += f"\n{i + 1}  | " + " | ".join(row) + " |"

        if self.hid:
            res = res.replace('■', '•')
        return res

    def add_ship(self, ship):
        for d in ship.dots:
            if self.out(d) or d in self.counter_list:
                raise BoardUsedException

        for d in ship.dots:
            self.table[d.x][d.y] = '■'

        self.ship_types.append(ship)
        self.counter(ship)

    def counter(self, ship, hid=False):
        counter = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),   (0, 0),  (0, 1),
                  (1, -1),   (1, 0),  (1, 1)]
        for d in ship.dots:
            for dx, dy in counter:
                cntr = Dot(d.x + dx, d.y + dy)
                if not self.out(cntr) and cntr not in self.counter_list:
                    if hid:
                        self.table[cntr.x][cntr.y] = '~'
                    self.counter_list.append(cntr)

    def out(self, d):
        return not ((0 <= d.x < 6) and (0 <= d.y < 6))

    def shot(self, d):
        if self.out(d):
            raise OutOfBoard()

        if d in self.counter_list:
            raise BoardUsed

        self.counter_list.append(d)

        for ship in self.ship_types:
            if ship.shooten(d):
                ship.hp -= 1
                self.table[d.x][d.y] = 'X'

                if ship.hp == 0:
                    self.counter(ship, hid=True)
                    self.table[d.x][d.y] = 'X'
                    print('Корабль потоплен!')
                    self.dead += 1
                    return False
                else:
                    print('Корабль поврежден!')
                    return True

        self.table[d.x][d.y] = '*'
        print('Мимо...')
        return False

    def povtor(self):
        self.counter_list = []


class Player:
    def __init__(self, board, board_vrag):
        self.board = board
        self.board_vrag = board_vrag

    def ask(self):
        pass

    def move(self):
        while True:
            try:
                coords = self.ask()
                target = self.board_vrag.shot(coords)
                return target
            except BoardExceptions as e:
                print(e)


class AI(Player):
    def ask(self):
        d = Dot(randint(0, 5), randint(0, 5))
        return d


class User(Player):
    def ask(self):
        while True:
            coords_shot = input('Чтобы сделать выстрел, введите 2 значения через пробел: ').split()

            if len(coords_shot) != 2:
                print('Введите 2 координаты')
                continue

            x, y = coords_shot

            if not (x.isdigit()) or not (y.isdigit()):
                print('Введите числа')
                continue

            x, y = int(x), int(y)

            return Dot(x - 1, y - 1)


class Game:
    def __init__(self):
        UserBoard = self.try_board()
        AIBoard = self.try_board()
        self.User = User(UserBoard, AIBoard)
        self.AI = AI(AIBoard, UserBoard)
        AIBoard.hid = True

    def random_board(self):
        board = Board()
        l = [3, 2, 2, 1, 1, 1, 1]
        num = 0
        for i in l:
            while True:
                num += 1
                if num > 20000:
                    return None
                ship = Battleship(i, Dot(randint(0, 5), randint(0, 5)), randint(0, 1))
                try:
                    board.add_ship(ship)
                    break
                except BoardUsedException:
                    pass
        board.povtor()
        return board

    def try_board(self):
        board = None
        while board is None:
            board = self.random_board()
        return board

    def great(self):
        print()
        print()
        print()
        print('*** МОРСКОЙ БОЙ В КОНСОЛИ ***')
        print()


    def loop(self):
        num = 0
        while True:
            print('Ваша доска:')
            print(self.User.board)
            print()
            print('Доска Компьютера:')
            print(self.AI.board)

            if num % 2 == 0:
                print('Ваш ход!')
                shotik = self.User.move()
            else:
                print('Ходит Компьютер!')
                shotik = self.AI.move()
            if shotik:
                num -= 1

            if self.User.board.dead == len(self.AI.board.ship_types):
                print('Ваша доска:')
                print(self.User.board)
                print()
                print('Доска Компьютера:')
                print(self.AI.board)
                print('Победил Компьютер!')
                break

            if self.AI.board.dead == len(self.User.board.ship_types):
                print('Ваша доска:')
                print(self.User.board)
                print()
                print('Доска Компьютера:')
                print(self.AI.board)
                print('Вы победили!')
                break
            num += 1
    def start(self):
        self.great()
        self.loop()


g = Game()
g.start()