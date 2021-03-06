"""Euler method for solving statment"""
from simulation.numericmethods.base import NumericMethod

class Euler(NumericMethod):
    """Solving equation using Euler method"""
    def __init__(self):
        super(Euler, self).__init__()

    def calculate(self, system, dt=0.1):
        """Main function returning dict of new system
        
        :param system: list of spaceobjects.
        :param dt: time step.
        :returns: new list of spaceobjects.
        """
        self.system = system
        new_system = list()
        for planet in self.system:
            axold, ayold = self.acceleration(planet)
            planet.x += planet.velocity_x * dt
            planet.y += planet.velocity_y * dt
            planet.velocity_x += axold * dt
            planet.velocity_y += ayold * dt
            new_system.append(planet)

        return new_system
