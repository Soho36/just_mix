# Krestiki noliki-------------------------------------------------------

player1 = "X"
player2 = "O"

board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
def display_board(board):
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "----------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "----------")
    print("\t", board[6], "|", board[7], "|", board[8])
    print("\t")
display_board(board)

def take_turn (player):
    while True:
        player_turn = int(input(f"{player} turn! Please enter number (0 - 8): "))
        if 0 <= player_turn <= 8 and board[player_turn] not in [player1, player2]:
            board[player_turn] = player
            break
        else:
            print("Invalid input! Try again!")
    display_board(board)

# win situations:
def win_situations():
    if (board[0] == board[1] == board[2])\
            or (board[3] == board[4] == board[5])\
            or (board[6] == board[7] == board[8])\
            or (board[0] == board[4] == board[8])\
            or (board[2] == board[4] == board[6]):
        return True
win_situations()

for _ in range(5):
    take_turn(player1)
    if win_situations():
        print(f"{player1} win win congratulations!!")
        break
    take_turn(player2)
    if win_situations():
        print(f"{player2} win win congratulations!!")
        break
print("Game Over!")