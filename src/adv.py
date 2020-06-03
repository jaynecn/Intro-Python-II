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


# CREATE VARIABLES FOR ROOMS
outside = room['outside']
foyer = room['foyer']
overlook = room['overlook']
narrow = room['narrow']
treasure = room['treasure']


# ADD ITEMS TO ROOMS
axe = Item("Axe", "by jove, it is sharp")
outside.stealthy_add(axe)

compass = Item("Compass", "weathered, but still works")
foyer.stealthy_add(compass)

binoculars = Item("Binoculars", "handy for spying")
overlook.stealthy_add(binoculars)

torch = Item("Torch", "batteries running low")
narrow.stealthy_add(torch)

gold = Item("Gold", "a small canvas sack filled with gold coins, they are worth a fortune!")
treasure.stealthy_add(gold)

knife = Item("Knife", "pocket knife, could be hidden in your socks")
new_player.stealthy_add(knife)

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
        
    # USER PROMPT
        
    # * Waits for user input and decides what to do        
    user_prompt = (input("\n---- WHAT NOW ? ---- \n[n], [s], [e] or [w] to move\n\n[look] to search room\n[inv] to see your stash\n[grab] [item] to grab\n[drop] [item] to drop\n[q] to quit:  "))
    
    
    # If the user enters a cardinal direction, attempt to move to the room there.
    
    # NORTH
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
    # SOUTH
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
    # EAST
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
    # WEST
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
    # LOOK
    elif user_prompt.lower() == 'look':
        #OUTSIDE
        if new_player.current_room == outside:
            outside.room_inventory()
        # FOYER
        elif new_player.current_room == foyer:
            foyer.room_inventory()
        # OVERLOOK
        elif new_player.current_room == overlook:
            overlook.room_inventory()
        # NARROW
        elif new_player.current_room == narrow:
            narrow.room_inventory()
        # TREASURE
        elif new_player.current_room == treasure:
            treasure.room_inventory()
    # INV
    elif user_prompt.lower() == 'inv':
        new_player.player_inventory()
        
    # ITEM ONLY
    
    # AXE
    elif user_prompt.lower() == 'axe':
        typed_item = user_prompt.lower()
        
        player_items = [f"{data.name.lower()}" for data in new_player.player_items]
        
        if typed_item in player_items:
            print(f"\n\tWhat do you want me to do with {typed_item}? \n\tYou need to tell me!!\n")
        else:
            print(f"\n\tIf you want to do something with {typed_item}, YOU NEED TO GO FIND IT FIRST!!!!")
    # COMPASS
    elif user_prompt.lower() == 'compass':
        typed_item = user_prompt.lower()
        
        player_items = [f"{data.name.lower()}" for data in new_player.player_items]
        
        if typed_item in player_items:
            print(f"\n\tWhat do you want me to do with {typed_item}? \n\tYou need to tell me!!\n")
        else:
            print(f"\n\tIf you want to do something with {typed_item}, YOU NEED TO GO FIND IT FIRST!!!!")
    # BINOCULARS
    elif user_prompt.lower() == 'binoculars':
        typed_item = user_prompt.lower()
        
        player_items = [f"{data.name.lower()}" for data in new_player.player_items]
        
        if typed_item in player_items:
            print(f"\n\tWhat do you want me to do with {typed_item}? \n\tYou need to tell me!!\n")
        else:
            print(f"\n\tIf you want to do something with {typed_item}, YOU NEED TO GO FIND IT FIRST!!!!")
    # TORCH
    elif user_prompt.lower() == 'torch':
        typed_item = user_prompt.lower()
        
        player_items = [f"{data.name.lower()}" for data in new_player.player_items]
        
        if typed_item in player_items:
            print(f"\n\tWhat do you want me to do with {typed_item}? \n\tYou need to tell me!!\n")
        else:
            print(f"\n\tIf you want to do something with {typed_item}, YOU NEED TO GO FIND IT FIRST!!!!")
    # GOLD
    elif user_prompt.lower() == 'gold':
        typed_item = user_prompt.lower()
        
        player_items = [f"{data.name.lower()}" for data in new_player.player_items]
        
        if typed_item in player_items:
            print(f"\n\tWhat do you want me to do with {typed_item}? \n\tYou need to tell me!!\n")
        else:
            print(f"\n\tIf you want to do something with {typed_item}, YOU NEED TO GO FIND IT FIRST!!!!")
    # KNIFE
    elif user_prompt.lower() == 'knife':
        typed_item = user_prompt.lower()
        
        player_items = [f"{data.name.lower()}" for data in new_player.player_items]
        
        if typed_item in player_items:
            print(f"\n\t>> What do you want me to do with {typed_item}? \n\t>> YOU NEED TO TELL ME!!\n")
        else:
            print(f"\n\t>> If you want to do something with {typed_item}, YOU NEED TO GO FIND IT FIRST!!!!")
        
    # VERB NOUN
    
    # GRAB ONLY
    if user_prompt.lower() == 'grab':
        print("\n\tGRAB WHAT..?\nYou need to tell me!!\n")
    
    # GRAB
    elif user_prompt.lower()[:4] == 'grab':
        # GRAB
        grab_separate_words = user_prompt.split(' ')
        command = grab_separate_words[0]
        item_to_grab = grab_separate_words[1].lower()
        
        current_room_items = [f"{data.name.lower()}" for data in new_player.current_room.room_items]
        
        if item_to_grab in current_room_items:
            print(f"\n\t>> YOU GRAB: {item_to_grab}")
            if item_to_grab == 'axe':
                new_player.add_player_item(axe)
            elif item_to_grab == 'compass':
                new_player.add_player_item(compass)
            elif item_to_grab == 'binoculars':
                new_player.add_player_item(binoculars)
            elif item_to_grab == 'torch':
                new_player.add_player_item(torch)
            elif item_to_grab == 'gold':
                new_player.add_player_item(gold)
            elif item_to_grab == 'knife':
                new_player.add_player_item(knife)  
        else:
            print("\nThat item is not found here!!\nSearch for it elsewhere\n")

    # DROP ONLY
    elif user_prompt.lower() == 'drop':
        print("\n\tDROP WHAT..?\nYou need to specify - I'm not psychic!\n")
    
    # DROP
    elif user_prompt.lower()[:4] == 'drop':
        print("\nDrop!")
        # new_player.drop_player_item(knife)
        grab_separate_words = user_prompt.split(' ')
        command = grab_separate_words[0]
        item_to_grab = grab_separate_words[1].lower()
        
        current_room_items = [f"{data.name.lower()}" for data in new_player.player_items]
        
        if item_to_grab in current_room_items:
            print(f"\t>> YOU DROP: {item_to_grab}")
            if item_to_grab == 'axe':
                new_player.drop_player_item(axe)
            elif item_to_grab == 'compass':
                new_player.drop_player_item(compass)
            elif item_to_grab == 'binoculars':
                new_player.drop_player_item(binoculars)
            elif item_to_grab == 'torch':
                new_player.drop_player_item(torch)
            elif item_to_grab == 'gold':
                new_player.drop_player_item(gold)
            elif item_to_grab == 'knife':
                new_player.drop_player_item(knife)    
        else:
            print("\nThat item is not found here!!\nSearch for it elsewhere\n")
    
    # If the user enters "q", quit the game
    elif user_prompt.lower() == 'q':
        print("Thank you for playing \nGoodbye!")
        break
    # Print an error message if the movement isn't allowed.
    else: 
        print("\n---- INVALID COMMAND ----")
        print("PLEASE SELECT FROM:  n, s, e, w or q\n")
