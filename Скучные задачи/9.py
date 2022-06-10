class main:
    def __init__(self):
        self.condition = 'A'

    def smash(self):
        if self.condition == 'A':
            self.condition = 'B'
            return 0
        elif self.condition == 'B':
            self.condition = 'C'
            return 3
        elif self.condition == 'E':
            self.condition = 'F'
            return 7
        elif self.condition == 'F':
            self.condition = 'G'
            return 8
        else:
            raise KeyError

    def mix(self):
        if self.condition == 'A':
            self.condition = 'C'
            return 1
        elif self.condition == 'C':
            self.condition = 'D'
            return 4
        elif self.condition == 'D':
            self.condition = 'A'
            return 6
        else:
            raise KeyError

    def rig(self):
        if self.condition == 'A':
            self.condition = 'E'
            return 2
        elif self.condition == 'D':
            self.condition = 'E'
            return 5
        elif self.condition == 'G':
            self.condition = 'B'
            return 9
        else:
            raise KeyError
