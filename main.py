# testing

# my project here

# test
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

def select_ships(board):
    # ask the user where they want to place their ships
    # return .... x ,y coordinates of ships
    grid_coordinates_A = ["1A", "2A", "3A", "4A" ,"5A", "6A", "7A", "8A", "9A", "10A" ,"11A", "12A", ]
    grid_coordinates_B = [ "1B" ,"2B" ,"3B" ,"4B","5B" ,"6B" , "7B", "8B", "9B", "10B", "11B" , "12B"]
    grid_coordinates_C = [ "1C" ,"2C" ,"3C" ,"4C","5C" ,"6C" , "7C", "8C", "9C", "10C", "11C" , "12C"]
    grid_coordinates_D = [ "1D" ,"2D" ,"3D" ,"4D","5D" ,"6D" , "7D", "8D", "9D", "10D", "11D" , "12D"]
    grid_coordinates_E = [ "1E" ,"2E" ,"3E" ,"4E","5E" ,"6E" , "7E", "8E", "9E", "10E", "11E" , "12E"]
    grid_coordinates_C = [ "1C" ,"2C" ,"3C" ,"4C","5C" ,"6C" , "7C", "8C", "9C", "10C", "11C" , "12C"]


    valid_coordinates = []
    for number in range(1,13):
        for letter in "ABCDEF":
            valid_coordinates.append(number)
            valid_coordinates.append(letter)
    
    print(valid_coordinates)




select_ships(None)


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
