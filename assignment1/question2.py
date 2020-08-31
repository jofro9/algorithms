# Joe Froelicher
# CSCI 3412 - Algorithms
# Dr. Mazen al Borno

import random

# Question 2
class RandomInteger:
    def A(self):
        return random.randint(0, 5)

    def B(self):
        return random.randint(0, 8)

    def useBforA(self):
        A_val = self.B()

        while A_val > 5:
            A_val = self.B()

        return A_val

    def useAforB(self):
        useful = False

        while not useful:
            B1 = self.A()
            B2 = self.A()

            while B1 > 4:
                B1 = self.A()

            while B2 > 4:
                B2 = self.A()

            if abs(B1 - B2) < 2:
                useful = True
                # break

        return B1 + B2


# Part A
A_rand = RandomInteger()
print("\nA's random value is: " + str(A_rand.A()))

# Part B
B_rand = RandomInteger()
print("B's random value is: " + str(B_rand.B()))

# Part C
print("A's new value using B is: " + str(A_rand.useBforA()))

# Part D
print("B's new value using A is: " + str(B_rand.useAforB()) + "\n")
