from typing import List, Tuple

board = list(range(1, 10))

winners = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
]

moves = ((1, 3, 7, 9), (5,), (2, 4, 6, 8))


class Colors:
    """A class to define ANSI escape codes for colored text"""

    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"  # orange on some systems
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    LIGHT_GRAY = "\033[37m"
    DARK_GRAY = "\033[90m"
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    WHITE = "\033[97m"

    RESET = "\033[0m"  # called to return to standard terminal text color


def print_board() -> None:
    """Print the Tic-Tac-Toe board with X and O markers.

    Returns:
        None
    """
    j = 1
    for i in board:
        end = " "
        if j % 3 == 0:
            end = "\n\n"
        if i == "X":
            print(Colors.RED + f"[{i}]" + Colors.RESET, end=end)
        elif i == "O":
            print(Colors.BLUE + f"[{i}]" + Colors.RESET, end=end)
        else:
            print(f"[{i}]", end=end)
        j += 1


def make_move(
    brd: List[int], plyr: str, mve: int, undo: bool = False
) -> Tuple[bool, bool]:
    """Make a move on the board.

    Args:
        brd (List[int]): The current board state.
        plyr (str): The player making the move ("X" or "O").
        mve (int): The chosen move (1-9).
        undo (bool, optional): Whether to undo the move (for checking purposes).

    Returns:
        Tuple[bool, bool]: A tuple indicating if the move was valid and if the player won.
    """
    if can_move(brd, mve):
        brd[mve - 1] = plyr
        win = is_winner(brd, plyr)
        if undo:
            brd[mve - 1] = mve
        return True, win
    return False, False


def can_move(brd: List[int], mve: int) -> bool:
    """Check if a move is valid.

    Args:
        brd (List[int]): The current board state.
        mve (int): The chosen move (1-9).

    Returns:
        bool: True if the move is valid, False otherwise.
    """
    if mve in range(1, 10) and isinstance(brd[mve - 1], int):
        return True
    return False


def is_winner(brd: List[int], plyr: str) -> bool:
    """Check if a player has won.

    Args:
        brd (List[int]): The current board state.
        plyr (str): The player to check ("X" or "O").

    Returns:
        bool: True if the player has won, False otherwise.
    """
    win = True
    for tup in winners:
        win = True
        for j in tup:
            if brd[j] != plyr:
                win = False
                break
        if win:
            break
    return win


def has_empty_space() -> bool:
    """Check if there is an empty space on the board.

    Returns:
        bool: True if there are empty spaces, False otherwise.
    """
    return board.count("X") + board.count("Y") != 9


def computer_move() -> Tuple[bool, bool]:
    """Determine the computer's move.

    Returns:
        Tuple[bool, bool]: A tuple indicating if the move was valid and if the computer won.
    """
    mv = -1
    for i in range(1, 10):
        if make_move(board, computer, i, True)[1]:
            mv = i
            break

    if mv == -1:
        for j in range(1, 10):
            if make_move(board, player, j, True)[1]:
                mv = j
                break

    if mv == -1:
        for tup in moves:
            for m in tup:
                if mv == -1 and can_move(board, m):
                    mv = m
                    break

    return make_move(board, computer, mv)


player, computer = "X", "O"
print(f"\nplayer: {player}\ncomputer: {computer}\n")
while has_empty_space():
    print_board()
    move = int(input("Choose your move(1-9): "))
    moved, won = make_move(board, player, move)
    if not moved:
        print("Invalid number! Try again!")
        continue
    if won:
        print(Colors.GREEN + f"You won!" + Colors.RESET)
        break
    elif computer_move()[1]:
        print(Colors.RED + f"You loose!" + Colors.RESET)
        break

print_board()
