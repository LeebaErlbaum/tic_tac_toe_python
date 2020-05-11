# Tic Tac Toe for 2 players

# Imports
from random import randrange

# Method to get player names
def define_players():
    # player one
    player_one = input("Welcome. Player One, please enter your name: ")
    print(f"Thank you {player_one}!")

    # player two
    player_two = input("Welcome. Player Two, please enter your name: ")
    print(f"Thank you {player_two}!")

    return player_one, player_two

# Method to randomly assign players X or O
def assign_x_or_o(player_one, player_two):
    # get randomly either 0 or 1
    rand_num = randrange(2)
    # if 0, player one is X 
    if rand_num == 0:
        player_one_letter = "X"
        print(f"{player_one}, you are X. You will go first.")

        player_two_letter = "O"
        print(f"{player_two}, you are O. You will go second.")

        return player_one_letter, player_two_letter 
    # if 1, player one is 0
    elif rand_num == 1:
        player_two_letter = "X"
        print(f"{player_two}, you are X. You will go first.")

        player_one_letter = "O"
        print(f"{player_one}, you are O. You will go second.")

        return player_one_letter, player_two_letter

# Method to start the game
def start_game(player_one, player_one_letter, player_two, player_two_letter, player_one_board_list, player_two_board_list):
    if player_one_letter == "X":
        current_player = player_one
        current_player_board_list = player_one_board_list
        other_player = player_two
        other_player_board_list = player_two_board_list
        current_player_letter = player_one_letter
        other_player_letter = player_two_letter


        return current_player, current_player_board_list, current_player_letter, other_player, other_player_board_list, other_player_letter
    elif player_two_letter == "X":
        current_player = player_two
        current_player_board_list = player_two_board_list
        other_player = player_one
        other_player_board_list = player_one_board_list
        current_player_letter = player_two_letter
        other_player_letter = player_one_letter

        return current_player, current_player_board_list, current_player_letter, other_player, other_player_board_list, other_player_letter

# Method to print board
def print_board(game_board_print):
    print("This is the current board:")
    print(game_board_print[0], "|",  game_board_print[1], "|", game_board_print[2], sep = '   ')
    print("___",  "___", "___", sep = '    ')
    print(game_board_print[3], "|",  game_board_print[4], "|", game_board_print[5], sep = '   ')
    print("___",  "___", "___", sep = '    ')
    print(game_board_print[6], "|",  game_board_print[7], "|", game_board_print[8], sep = '   ')

    return 0

# Method for a player to pick a game board spot
def pick_spot(current_player, current_player_letter, board_positions_list, game_board_print, current_player_board_list):
    print(" The current available positions are, " + ', '.join(board_positions_list))
    position = 100
    while position == 100:
        try:
            position = int(input(f"{current_player}, choose an available position: "))
            if position not in (0, 1, 2, 3, 4, 5, 6, 7, 8):
                raise ValueError
            elif position not in board_positions_list:
                position = 100
                print("Oops. That position is taken.") 
        except ValueError:
            position = 100
            print("Oops, that's not a valid tic tac toe board position!")
    # replace chosen position on board with either X or O depending on the current player's letter
    game_board_print[position] = current_player_letter
    board_positions_list.remove(position)
    current_player_board_list.append(position)
    
    return board_positions_list, current_player_board_list

# Method to check if current player has won
def check_for_win(current_player_board_list):
    # Check rows for win
    row_a = all(x in current_player_board_list for x in [0, 1, 2])
    if row_a == True:
        return True
    row_b = all(x in current_player_board_list for x in [3, 4, 5])
    if row_b == True:
        return True
    row_c = all(x in current_player_board_list for x in [6, 7, 8])
    if row_c == True:
        return True

    # Check columns for win
    column_a = all(x in current_player_board_list for x in [0, 3, 6])
    if column_a == True:
        return True
    column_b = all(x in current_player_board_list for x in [1, 4, 7])
    if column_b == True:
        return True
    column_c = all(x in current_player_board_list for x in [2, 5, 8])
    if column_c == True:
        return True

    # Check diagonal for win
    diagonal_aa_to_cc = all(x in current_player_board_list for x in [0, 4, 8])
    if diagonal_aa_to_cc == True:
        return True
    diagonal_ca_to_ac = all(x in current_player_board_list for x in [2, 4, 6])
    if diagonal_ca_to_ac == True:
        return True

    return False

