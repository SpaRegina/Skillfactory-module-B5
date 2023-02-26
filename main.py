def print_board(board):
    """
    Функция для вывода игрового поля на экран
    """
    print("----1---2---3--")
    for i in range(3):
        print(i+1,"|", end=" ")
        for j in range(3):
            print(board[i][j], end=" | ")
        print()
        print("---------------")

def get_move(player, board):
    """
    Функция для получения хода от игрока
    """
    while True:
        move = input("Ход игрока " + player + " (строка, столбец): ")
        try:
            row, col = move.split(",")
            row = int(row)
            col = int(col)
            if row >= 1 and row <= 3 and col >= 1 and col <= 3 and board[row-1][col-1] == "-":
                return row-1, col-1
            else:
                print("Некорректный ход, попробуйте еще раз")
        except:
            print("Некорректный ввод, попробуйте еще раз")

def check_win(board):
    """
    Функция для проверки, выиграл ли кто-то из игроков
    """
    # проверяем горизонтали
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "-":
            return board[i][0]

    # проверяем вертикали
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "-":
            return board[0][i]

    # проверяем диагонали
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "-":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "-":
        return board[0][2]

    return None

def play_game():
    """
    Основная функция игры
    """
    board = [["-" for i in range(3)] for j in range(3)]
    players = ["X", "O"]
    current_player = 0

    while True:
        # выводим текущее состояние поля на экран
        print_board(board)

        # получаем ход от игрока
        row, col = get_move(players[current_player], board)
        board[row][col] = players[current_player]

        # проверяем, выиграл ли кто-то
        winner = check_win(board)
        if winner is not None:
            print_board(board)
            print("Игрок", winner, "выиграл!")
            return

        # проверяем, не закончилась ли игра в ничью
        if all([cell != "-" for row in board for cell in row]):
            print_board(board)
            print("Ничья!")
            return


        current_player = (current_player + 1) % 2

if __name__ == "__main__":
    play_game()
