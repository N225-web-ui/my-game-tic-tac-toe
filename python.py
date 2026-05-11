import math
from tkinter import*


# Score tracker
stats = {
    "Player Wins": 0,
    "AI Wins": 0,
    "Draws": 0
}


class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.player = "X"
        self.ai = "O"

    def print_board(self):
        print("\n")
        for i in range(0, 9, 3):
            print(f" {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} ")
            if i < 6:
                print("---+---+---")
        print("\n")

    def print_positions(self):
        print("\nBoard positions:")
        for i in range(0, 9, 3):
            print(f" {i} | {i+1} | {i+2} ")
            if i < 6:
                print("---+---+---")
        print("\n")

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def is_winner(self, player):
        win_patterns = [
            [0,1,2], [3,4,5], [6,7,8],  # rows
            [0,3,6], [1,4,7], [2,5,8],  # cols
            [0,4,8], [2,4,6]            # diagonals
        ]
        return any(all(self.board[pos] == player for pos in pattern)
                   for pattern in win_patterns)

    def is_draw(self):
        return " " not in self.board

    def minimax(self, is_maximizing):
        if self.is_winner(self.ai):
            return 1
        if self.is_winner(self.player):
            return -1
        if self.is_draw():
            return 0

        if is_maximizing:
            best_score = -math.inf
            for move in self.available_moves():
                self.board[move] = self.ai
                score = self.minimax(False)
                self.board[move] = " "
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for move in self.available_moves():
                self.board[move] = self.player
                score = self.minimax(True)
                self.board[move] = " "
                best_score = min(score, best_score)
            return best_score

    def best_move(self):
        best_score = -math.inf
        move = None

        for possible_move in self.available_moves():
            self.board[possible_move] = self.ai
            score = self.minimax(False)
            self.board[possible_move] = " "

            if score > best_score:
                best_score = score
                move = possible_move

        return move

    def player_move(self):
        while True:
            try:
                move = int(input("Enter your move (0-8): "))
                if move in self.available_moves():
                    self.board[move] = self.player
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Please enter a number between 0-8.")

    def ai_move(self):
        move = self.best_move()
        self.board[move] = self.ai
        print(f"AI chooses position {move}")

    def play(self):
        self.print_positions()

        while True:
            self.print_board()

            # Player turn
            self.player_move()
            if self.is_winner(self.player):
                self.print_board()
                print("🎉 You win!")
                stats["Player Wins"] += 1
                break
            if self.is_draw():
                self.print_board()
                print("It's a draw!")
                stats["Draws"] += 1
                break

            # AI turn
            self.ai_move()
            if self.is_winner(self.ai):
                self.print_board()
                print("🤖 AI wins!")
                stats["AI Wins"] += 1
                break
            if self.is_draw():
                self.print_board()
                print("It's a draw!")
                stats["Draws"] += 1
                break


def main():
    print("=== AI Tic-Tac-Toe (Minimax) ===")

    while True:
        game = TicTacToe()
        game.play()

        print("\nScoreboard:")
        for key, value in stats.items():
            print(f"{key}: {value}")

        replay = input("\nPlay again? (y/n): ").lower()
        if replay != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()