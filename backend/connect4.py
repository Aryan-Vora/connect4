import random


class Game:
    def __init__(self):
        self.board = ConnectFour()
        self.mode = None
        self.turn = 0
        self.moves = []
        self.winner = -1

    def reset(self):
        self.board.reset()
        self.turn = 0
        self.moves = []
        self.winner = -1

    def move(self, col, playerID):
        # check if playerID matches turn
        if self.winner != -1:
            return 400
        if playerID != self.turn:
            return 400
        # make the move
        if self.board.move(col, playerID) == True:
            self.moves.append([col, playerID])
            self.turn += 1
            self.turn %= 2
            # check for a winner
            winner = self.board.check_winner()
            if winner == 1:
                self.winner = playerID
            elif winner == 2:
                self.winner = 2
            return 200
        else:
            return 403


class ConnectFour:
    def __init__(self):
        self.board = [[-1 for _ in range(7)] for _ in range(6)]

    def reset(self):
        self.board = [[-1 for _ in range(7)] for _ in range(6)]

    def get_board(self):
        return self.board

    def available_moves(self):
        moves = []
        for col in range(7):
            if self.board[0][col] == -1:
                moves.append(col)
        return moves

    def move(self, col, player):
        # check if the column is full
        if self.board[0][col] != -1:
            return False
        # find the lowest empty cell in the column
        row = 0
        while row < 6 and self.board[row][col] == -1:
            row += 1
        # make the move
        self.board[row-1][col] = player
        return True

    def check_winner(self):
        # check rows
        for row in range(6):
            for col in range(4):
                if self.board[row][col] == self.board[row][col+1] == self.board[row][col+2] == self.board[row][col+3] != -1:
                    return 1
        # check columns
        for col in range(7):
            for row in range(3):
                if self.board[row][col] == self.board[row+1][col] == self.board[row+2][col] == self.board[row+3][col] != -1:
                    return 1
        # check diagonals
        for row in range(3):
            for col in range(4):
                if self.board[row][col] == self.board[row+1][col+1] == self.board[row+2][col+2] == self.board[row+3][col+3] != -1:
                    return 1
        for row in range(3):
            for col in range(3, 7):
                if self.board[row][col] == self.board[row+1][col-1] == self.board[row+2][col-2] == self.board[row+3][col-3] != -1:
                    return 1
        # check for a draw
        count = 0
        for row in range(6):
            for col in range(7):
                if self.board[row][col] != -1:
                    count = 1
                    break
        if count == 0:
            return 2
        return 0
