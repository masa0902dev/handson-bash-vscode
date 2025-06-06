class Particle:
    def __init__(self, pid, x, y, vx, vy, radius=0.015):
        self.id = pid
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = radius
        self.collision_count = 0

    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

    def position(self):
        return self.x, self.y

    def velocity(self):
        return self.vx, self.vy
