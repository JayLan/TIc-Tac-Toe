# Developed with assistance from ChatGPT

import curses


def print_board(stdscr, board):
    stdscr.clear()
    stdscr.addstr(0, 0, "Tic-Tac-Toe", curses.A_BOLD)
    stdscr.addstr(1, 0, "Player 1 'X' (© - Blue), Player 2 'O' (© - Red)", curses.A_BOLD)
   	    
    
    for index, position in enumerate(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']):
        row = index // 3
        col = index % 3

        # Set up row positions for the board display
        y = 3 + row * 2
        x = col * 4

        if board[position] == 'X':
                stdscr.addstr(y, x, " © ", curses.color_pair(1))  # Player 1 © in blue
        elif board[position] == 'O':
                stdscr.addstr(y, x, " © ", curses.color_pair(2))  # Player 2 © in red
        else:
            stdscr.addstr(y, x, f" {board[position]} ", curses.color_pair(4))  # Board spots in white

        # Draw horizontal lines
        if col < 2:
            stdscr.addstr(y, x + 3, "|", curses.color_pair(3))
        
        # Draw vertical lines
        if row < 2:
            stdscr.addstr(y + 1, x, "---+", curses.color_pair(3))

    stdscr.refresh()

def check_winner(board, player):
    win_conditions = [
        ['A', 'B', 'C'],
        ['D', 'E', 'F'],
        ['G', 'H', 'I'],
        ['A', 'D', 'G'],
        ['B', 'E', 'H'],
        ['C', 'F', 'I'],
        ['A', 'E', 'I'],
        ['C', 'E', 'G']
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def is_draw(board):
    return all(board[pos] != pos for pos in board)

def tic_tac_toe(stdscr):
    global piecesSet, pieces
    
    # Initialization for curses
    curses.curs_set(1)  # Blinking cursor for input
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)  # Player 1 color (blue)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)   # Player 2 color (red)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK) # Board color (white)
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK) # Positions Color (yellow)
    
    board = {
        'A': 'A', 'B': 'B', 'C': 'C',
        'D': 'D', 'E': 'E', 'F': 'F',
        'G': 'G', 'H': 'H', 'I': 'I'
    }

    current_player = 'X'
    available_positions = list(board.keys())
    
    while True:
        # Display board
        print_board(stdscr, board)
        stdscr.addstr(10, 0, f"Player {current_player}, enter your move (A-I): ", curses.color_pair(3))
        stdscr.addstr(11, 0, f"Available positions: {', '.join([pos for pos in board if board[pos] in available_positions])}", 
curses.color_pair(3))
        
        stdscr.refresh()

        # Get user input
        curses.echo()  # Enable input display
        move = stdscr.getstr(12, 0, 2).decode('utf-8').upper()  # Input move
        curses.noecho()  # Disable input display after entry

        # Validate the move
        if move not in available_positions or board[move] != move:
            stdscr.addstr(13, 0, "Invalid move! Please try again.", curses.color_pair(3))
            stdscr.refresh()
            stdscr.getch()
            continue

        # Place the move on the board
        board[move] = current_player

        # Check for a winner
        if check_winner(board, current_player):
            print_board(stdscr, board)
            stdscr.addstr(14, 0, f"Player {current_player} wins!", curses.color_pair(3))
            stdscr.refresh()
            stdscr.getch()
            break

        # Check for a draw
        if is_draw(board):
            print_board(stdscr, board)
            stdscr.addstr(14, 0, "It's a draw!", curses.color_pair(3))
            stdscr.refresh()
            stdscr.getch()
            break

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    curses.wrapper(tic_tac_toe)

