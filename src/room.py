# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room:
    # construction function
    def __init__(self, name, description):
       self.name = name
       self.description = description
       self.room_items = []
    
    def __str__(self):
        return f"room name is {self.name}"
    
    def stealthy_add(self, item):
        self.item = item
        # seitem = Item(item_name, item_description)
        self.room_items.append(item)
    
    def add_room_item(self, item):
        self.item = item
        self.room_items.append(item)
        for i in self.room_items:
            print(f"{i.name} added to {self.name}")
        
    def room_inventory(self):
        if (len(self.room_items) == 0):
            return f"There's nothing in this room. That sucks.  Search other rooms!"
        elif (len(self.room_items) > 0):
            print(f"\nLook what you found in the {self.name}:\n")
            for i in self.room_items:
                print(f"{i}")
            
            
        
    
    # def add_item(self, item):
    #     self.item = item
    pass
