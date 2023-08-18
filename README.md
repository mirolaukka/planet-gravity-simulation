# Planet-Moon Gravity Simulation

This is a simple Python simulation that uses the Pygame library to visualize the gravitational interaction between a planet and its moon. In this simulation, you can observe the moon's orbit around the planet due to their gravitational attraction.

## Features

- Visualizes the motion of a moon orbiting around a planet under the influence of gravity.
- Simulates gravitational forces and updates the positions of celestial bodies using Euler's method.
- Displays the path of the moon over time as it orbits the planet.

## How It Works

The simulation creates two instances of the `CelestialBody` class, representing the planet and the moon. Each `CelestialBody` object has properties like position, mass, velocity, and a path to track its movement.

The main loop of the simulation calculates the gravitational force between the planet and the moon using Newton's law of universal gravitation. It then updates the moon's velocity and position using Euler's method based on the calculated force.

The moon's path is also updated to keep track of its trajectory. The path is limited to a certain number of points for performance reasons.

The Pygame library is used to create a graphical display where the planet, moon, and path are drawn on the screen. The display is updated in each iteration of the main loop to show the evolving motion of the moon around the planet.

## Constants and Customization

- `SCREEN_WIDTH` and `SCREEN_HEIGHT`: The dimensions of the simulation window.
- `BACKGROUND_COLOR`: The background color of the simulation.
- `PATH_COLOR`: The color of the path traced by the moon.
- `PLANET_COLOR`: The color of the planet.
- `MOON_COLOR`: The color of the moon.
- `GRAVITATIONAL_CONSTANT`: The constant used to calculate gravitational force.

## Acknowledgments

This simulation is a simplified representation of gravitational interactions and serves as an educational tool to visualize orbital mechanics.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify the code for your own educational purposes.


### Work-in-progress