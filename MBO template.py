import random

# Inner logics
# Exception classes
# BoardOutException
# В начале имеет смысл написать классы исключений, которые будет использовать наша программа.
# Например, когда игрок пытается выстрелить в клетку за пределами поля, во внутренней логике
# должно выбрасываться соответствующее исключение BoardOutException, а потом отлавливаться во
# внешней логике, выводя сообщение об этой ошибке пользователю.

class Dot:              #— класс точек на поле.
    def __init__(self, x, y):
        self.x = x
        self.y = y
# Очень удобно будет реализовать в этом классе метод __eq__,
# чтобы точки можно было проверять на равенство. Тогда, чтобы проверить, находится ли точка в списке,
# достаточно просто использовать оператор in, как мы делали это с числами .

class Ship:
    def __init__(self, length, nospoint, position, lives):
        self.length = length
        self.nospoint = nospoint                        #нос корабля
        self.position = position                        #вертикальное/горизонтальное
        self.lives = lives                            #сколько точек корабля ещё не подбито
    def dots(self):                                 #возвращает список всех точек корабля
        pass


class Board:
    def __init__(self, cells_list, ships_list, hid, live_ships):
        self.cells_list = cells_list                            #Двумерный список, в котором хранятся состояния каждой из клеток.
        self.ships_list = ships_list                            #Список кораблей доски
        self.hid = hid                                          #Параметр hid типа bool — информация о том, нужно ли скрывать корабли на доске (для вывода доски врага) или нет (для своей доски).
        self.live_ships = live_ships                            #Количество живых кораблей на доске.
        pass
    def add_ship(self):                 #ставит корабль на доску (если ставить не получается, выбрасываем исключения).
        pass
    def contour(self):                  #который обводит корабль по контуру. Он будет полезен и в ходе самой игры, и в при расстановке кораблей (помечает соседние точки, где корабля по правилам быть не может).
        pass
    def show_board(self):               #который выводит доску в консоль в зависимости от параметра hid
        for row in self.cells_list:
            print(" ".join(row))
    def out_of_board(self):             #Метод out, который для точки (объекта класса Dot) возвращает True, если точка выходит за пределы поля, и False, если не выходит.
        pass
    def shot(self):                     #делает выстрел по доске (если есть попытка выстрелить за пределы и в использованную точку, нужно выбрасывать исключения).
        pass



# Outer logics
class Player:                           #Этот класс будет родителем для классов с AI и с пользователем. Игрок описывается параметрами: 1. Собственная доска (объект класса Board). 2 Доска врага.
    def __init__(self, user_board, ai_board):
        pass
    def ask(self):      #метод, который «спрашивает» игрока, в какую клетку он делает выстрел. Пока мы делаем общий для AI и пользователя класс, этот метод мы описать не можем. Оставим этот метод пустым. Тем самым обозначим, что потомки должны реализовать этот метод.
        pass
    def move(self):     #метод, который делает ход в игре. Тут мы вызываем метод ask, делаем выстрел по вражеской доске (метод Board.shot), отлавливаем исключения, и если они есть, пытаемся повторить ход. Метод должен возвращать True, если этому игроку нужен повторный ход (например, если он выстрелом подбил корабль).
        pass
class AI(Player):       #Теперь нам остаётся унаследовать классы AI и User от Player и переопределить в них метод ask. Для AI это будет выбор случайной точки, а для User этот метод будет спрашивать координаты точки из консоли.
    def ask(self):
        pass
class User(Player):
    def ask(self):
        pass

class Game:
    def __init__(self, user, ai, user_board, ai_board):
        pass
    def random_board(self):     #метод генерирует случайную доску. Для этого мы просто пытаемся в случайные клетки изначально пустой доски расставлять корабли (в бесконечном цикле пытаемся поставить корабль в случайную доску, пока наша попытка не окажется успешной). Лучше расставлять сначала длинные корабли, а потом короткие. Если было сделано много (несколько тысяч) попыток установить корабль, но это не получилось, значит доска неудачная и на неё корабль уже не добавить. В таком случае нужно начать генерировать новую доску.
        pass
    def greet(self):            #метод, который в консоли приветствует пользователя и рассказывает о формате ввода.
        pass
    def loop(self):         #метод с самим игровым циклом. Там мы просто последовательно вызываем метод mode для игроков и делаем проверку, сколько живых кораблей осталось на досках, чтобы определить победу.
        pass
    def mode(self):
        pass
    def start(self):        #запуск игры. Сначала вызываем greet, а потом loop.
        pass
