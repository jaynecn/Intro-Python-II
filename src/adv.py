from room import Room
from player import Player
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
directions = ['n', 's', 'e', 'w']

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
    user_prompt = (input("---- WHERE DO YOU WANT TO GO ? ---- \n Type n, s, e or w OR quit (q):  "))
    
    # JAYNE: USER_PROMPT IS A STRING
    
    # If the user enters a cardinal direction, attempt to move to the room there.
    
    if user_prompt.lower() == 'n':
        #OUTSIDE
        if new_player.current_room.name == 'Outside Cave Entrance':
            print("---- LET US GO NORTH ----")
            new_player = Player("Jayne", room['foyer'])
            print(new_player.current_room)
        #FOYER
        elif new_player.current_room.name == 'Foyer':
            print("---- LET US GO NORTH ----")
            new_player = Player("Jayne", room['overlook'])
            print(new_player.current_room)
        #OVERLOOK
        elif new_player.current_room.name == 'Grand Overlook':
            print("----     YOU SHALL NOT PASS ----")
            print("---- CHOOSE ANOTHER DIRECTION ----")
            new_player = Player("Jayne", room['overlook'])
            print(new_player.current_room)
        #NARROW
        elif new_player.current_room.name == 'Narrow Passage':
            print("---- LET US GO NORTH ----")
            new_player = Player("Jayne", room['treasure'])
            print(new_player.current_room)
        #TREASURE
        elif new_player.current_room.name == 'Treasure Chamber':
            print("----    YOU SHALL NOT PASS ----")
            print("---- CHOOSE ANOTHER DIRECTION ----")
            new_player = Player("Jayne", room['treasure'])
            print(new_player.current_room)
    elif user_prompt.lower() == 's':
        #OUTSIDE
        if new_player.current_room.name == 'Outside Cave Entrance':
            print("----    YOU SHALL NOT PASS ----")
            print("---- CHOOSE ANOTHER DIRECTION ----")
            new_player = Player("Jayne", room['outside'])
            print(new_player.current_room)
        #FOYER
        elif new_player.current_room.name == 'Foyer':
            print("---- LET US GO SOUTH ----")
            new_player = Player("Jayne", room['outside'])
            print(new_player.current_room)
        #OVERLOOK
        elif new_player.current_room.name == 'Grand Overlook':
            print("---- LET US GO SOUTH ----")
            new_player = Player("Jayne", room['foyer'])
            print(new_player.current_room)
        #NARROW
        elif new_player.current_room.name == 'Narrow Passage':
            print("----   YOU SHALL NOT PASS ----")
            print("---- CHOOSE ANOTHER DIRECTION ----")
            new_player = Player("Jayne", room['narrow'])
            print(new_player.current_room)
        #TREASURE
        elif new_player.current_room.name == 'Treasure Chamber':
            print("---- LET US GO SOUTH ----")
            new_player = Player("Jayne", room['narrow'])
            print(new_player.current_room)
    elif user_prompt.lower() == 'e':
        #OUTSIDE
        if new_player.current_room.name == 'Outside Cave Entrance':
            print("----    YOU SHALL NOT PASS ----")
            print("---- CHOOSE ANOTHER DIRECTION ----")
            new_player = Player("Jayne", room['outside'])
            print(new_player.current_room)
        #FOYER
        elif new_player.current_room.name == 'Foyer':
            print("---- LET US GO EAST ----")
            new_player = Player("Jayne", room['narrow'])
            print(new_player.current_room)
        #OVERLOOK
        elif new_player.current_room.name == 'Grand Overlook':
            print("----    YOU SHALL NOT PASS ----")
            print("---- CHOOSE ANOTHER DIRECTION ----")
            new_player = Player("Jayne", room['overlook'])
            print(new_player.current_room)
        #NARROW
        elif new_player.current_room.name == 'Narrow Passage':
            print("----    YOU SHALL NOT PASS ----")
            print("---- CHOOSE ANOTHER DIRECTION ----")
            new_player = Player("Jayne", room['narrow'])
            print(new_player.current_room)
        #TREASURE
        elif new_player.current_room.name == 'Treasure Chamber':
            print("----    YOU SHALL NOT PASS ----")
            print("---- CHOOSE ANOTHER DIRECTION ----")
            new_player = Player("Jayne", room['treasure'])
            print(new_player.current_room)
    elif user_prompt.lower() == 'w':
        #OUTSIDE
        if new_player.current_room.name == 'Outside Cave Entrance':
            print("----    YOU SHALL NOT PASS ----")
            print("---- CHOOSE ANOTHER DIRECTION ----")
            new_player = Player("Jayne", room['outside'])
            print(new_player.current_room)
        #FOYER
        elif new_player.current_room.name == 'Foyer':
            print("----    YOU SHALL NOT PASS ----")
            print("---- CHOOSE ANOTHER DIRECTION ----")
            new_player = Player("Jayne", room['foyer'])
            print(new_player.current_room)
        #OVERLOOK
        elif new_player.current_room.name == 'Grand Overlook':
            print("----    YOU SHALL NOT PASS ----")
            print("---- CHOOSE ANOTHER DIRECTION ----")
            new_player = Player("Jayne", room['overlook'])
            print(new_player.current_room)
        #NARROW
        elif new_player.current_room.name == 'Narrow Passage':
            print("---- LET US GO WEST ----")
            new_player = Player("Jayne", room['foyer'])
            print(new_player.current_room)
        #TREASURE
        elif new_player.current_room.name == 'Treasure Chamber':
            print("----    YOU SHALL NOT PASS ----")
            print("---- CHOOSE ANOTHER DIRECTION ----")
            new_player = Player("Jayne", room['treasure'])
            print(new_player.current_room)
    # If the user enters "q", quit the game
    elif user_prompt.lower() == 'q':
        print("Thank you for playing \nGoodbye!")
        break
    # Print an error message if the movement isn't allowed.
    else: 
        print("---- INVALID COMMAND ----")
        print("PLEASE SELECT FROM:  n, s, e, w or q")