# Method to switch the current player of the game
def switch_players(current_player, current_player_board_list, current_player_letter, player_one, player_two, other_player, other_player_board_list, other_player_letter):
    if current_player == player_one:
        current_player = player_two
        other_player = player_one
        temp_board_list = current_player_board_list
        current_player_board_list = other_player_board_list
        other_player_board_list = temp_board_list
        temp_player_letter = current_player_letter
        current_player_letter = other_player_letter
        other_player_letter = temp_player_letter

        return current_player, current_player_board_list, current_player_letter, other_player, other_player_board_list, other_player_letter
    elif current_player == player_two:
        current_player = player_one
        other_player = player_two
        temp_board_list = current_player_board_list
        current_player_board_list = other_player_board_list
        other_player_board_list = temp_board_list
        temp_player_letter = current_player_letter
        current_player_letter = other_player_letter
        other_player_letter = temp_player_letter

        return current_player, current_player_board_list, current_player_letter, other_player, other_player_board_list, other_player_letter

# Method to determine if players would like to play again
def play_again():
    play_again = "m"
    while play_again == "m":
        try: 
            play_again = str(input("Do you want to play again? [y, n]"))
            if play_again not in ("y", "n"):
                raise ValueError
            else:
                return play_again
        except ValueError:
            play_again = "m"
            print("Please return a valid response to the question. Valid responses include: [y, n]")

# Method to play the game 
def play_game(game_board_print, player_one, player_one_letter, player_two, player_two_letter, board_positions_list, player_one_board_list, player_two_board_list):
    # To start game
    print_board(game_board_print)
    current_player, current_player_board_list, current_player_letter, other_player, other_player_board_list, other_player_letter = start_game(player_one, player_one_letter, player_two, player_two_letter, player_one_board_list, player_two_board_list)
    player_who_went_second = other_player

    while board_positions_list != []:
        board_positions_list, current_player_board_list = pick_spot(current_player, current_player_letter, board_positions_list, game_board_print, current_player_board_list)

        if len(board_positions_list) <= 6:
            maybe_win = check_for_win(current_player_board_list)
            if maybe_win == True:
                print(f"Congratulations {current_player}, you win!")
                play_again = play_again()
                winning_player = current_player

                return play_again, winning_player
            elif board_positions_list == []:
                print(f"It's a tie.")
                play_again = play_again()

                return play_again, player_who_went_second
            else:
                print(f"Let's continue the game. {other_player}, you're next!")
        else:
            print(f"Let's continue the game. {other_player}, you're next!")
        
        current_player, current_player_board_list, current_player_letter, other_player, other_player_board_list, other_player_letter = switch_players(current_player, current_player_board_list, current_player_letter, player_one, player_two, other_player, other_player_board_list, other_player_letter)

# Method to check if same people are playing again
def same_people_playing():
    same_people = "m"
    while same_people == "m":
        try:
            same_people = str(input("Are the same people playing? [y, n]"))
            if same_people not in ("y", "n"):
                raise ValueError
            else:
                return same_people
        except ValueError:
            same_people = "m"
            print("Please return a valid response to the question. Valid responses include: [y, n]")

# Main method
def main():
    player_one, player_two = define_players()
    player_one_letter, player_two_letter = assign_x_or_o(player_one, player_two)
    
    board_positions_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    game_board_print = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    player_one_board_list = []
    player_two_board_list = []
    play_again, player_to_go_first_next_round = play_game(game_board_print, player_one, player_one_letter, player_two, player_two_letter, board_positions_list, player_one_board_list, player_two_board_list)

    while play_again == "y":
        same_people = same_people_playing()
        if same_people == "y":
            if player_to_go_first_next_round == player_one:
                player_one_letter = "X"
                player_two_letter = "O"
                play_again, player_to_go_first_next_round = play_game(game_board_print, player_one, player_one_letter, player_two, player_two_letter, board_positions_list, player_one_board_list, player_two_board_list)
            elif player_to_go_first_next_round == player_two:
                player_one_letter = "O"
                player_two_letter = "X"
                play_again, player_to_go_first_next_round = play_game(game_board_print, player_one, player_one_letter, player_two, player_two_letter, board_positions_list, player_one_board_list, player_two_board_list)
        elif same_people == "n":
            main()

    if play_again == "n":
        print("Thank you for playing. Play again soon!")
        exit()

# Call main method
if __name__ == "__main__":
    main()