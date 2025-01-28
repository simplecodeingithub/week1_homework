# Importing the math module to use math functions like tan, cos, and radians
import math

# Constants (fixed values)
g = 9.81  # Gravity: The force that pulls the projectile down (m/s^2)
y0 = 1    # Initial height of the projectile when it's launched (m)
x = 0.5   # Horizontal distance the projectile travels (m)
v0 = 44   # Initial velocity: How fast the projectile is launched (m/s)
theta_deg = 80  # Angle of launch: The direction at which the projectile is launched (degrees)

# Convert angle from degrees to radians manually using the formula
theta = theta_deg * (math.pi / 180)
print(math.pi)
print(theta) #print the value in radians
print("The value of theta is: {:.2f}".format(theta)) # Format the result to 2 decimal places

# # Using math.radians() function to convert the angle from degrees to radians
# theta = math.radians(theta_deg)
# print(theta)

# The formula calculates the height of the projectile at a given horizontal distance (x),
# considering the initial height (y0), launch angle (theta), initial velocity (v0), and gravity (g).
y = y0 + x * math.tan(theta) - (g * x**2) / (2 * (v0 * math.cos(theta))**2)

# Print the result: The height of the projectile at the given horizontal distance (x)
# converts y to string and concatenates and print the result as a string
print("The height of the projectile is: " + str(y))
# Format the result to 2 decimal places
print("The height of the projectile is: {:.2f}".format(y))

# tan(θ): Helps calculate the vertical distance (height) of the projectile based on the launch angle.
# cos(θ): Helps calculate the horizontal motion of the projectile and is used in the formula to account for gravity’s effect on the projectile.