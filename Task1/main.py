import pygame 
from Board import Board, changeTurn

pygame.display.set_caption("Tic Tack Toe AI")

def main(win_size=600, row=3):
    board = Board(row, win_size)
    turn = 'X'

    running = True
    while running:
        board.redrawWindow()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and turn == 'X':
                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()
                    if board.validMove(pos):
                        board.updateBoard(pos, turn)
                        if board.wining(turn):
                            board.redrawWindow()
                            pygame.time.delay(400)

                            if turn == 'X':
                                winner = "You won!"
                            else:
                                winner = "AI wins!"

                            if board.endScreen(winner):
                                board.redrawWindow()
                            else:
                                running = False

                        if board.matchDrawCondi():
                            board.redrawWindow()
                            pygame.time.delay(400)
                            if board.endScreen("Match draw!"):
                                board.redrawWindow()
                            else:
                                running = False

                        turn = changeTurn(turn)
            elif turn == 'O':
                # AI's turn
                best_move = board.find_best_move()
                board.updateBoard((best_move[1] * board.sizeBTWN, best_move[0] * board.sizeBTWN), turn)

                if board.wining(turn):
                    board.redrawWindow()
                    pygame.time.delay(400)
                    
                    if turn == 'X':
                        winner = "You won!"
                    else:
                        winner = "AI wins!"

                    if board.endScreen(winner):
                        board.redrawWindow()
                    else:
                        running = False

                if board.matchDrawCondi():
                    board.redrawWindow()
                    pygame.time.delay(400)
                    if board.endScreen("Match draw!"):
                        board.redrawWindow()
                    else:
                        running = False

                turn = changeTurn(turn)

if __name__ == '__main__':
    main(600, 3)
    