# Joe Froelicher
# CSCI 3412 - Algorithms
# Dr. Mazen al Borno

# Question 1

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
