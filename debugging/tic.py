#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Rows
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return True

    # Columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        try:
            row = int(input(f"Enter row (0, 1, 2) for player {player}: "))
            col = int(input(f"Enter col (0, 1, 2) for player {player}: "))
        except ValueError:
            print("❌ Invalid input! Please enter numbers.")
            continue

        if not (0 <= row < 3 and 0 <= col < 3):
            print("🚫 Coordinates out of range! Try (0, 1, or 2).")
            continue

        if board[row][col] != " ":
            print("⚠️ That spot is already taken!")
            continue

        board[row][col] = player

        if check_winner(board):
            print_board(board)
            print(f"🏆 Player {player} wins!")
            break

        if is_full(board):
            print_board(board)
            print("🤝 It's a draw!")
            break

        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
