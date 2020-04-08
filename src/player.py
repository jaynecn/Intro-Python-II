# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    # constructor function
    def __init__(self, name, room):
        self.name = name
        self.current_room = room
        
    # string value
    def __str__(self):
        return f"{self.name} is in {self.current_room.name}"
    pass

