import math

def myHash(key):
    return math.trunc(((math.trunc(key) + 6) ** 3 / 17 + key) % 13)

class Node():
    def __init__(self, key, prev, nex):
        self.key = key
        self.prev = prev
        self.nex = nex

class DoublyLinkedList():
    head = None
    tail = None

    def insertBefore(self, key):
        new_node = Node(key, None, None)

        new_node.next = self.head
        new_node.prev = None

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    def printNodes(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.key)
            current_node = current_node.next

class HashTable:
    def __init__(self, length, keys):
        self.hashtable = [None] * length
        self.keys = keys

    def hashValues(self):
        temp = [None] * len(self.keys)

        for i in range(len(self.keys)):
            temp[i] = myHash(self.keys[i])

        for i in range(len(temp)):
            double_list = DoublyLinkedList()

            if self.hashtable[temp[i]] == None:
                double_list.insertBefore(keys[i])
                self.hashtable[temp[i]] = double_list

            else:
                self.hashtable[temp[i]].insertBefore(keys[i])

    def output(self):
        j = 1

        for h in self.hashtable:
            print("Value: " + str(j))
            print("Keys: ")

            if h != None:
                h.printNodes()

            else:
                print(None)

            j += 1

keys = [43, 22, 1, 0, 15, 31, 99, 218, 4, 7, 11, 3, 9]

H = HashTable(len(keys), keys)

H.hashValues()

H.output()


