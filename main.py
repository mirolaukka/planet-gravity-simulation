import pygame
import sys
import math

# Initialize pygame
pygame.init()

# Constants for the simulation
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)
PATH_COLOR = (100, 100, 100)
PLANET_COLOR = (0, 128, 255)
MOON_COLOR = (255, 255, 255)
GRAVITATIONAL_CONSTANT = 0.1

# Define the CelestialBody class


class CelestialBody:
    def __init__(self, x, y, mass, velocity):
        self.x = x
        self.y = y
        self.mass = mass
        self.velocity = velocity
        self.path = []

    def update_path(self):
        self.path.append((self.x, self.y))
        if len(self.path) > 500:  # Limit the length of the path for performance
            self.path.pop(0)


# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Planet-Moon Gravity Simulation")

# Create celestial bodies
planet = CelestialBody(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 5000, [0, 0])
moon = CelestialBody(SCREEN_WIDTH // 2 + 150,
                     SCREEN_HEIGHT // 2, 50, [0, -1.5])

# Main loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate distance and direction
    dx = planet.x - moon.x
    dy = planet.y - moon.y
    distance = math.sqrt(dx ** 2 + dy ** 2)
    direction = [dx / distance, dy / distance]

    # Calculate gravitational force
    force_magnitude = (GRAVITATIONAL_CONSTANT *
                       planet.mass * moon.mass) / (distance ** 2)
    force = [force_magnitude * direction[0], force_magnitude * direction[1]]

    # Update moon's velocity using Euler's method
    moon.velocity[0] += force[0] / moon.mass
    moon.velocity[1] += force[1] / moon.mass

    # Update moon's position using Euler's method
    moon.x += moon.velocity[0]
    moon.y += moon.velocity[1]

    # Update moon's path
    moon.update_path()

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Draw moon's path
    for point in moon.path:
        pygame.draw.circle(screen, PATH_COLOR,
                           (int(point[0]), int(point[1])), 1)

    # Draw celestial bodies
    pygame.draw.circle(screen, PLANET_COLOR,
                       (int(planet.x), int(planet.y)), 40)
    pygame.draw.circle(screen, MOON_COLOR, (int(moon.x), int(moon.y)), 10)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
