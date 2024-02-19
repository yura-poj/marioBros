class Mario:
    def __init__(self):
        self.x_cordinat = 0
        self.y_cordinat = 31
        self.move_left = False
        self.move_right = False
    def update(self):
        if(self.move_left and self.x_cordinat > 0):
            self.x_cordinat -= 0.01
        if(self.move_right and self.x_cordinat < 31):
            self.x_cordinat += 0.01


