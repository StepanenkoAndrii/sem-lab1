board_length = 19
test_number = 1


def check_win(board):
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]

    for i in range(board_length):
        for j in range(board_length):
            if board[i][j] == 0:
                continue

            color = board[i][j]
            for dx, dy in directions:
                consecutive_count = 1

                nx, ny = i + dy, j + dx
                while 0 <= nx < board_length and 0 <= ny < 19 and board[nx][ny] == color:
                    consecutive_count += 1
                    nx += dy
                    ny += dx

                if consecutive_count == 5:
                    nx, ny = i - dy, j - dx
                    if 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == color:
                        continue

                    return color, i + 1, j + 1

    return 0, -1, -1


def main():
    with open(f"input{test_number}.txt", "r") as f_in, open("output.txt", "w") as f_out:
        test_cases = int(f_in.readline())
        for test_case in range(1, test_cases + 1):
            board = []
            for line_num in range(board_length):
                line = f_in.readline().strip().split()
                if len(line) != board_length:
                    print(len(line))
                    raise ValueError(
                        f"Invalid input in test case {test_case}: Each row must contain exactly 19 numbers")
                row = list(map(int, line))
                board.append(row)

            if len(board) != 19:
                raise ValueError(f"Invalid input in test case {test_case}: There must be exactly 19 rows")

            color, horizontal, vertical = check_win(board)
            f_out.write(str(color) + "\n")
            if color != 0:
                f_out.write(str(horizontal) + " " + str(vertical) + "\n")


if __name__ == "__main__":
    main()
