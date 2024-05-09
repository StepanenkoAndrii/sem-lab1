board_length = 19
test_number = 3


def check_win(board):
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]

    for i in range(board_length):
        for j in range(board_length):
            if board[i][j] == 0:
                continue

            color = board[i][j]
            for direction_x, direction_y in directions:
                consecutive_count = 1

                current_x, current_y = i + direction_y, j + direction_x
                while 0 <= current_x < board_length and 0 <= current_y < board_length and board[current_x][current_y] == color:
                    consecutive_count += 1
                    current_x += direction_y
                    current_y += direction_x

                if consecutive_count == 5:
                    current_x, current_y = i - direction_y, j - direction_x
                    if 0 <= current_x < board_length and 0 <= current_y < board_length and board[current_x][current_y] == color:
                        continue

                    return color, i + 1, j + 1

    return 0, -1, -1


def handle_file_input():
    with open(f"input{test_number}.txt", "r") as f_in, open("output.txt", "w") as f_out:
        test_cases = int(f_in.readline())
        for test_case in range(1, test_cases + 1):
            board = []
            for line_num in range(board_length):
                line = f_in.readline().strip().split()
                if len(line) != board_length:
                    print(len(line))
                    raise ValueError(
                        f"Invalid input in test case {test_case}: Each row must contain exactly {board_length} numbers")
                row = list(map(int, line))
                board.append(row)

            if len(board) != board_length:
                raise ValueError(f"Invalid input in test case {test_case}: There must be exactly {board_length} rows")

            color, horizontal, vertical = check_win(board)
            f_out.write(str(color) + "\n")
            if color != 0:
                f_out.write(str(horizontal) + " " + str(vertical) + "\n")


def main():
    handle_file_input()


if __name__ == "__main__":
    main()
