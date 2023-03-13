positions = ["0", "1", "2", "3", "4", "5", "6", "7", "8", ]
game_is_on = True


def grid():
    board = f""" 
         {positions[0]} | {positions[1]} | {positions[2]} 
        -----------
         {positions[3]} | {positions[4]} | {positions[5]}
        -----------
         {positions[6]} | {positions[7]} | {positions[8]}"""
    print(board)


def game_status():
    global game_is_on
    if positions[0] == positions[1] == positions[2] or positions[3] == positions[4] == positions[5] or positions[6] == \
            positions[7] == positions[8] or positions[1] == positions[4] == positions[7] or positions[0] == positions[
        3] == positions[6] or positions[2] == positions[5] == positions[8] or positions[0] == positions[4] == positions[
        8] or positions[2] == positions[4] == positions[6]:
        game_is_on = False
        return game_is_on


def player_one():
    player_1 = int(input("Type the number to place the X: "))
    if positions[player_1] == "O" or positions[player_1] == "X":
        player_1 = int(input("Sorry, that position is already taken. Choose another: "))
        positions[player_1] = "X"
    else:
        positions[player_1] = "X"



def player_two():
    player_2 = int(input("Type the number to place the O: "))
    if positions[player_2] == "X" or positions[player_2] == "O":
        player_2 = int(input("Sorry, that position is already taken. Choose another: "))
        positions[player_2] = "O"
    else:
        positions[player_2] = "O"




while game_is_on:

    grid()
    player_one()
    game_status()

    grid()
    player_two()
    game_status()
