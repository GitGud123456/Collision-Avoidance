







# handles collisions between and object and canvas walls
def collision(self,size):
            if self.x + self.r > size[0]:
                var = (self.x + self.r) - size[0]
                self.x -= var
                self.xV = -1 * self.xV 
            elif self.x - self.r < 0:
                var = (self.x - self.r)
                self.x -= var
                self.xV = -1 * self.xV
            if self.y + self.r > size[1]:
                var = (self.y + self.r) - size[1]
                self.y -= var
                self.yV = -1 * self.yV
            elif self.y - self.r < 0:
                var = (self.y - self.r)
                self.y -= var
                self.yV = -1 * self.yV



# detects if to circles collided returns bool
def collide(self, other_circle):
            dx = self.x - other_circle.x
            dy = self.y - other_circle.y
            distance = (dx * dx + dy * dy)**0.5
            if distance - other_circle.r < self.r:
                return True
            else:
                return False