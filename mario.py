class Mario:
    def __init__(self):
        self.x_cordinat = 0
        self.y_cordinat = 29
        self.move_left = False
        self.move_right = False
        self.jump_count = 0
        self.jump = False
        self.access_to_jump = True

    def update(self):
        if(self.move_left and self.x_cordinat > 0):
            self.x_cordinat -= 0.01
        if(self.move_right and self.x_cordinat < 31):
            self.x_cordinat += 0.01
        if(self.y_cordinat < 30 and not self.jump):
            self.y_cordinat += 0.01
        if(self.jump):
            self.access_to_jump = False
            self.y_cordinat -= 0.01
            self.jump_count += 1
            if(self.jump_count == 500):
                self.jump_count = 0
                self.jump = False
        if(self.y_cordinat == 29):
            self.access_to_jump = True

