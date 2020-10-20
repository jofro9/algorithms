import math

def myHash(key):
    return math.trunc(((math.trunc(key) + 6) ** 3 / 17 + key) % 13)

class HashTable():
    def __init__(self, length, keys):
        self.hashtable = [None] * length
        self.keys = keys
        self.length = length

    def hashValues(self):
        temp = [None] * self.length

        for i in range(self.length):
            temp[i] = myHash(self.keys[i])

        for i in range(self.length):

            if self.hashtable[temp[i]] == None:
                self.hashtable[temp[i]] = keys[i]

            else:
                for j in range(self.length):
                    k = (temp[i] + j) % self.length

                    if self.hashtable[k] == None:
                        self.hashtable[k] = keys[i]
                        break

    def output(self):
        for i in range(len(self.hashtable)):
            print("Value: " + str(i) + ", Key: " + str(self.hashtable[i]))

keys = [43, 22, 1, 0, 15, 31, 99, 218, 4, 7, 11, 3, 9]

H = HashTable(len(keys), keys)

H.hashValues()
H.output()
