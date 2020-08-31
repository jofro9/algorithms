# Joe Froelicher
# CSCI 3412 - Algorithms
# Dr. Mazen al Borno

import math

# Question 3

def triangleArea(beta, alpha):
    return beta * alpha

alpha = 0.5 * math.sqrt(2.)
area = alpha * alpha # value to updated
print("Current Area: " + str(area))

# target area (pi * 0.5 ^ 2), to three digits
TARGET_AREA = 0.785
RADIUS = 0.5
triangles = 4
correct = False

while not correct:
    alpha = alpha / 2.
    beta = math.sqrt( (RADIUS * RADIUS) - (alpha * alpha) )
    triangle_area = triangleArea(beta, alpha)

    area = area + (triangles * triangle_area)

    print(
        "Area: " + str(area) +
        ", alpha: " + str(alpha) +
        ", beta: " + str(beta) +
        ", triangle area: " + str(triangle_area)
    )

    triangles = 2 * triangles


    if (TARGET_AREA - area) < 0.001:
        correct = True
    else:
        continue
