def evaluate(board):
    # Check rows
    for row in board:
        if all(cell == 'X' for cell in row):
            return -1
        elif all(cell == 'O' for cell in row):
            return 1

    # Check columns
    for col in range(3):
        if all(board[row][col] == 'X' for row in range(3)):
            return -1
        elif all(board[row][col] == 'O' for row in range(3)):
            return 1

    # Check diagonals
    if all(board[i][i] == 'X' for i in range(3)) or all(board[i][2 - i] == 'X' for i in range(3)):
        return -1
    elif all(board[i][i] == 'O' for i in range(3)) or all(board[i][2 - i] == 'O' for i in range(3)):
        return 1

    return 0  # No winner yet

def is_board_full(board):
    return all(cell != '' for row in board for cell in row)

def minimax(board, depth, alpha, beta, is_maximizing):
    score = evaluate(board)

    if score == 1 or score == -1:
        return score - depth

    if is_board_full(board):
        return 0

    if is_maximizing:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, alpha, beta, False)
                    board[i][j] = ''
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, alpha, beta, True)
                    board[i][j] = ''
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

