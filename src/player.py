# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item

class Player:
    # constructor function
    def __init__(self, name, room):
        self.name = name
        self.current_room = room
        self.player_items = []
        
    # string value
    def __str__(self):
        return f"{self.name} is currently located: {self.current_room.name}"
    
    def add_player_item(self, item):
        self.item = item
        self.player_items.append(item)
        for i in self.player_items:
            print(f"{i.name} added to {self.name}'s stash")
    
    def player_inventory(self):
        if (len(self.player_items) >= 1):
            print(f"\n>> Here is what you have on your person:")
            for i in self.player_items:
                print(f"\t{i}")
        else:
            print(f"\n>> You dont have anything on your person.\nLook in rooms!\n")
            
    pass



