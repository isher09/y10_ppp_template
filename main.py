# testing

# my project here


# some more stuff

import __main__


print("hello")

# test

Grid = []
Attempts = []
player_one_sunk_ships = []
player_two_sunk_ships = []
player_one_ship_coordinates = []
player_two_ship_coordinates = []
player_one_bomb_attempts = []
player_two_bomb_attempts = []

def initialise_board():
    return[["~"] * 12 for _ in range(8)]

def show_instructions():

    print("Welcome to Battleships on python terminal! ")
    print("Do you have what it takes to defeat your opponent? ")
    print("The rules are simple: ")
    print("Sink your opponents ships before they sink yours.")
    print(".                       You can choose where to place your ships on a 12 x 8 grid. ")
    print(".                       You will be able to place three ships, each with a length of one ")
    print(".                       coordinate. You can choose were to place your ships on the grid but")
    print("                        you can only them horizontally or vertically. ")
    print("The aim of the game is to sink your opposition’s ships before they sink yours.")
    print("You and your opponent will each have 1 turn to try and sink their opponent's ships.")
    print("You will be able to see your attempts to sink the opponent's ship.")
    print("If you have hit a part of your opponent's ship. The coordinate will display a yellow colour.")
    print("If you have sunk your opponent's ship, then the ship’s coordinates will be displayed in a red colour. ")
    print("")
    print("If you have missed completely, then the coordinates will display a blue colour.")
    print("The game is over when you or your opponent have no more ships floating.")
    print("If you would like to play again, then there will be an option to at the end.")
    print("That is all from me so happy battles! ")

board = ""
def select_ships():
    valid_selection_ships = []
    p1_selection = False
    columns = "ABCDEFGHIJKL"
    
    while p1_selection == False:
        selection_p1 = (input("Player 1 place your ships:"))
        for i in range(1, 9):
            if selection_p1[0] in columns:  
                if i == selection_p1[1]:
                
                    if len(selection_p1) == 2:
                        print(f"You successfully placed a ship at, {selection_p1}")
                        p1_selection = True
                        return selection_p1
            
        print("Invalid column/row/length of selection  please try again") # should this be repeated?

            
           
# the if staement checks the first letter only but what if the column is 10 or more ?

                    



            





    pass


def display_board(board):
    pass


# terminal
#>>> 
#>>> print("isher\njohal")
#isher
#ohal
#>>> print("isher\tjohal")
#isher	johal
#>>> print("isher johal".center(50))
#                   isher johal                    
#>>> print("isher johal".rjust(50, "X"))
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXisher johal

def check_if_hit():
    pass


def tests():
    for i in range(1, 4):
        print("test", i)
        select_ships()


if __name__ == "__main__":
    tests()
    # setup
    # show_instructions()
    # board = initialise_board()
    # display_board(board)
    # board = select_ships(board)
    # winner = False

    # while winner == False:
    #     # step 1
    #     x, y = choose_coordinates(board)
    #     # step 2
    #     check_if_hit() #     return... hit, sink,
        
    #     # step 3

    #     # step 4
    #     winner = check_if_boats_remain(board)
    #     print("hello")