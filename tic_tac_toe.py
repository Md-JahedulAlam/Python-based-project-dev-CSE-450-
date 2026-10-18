WINS = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)]


def show(board):
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i + 3]))
        if i < 6:
            print("--+---+--")


def winner(board):
    for a, b, c in WINS:
        if board[a] == board[b] == board[c] != " ":
            return board[a]
    return None


def main():
    board = [" "] * 9
    player = "X"
    for _ in range(9):
        show(board)
        while True:
            move = input(f"Player {player}, choose a cell (1-9): ")
            if move.isdigit() and 1 <= int(move) <= 9 and board[int(move) - 1] == " ":
                board[int(move) - 1] = player
                break
            print("Invalid move, try again.")
        if winner(board):
            show(board)
            print(f"Player {player} wins!")
            return
        player = "O" if player == "X" else "X"
    show(board)
    print("It's a draw!")


if __name__ == "__main__":
    main()