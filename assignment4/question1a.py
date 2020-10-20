import math

def myHash(key):
    return math.trunc(((math.trunc(key) + 6) ** 3 / 17 + key) % 13)

class HashTable:
    def __init__(self, length, keys):
        self.hashtable = [None] * length
        self.keys = keys

    def hashValues(self):
        temp = [None] * len(self.keys)

        for i in range(len(self.keys)):
            temp[i] = myHash(self.keys[i])

        for i in range(len(temp)):
            if self.hashtable[temp[i]] == None:
                self.hashtable[temp[i]] = [keys[i]]
            else:
                self.hashtable[temp[i]].insert(0, keys[i])

    def output(self):
        for i in range(len(self.hashtable)):
            print("Value: " + str(i) + ", Keys: " + str(self.hashtable[i]))

keys = [43, 22, 1, 0, 15, 31, 99, 218, 4, 7, 11, 3, 9]

H = HashTable(len(keys), keys)

H.hashValues()
H.output()

