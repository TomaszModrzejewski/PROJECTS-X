import math

class Sphere:
    """
    A class to represent a sphere.

    Attributes:
    -----------
    radius : float
        The radius of the sphere.
    """

    def __init__(self, radius):
        """
        Constructs all the necessary attributes for the sphere object.

        Parameters:
        -----------
            radius (float): The radius of the sphere. Must be non-negative.
        """
        if radius < 0:
            raise ValueError("Radius cannot be negative.")
        self.radius = radius

    def diameter(self):
        """Calculates the diameter of the sphere."""
        return self.radius * 2

    def surface_area(self):
        """Calculates the surface area of the sphere."""
        return 4 * math.pi * (self.radius ** 2)

    def volume(self):
        """Calculates the volume of the sphere."""
        return (4/3) * math.pi * (self.radius ** 3)

    def __repr__(self):
        """Provides a developer-friendly string representation of the sphere."""
        return f"Sphere(radius={self.radius})"

# Example of how to use the Sphere class
if __name__ == "__main__":
    try:
        # Create a sphere with a radius of 5
        my_sphere = Sphere(5)
        print(f"Created Sphere: {my_sphere}")
        print(f"Diameter: {my_sphere.diameter()}")
        print(f"Surface Area: {my_sphere.surface_area():.2f}")
        print(f"Volume: {my_sphere.volume():.2f}")

    except ValueError as e:
        print(f"Error: {e}")