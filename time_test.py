import time

fps = time.sleep(1/60)



class PhysicsSimulation:

    def __init__(self, initial_position):

        self.position = initial_position

        self.velocity = 0  # meters per second



    def update(self, time):

        self.position += self.velocity * time



# Example usage

simulation = PhysicsSimulation(0)  # Initial position is 0 meters

time = 5  # Time in seconds

simulation.update(time)

print("Final position:", simulation.position, "meters")

