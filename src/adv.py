from room import Room
from player import Player
from item import Item
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
new_player = Player("Jayne", room['outside'])

# print(len(room['outside'].room_items))

# CREATE VARIABLES FOR ROOMS
outside = room['outside']
foyer = room['foyer']
overlook = room['overlook']
narrow = room['narrow']
treasure = room['treasure']


# ADD ITEMS TO ROOMS
axe = Item("AXE", "by jove, it is sharp")
compass = Item("Compass", "weathered, but still works")
outside.stealthy_add(axe)
outside.stealthy_add(compass)

foyer.stealthy_add(compass)

binoculars = Item("Binoculars", "handy for spying")
overlook.stealthy_add(binoculars)

torch = Item("Torch", "batteries running low")
narrow.stealthy_add(torch)

gold = Item("Gold coins", "they are worth a fortune!")
treasure.stealthy_add(gold)

print("\n------- WELCOME TO JAYNE'S GAME ---------\n")






# Write a loop that:

user_prompt = None

while user_prompt != "q":
    
    # * Prints the current room name
    print(new_player)
    
    # * Prints the current description (the textwrap module might be useful here).
    room_description = new_player.current_room.description
    wrapper = textwrap.TextWrapper(width=15)
    word_list = wrapper.wrap(text=room_description)
    for element in word_list:
        print("  >    " + element)
        
    # * Waits for user input and decides what to do        
    user_prompt = (input("\n---- WHERE DO YOU WANT TO GO ? ---- \n Type [n], [s], [e] or [w]\n OR [look]\n OR quit:(q):  "))
    
    # JAYNE: USER_PROMPT IS A STRING
    
    # If the user enters a cardinal direction, attempt to move to the room there.
    
    if user_prompt.lower() == 'n':
        #OUTSIDE
        if new_player.current_room == outside:
            print("\n---- LET US GO NORTH ----\n")
            new_player.current_room = foyer
            print(new_player.current_room)
        #FOYER
        elif new_player.current_room == foyer:
            print("\n---- LET US GO NORTH ----\n")
            new_player.current_room = overlook
            print(new_player.current_room)
        #OVERLOOK
        elif new_player.current_room == overlook:
            print("\n----     YOU SHALL NOT PASS ----")
            print("---- CHOOSE ANOTHER DIRECTION ----\n")
            new_player.current_room = overlook
            print(new_player.current_room)
        #NARROW
        elif new_player.current_room == narrow:
            print("\n---- LET US GO NORTH ----\n")
            new_player.current_room = treasure
            print(new_player.current_room)
        #TREASURE
        elif new_player.current_room == treasure:
            print("\n----    YOU SHALL NOT PASS ----")
            print("---- CHOOSE ANOTHER DIRECTION ----\n")
            new_player.current_room = treasure
            print(new_player.current_room)
    elif user_prompt.lower() == 's':
        #OUTSIDE
        if new_player.current_room == outside:
            print("\n----    YOU SHALL NOT PASS ----")
            print("---- CHOOSE ANOTHER DIRECTION ----\n")
            new_player.current_room = outside
            print(new_player.current_room)
        #FOYER
        elif new_player.current_room == foyer:
            print("\n---- LET US GO SOUTH ----\n")
            new_player.current_room = outside
            print(new_player.current_room)
        #OVERLOOK
        elif new_player.current_room == overlook:
            print("\n---- LET US GO SOUTH ----\n")
            new_player.current_room = foyer
            print(new_player.current_room)
        #NARROW
        elif new_player.current_room == narrow:
            print("\n----   YOU SHALL NOT PASS ----")
            print("---- CHOOSE ANOTHER DIRECTION ----\n")
            new_player.current_room = narrow
            print(new_player.current_room)
        #TREASURE
        elif new_player.current_room == treasure:
            print("\n---- LET US GO SOUTH ----\n")
            new_player.current_room = narrow
            print(new_player.current_room)
    elif user_prompt.lower() == 'e':
        #OUTSIDE
        if new_player.current_room == outside:
            print("\n----    YOU SHALL NOT PASS ----")
            print("---- CHOOSE ANOTHER DIRECTION ----\n")
            new_player.current_room = outside
            print(new_player.current_room)
        #FOYER
        elif new_player.current_room == foyer:
            print("\n---- LET US GO EAST ----\n")
            new_player.current_room = narrow
            print(new_player.current_room)
        #OVERLOOK
        elif new_player.current_room == overlook:
            print("\n----    YOU SHALL NOT PASS ----")
            print("---- CHOOSE ANOTHER DIRECTION ----\n")
            new_player.current_room = overlook
            print(new_player.current_room)
        #NARROW
        elif new_player.current_room == narrow:
            print("\n----    YOU SHALL NOT PASS ----")
            print("---- CHOOSE ANOTHER DIRECTION ----\n")
            new_player.current_room = narrow
            print(new_player.current_room)
        #TREASURE
        elif new_player.current_room == treasure:
            print("\n----    YOU SHALL NOT PASS ----")
            print("---- CHOOSE ANOTHER DIRECTION ----\n")
            new_player.current_room = treasure
            print(new_player.current_room)
    elif user_prompt.lower() == 'w':
        #OUTSIDE
        if new_player.current_room == outside:
            print("\n----    YOU SHALL NOT PASS ----")
            print("---- CHOOSE ANOTHER DIRECTION ----\n")
            new_player.current_room = outside
            print(new_player.current_room)
        #FOYER
        elif new_player.current_room == foyer:
            print("\n----    YOU SHALL NOT PASS ----")
            print("---- CHOOSE ANOTHER DIRECTION ----\n")
            new_player.current_room = foyer
            print(new_player.current_room)
        #OVERLOOK
        elif new_player.current_room == overlook:
            print("\n----    YOU SHALL NOT PASS ----")
            print("---- CHOOSE ANOTHER DIRECTION ----\n")
            new_player.current_room = overlook
            print(new_player.current_room)
        #NARROW
        elif new_player.current_room == narrow:
            print("\n---- LET US GO WEST ----\n")
            new_player.current_room = foyer
            print(new_player.current_room)
        #TREASURE
        elif new_player.current_room == treasure:
            print("\n----    YOU SHALL NOT PASS ----")
            print("---- CHOOSE ANOTHER DIRECTION ----\n")
            new_player.current_room = treasure
            print(new_player.current_room)
    # If the user enters "q", quit the game
    elif user_prompt.lower() == 'q':
        print("Thank you for playing \nGoodbye!")
        break
    # Print an error message if the movement isn't allowed.
    else: 
        print("---- INVALID COMMAND ----")
        print("PLEASE SELECT FROM:  n, s, e, w or q")
