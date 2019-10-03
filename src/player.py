# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self,
                 name,
                 current_room):
        self.name = name
        self.current_room = current_room

    def move(self, direction):

        dir_dict = {"n": 'n_to', "s": 's_to', "e": 'e_to', "w": 'w_to'}

        if direction in dir_dict:
            move_to = getattr(self.current_room, dir_dict[direction])
            if move_to is not None:
                self.current_room = move_to
            else:
                print("You can't move that way")
        else:
            print('Please select a valid direction: n, s, e, or w')
