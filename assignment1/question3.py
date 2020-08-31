# Joe Froelicher
# CSCI 3412 - Algorithms
# Dr. Mazen al Borno
# 9/8/2020
# Assignment 1

import math

# Question 3
class UnitCircle:
    def __init__(self):
        self.TARGET_AREA_ = 3.14
        self.RADIUS_ = 1.
        self.triangles_ = 4.
        self.iter = 0

    ### member functions for use throughout code ###
    # gamma function for pythagorean long side of right triangle formed by splitting the isosceles in half
    def Gamma(self, alpha, beta):
        return math.sqrt( (alpha ** 2) + (beta ** 2) )

    # distance from centroid to the side calculated by gamma
    def Altitude(self, gamma):
        return math.sqrt( (self.RADIUS_ ** 2) - ((gamma / 2.) ** 2) )

    # area of all of the isosceles trianlges for the current iteration,
    # update the number of triangles for the next iteration
    def TriangleArea(self, alpha, beta):
        t_area = alpha * beta * self.triangles_
        self.triangles_ *= 2
        return t_area

    def PrintTriangle(self, alpha, beta, gamma, area, altitude):
        if self.iter == 0.:
            triangles = 0
        else:
            triangles = self.triangles_
        print(
            "\nIteration #" + str(self.iter) + "\n" + "___________________________________\n"
            "\nCurrent area: " + str(area) +
            "\nNumber of triangles: " + str(int(triangles / 2)) +
            "\nalpha: " + str(alpha) +
            "\nbeta: " + str(beta) +
            "\ngamma: " + str(gamma) +
            "\naltitude: " + str(altitude)
        )

        self.iter += 1

# New unit Circle Object
unit_circle = UnitCircle()

### init values (0th iteration)
alpha = unit_circle.RADIUS_ * math.sqrt(2.) / 2. # straight distance to farthes inscribe geometry
beta = unit_circle.RADIUS_ - alpha
area = (2. * alpha) ** 2
gamma = 0.
altitude = 0.

unit_circle.PrintTriangle(alpha, beta, gamma, area, altitude)

# 1st iteration, slightly different calculation than the rest
t_area = unit_circle.TriangleArea(alpha, beta)
area += t_area
gamma = unit_circle.Gamma(alpha, beta)
altitude = unit_circle.Altitude(gamma)
unit_circle.PrintTriangle(alpha, beta, gamma, area, altitude)

while (unit_circle.TARGET_AREA_ - area) > 0.001:
    beta = gamma / 2.
    alpha = unit_circle.RADIUS_ - altitude
    t_area = unit_circle.TriangleArea(alpha, beta)
    area += t_area
    gamma = unit_circle.Gamma(alpha, beta)
    altitude = unit_circle.Altitude(gamma)
    unit_circle.PrintTriangle(alpha, beta, gamma, area, altitude)
