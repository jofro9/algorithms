# Joe Froelicher
# CSCI 3412 - Algorithms
# Dr. Mazen al Borno

import random

# initialize an empty list and fill
bulbs = []

for i in range(100):
    bulbs.append(False)

switches = len(bulbs)

# make sure initial list is what we are expecting
print("\nYou have created " + str(switches) + " light bulbs")

good_list = False
for i in range(len(bulbs)):
    if not bulbs[i]:
        good_list = True
    else:
        print("ERROR: at least one switch is on\n")

if good_list:
    print("All switches are off\n")

# Question 1 part A
people = 100

for person in range(people):
    on = 0
    off = 0

    for switch in range(person, switches, person + 1):
        if bulbs[switch]:
            bulbs[switch] = False
        elif not bulbs[switch]:
            bulbs[switch] = True

    for i in range(len(bulbs)):

        if bulbs[i]:
            on += 1

        elif not bulbs[i]:
            off += 1

    if person + 1 == 10 or person + 1 == 40 or person + 1 == 70 or person + 1 == 100:
        print("After person " + str(person + 1) + ", there are " + str(on) + " lights on, and " + str(off) + " lights off.")

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
                # Break

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

# Question 3
