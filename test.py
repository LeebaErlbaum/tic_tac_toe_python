# Method to print board
def print_board(game_board_print):
    print(game_board_print[0], "|",  game_board_print[1], "|", game_board_print[2], sep = '   ')
    print("___",  "___", "___", sep = '    ')
    print(game_board_print[3], "|",  game_board_print[4], "|", game_board_print[5], sep = '   ')
    print("___",  "___", "___", sep = '    ')
    print(game_board_print[6], "|",  game_board_print[7], "|", game_board_print[8], sep = '   ')
    return 0

game_board_print = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print_board(game_board_print)