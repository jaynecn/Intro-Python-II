# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    # construction function
    def __init__(self, name, description):
       self.name = name
       self.description = description
    
    def __str__(self):
        return f"room name is {self.name}" 
    
    def add_item(self, item):
        self.item = item
    pass
