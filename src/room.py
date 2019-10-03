# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, text):
        self.name = name
        self.text = text
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return '{self.name}:\n\n{self.text}'.format(self=self)
