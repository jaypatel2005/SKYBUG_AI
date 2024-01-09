import pygame
from Button import Button
from colors import *
from MinMax import minimax

pygame.font.init()
font = pygame.font.SysFont('lucidasans', 40)


def changeTurn(turn):
    if turn == 'O':
        return 'X'

    return 'O'


class Board:
    def __init__(self, row, win_size):
        self.refer_x = 100
        self.refer_y = 100    
        self.win = pygame.display.set_mode((win_size, win_size), 0)
        self.row = row
        self.win_size = win_size

        self.board = []
        for i in range(row):
            self.board.append([])
            for j in range(row):
                self.board[i].append('')

    def _drawLine(self):
        self.sizeBTWN = self.win_size//self.row

        x = 0
        y = 0
        for r in range(self.row):
            x = x + self.sizeBTWN
            y = y + self.sizeBTWN
            pygame.draw.line(self.win, (255, 255, 255), (x, 0), (x, self.win_size))
            pygame.draw.line(self.win, (255, 255, 255), (0, y), (self.win_size, y))

    def _drawCircle(self, x, y):
        pygame.draw.circle(self.win, (0, 0, 255), (x, y), 60, 2)

    def _drawX(self, x, y):
        lngth = 110
        x -= lngth/2
        y -= lngth/2

        pygame.draw.line(self.win, (255, 0, 0), (x, y), (x+lngth, y+lngth))
        x += lngth 
        pygame.draw.line(self.win, (255, 0, 0), (x, y), (x-lngth, y+lngth))

    def redrawWindow(self):
        self._drawLine()
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == 'X':
                    self._drawX(self.sizeBTWN*(col) + self.refer_x, self.sizeBTWN*(row) + self.refer_y)
                elif self.board[row][col] == 'O':
                    self._drawCircle(self.sizeBTWN*(col) + self.refer_x, self.sizeBTWN*(row) + self.refer_y)
        pygame.display.update()

    def find_best_move(self):
        best_val = float('-inf')
        best_move = (-1, -1)
        alpha = float('-inf')
        beta = float('inf')

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '':
                    self.board[i][j] = 'O'
                    move_val = minimax(self.board, 0, alpha, beta, False)
                    self.board[i][j] = ''
                    if move_val > best_val:
                        best_move = (i, j)
                        best_val = move_val

        return best_move


    def updateBoard(self, pos, turn):
        if turn == 'X':
            # Human move
            for i in range(3):
                if pos[0] > self.sizeBTWN * i and pos[0] < self.sizeBTWN * (i + 1):
                    for j in range(3):
                        if pos[1] > self.sizeBTWN * j and pos[1] < self.sizeBTWN * (j + 1):
                            if self.board[j][i] == '':
                                self.board[j][i] = turn
                                break
        else:
            # AI move (using Minimax)
            best_move = self.find_best_move()
            self.board[best_move[0]][best_move[1]] = turn

    def wining(self, turn):
        for row in range(self.row):
            for col in range(self.row):
                if self.board[row][0] == self.board[row][1] and self.board[row][1] == self.board[row][2]:
                    if self.board[row][0] == turn:
                        return 1
                    elif self.board[row][0] == changeTurn(turn):
                        return -1
                if self.board[0][col] == self.board[1][col] and self.board[1][col] == self.board[2][col]:
                    if self.board[0][col] == turn:
                        return 1
                    elif self.board[0][col] == changeTurn(turn):
                        return -1

        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
            if self.board[0][0] == turn:
                return 1
            elif self.board[0][0] == changeTurn(turn):
                return -1

        if self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]:
            if self.board[0][2] == turn:
                return 1
            elif self.board[0][2] == changeTurn(turn):
                return -1
        return 0

    def validMove(self, pos):
        for i in range(self.row):
            if self.sizeBTWN*i < pos[0] < self.sizeBTWN*(i + 1):
                for j in range(self.row):    
                    if self.sizeBTWN*j < pos[1] < self.sizeBTWN*(j + 1):
                        if self.board[j][i] == '':
                            return True
        return False

    def restart(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ''

    def matchDrawCondi(self):
        for i in range(self.row):
            for j in range(self.row):
                if self.board[i][j] == '':
                    return False
        return True

    def endScreen(self, text):
        restartButton = Button(self.win_size//2 - 44, self.win_size//2 , 88, 32, text="Restart", color=GREEN, fColor=BLACK, fStyle='lucidasans', fSize=20)
        exitButton = Button(self.win_size//2 - 28, self.win_size//2 + 50, 56, 32, text="Exit", color=DARK_RED, fColor=BLACK, fStyle='lucidasans', fSize=20)
        while True:
            self.win.fill(BLACK)
            winnerText = font.render(text, True, (255, 255, 255))
            self.win.blit(winnerText, ((self.win_size - winnerText.get_width())//2, (self.win_size - winnerText.get_height())//4))
            restartButton.draw(self.win, hoverColor=LIME, radius=5)
            exitButton.draw(self.win, hoverColor=RED, radius=5)
            
            if restartButton.clicked():
                self.__init__(self.row, self.win_size)
                return True
            
            if exitButton.clicked():
                return False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False

            pygame.display.update()
