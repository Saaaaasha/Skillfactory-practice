def greeting():
    print("----- ИГРА -----")
    print("-КРЕСТИКИ-НОЛИКИ-")
    print("-----------------")
    print("---- ПРАВИЛА: ----")
    print("- Введите 2 координаты "
          "через пробел!-")
    print("-----------------")


board = [["_" for i in range(3)] for y in range(3)]
vertical_coordinates = ("0", "1", "2")


def show_board():
    print(" ", "0", "1", "2")
    for y, i in enumerate(vertical_coordinates):
        print(i, " ".join(board[y]))


def user_input():
    # x, y = map(int, input(" Ваш ход: ").split())
    while True:
        coordinates = input(" Ваш ход: ").split()

        if len(coordinates) != 2:
            print("Введите 2 координаты через пробел!")
            continue

        x, y = coordinates
        x, y = int(x), int(y)
        if 0 <= x <= 2 and 0 <= y <= 2:
            if board[x][y] == "_":
                return x, y
            else:
                print("Клетка недоступна!")
        else:
            print(" Неверные координаты! ")
            continue

        return x, y


def check_winner():
    win_coordinate = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_coordinate:
        symbols = []
        for c in cord:
            symbols.append(board[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!")
            return True
    return False


greeting()
count = 0
while True:
    count += 1
    show_board()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")

    x, y = user_input()

    if count % 2 == 1:
        board[x][y] = "X"
    else:
        board[x][y] = "0"

    if check_winner():
        break

    if count == 9:
        print(" Ничья!")
        break

