# testing

# my project here


# some more stuff

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

def Instructions():

    print("Welcome to Battleships on python terminal! ")
    print("Do you have what it takes to defeat your opponent? ")
    print("The rules are simple: ")
    print("Sink your opponents ships before they sink yours.")

def selection_ships(board):

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
