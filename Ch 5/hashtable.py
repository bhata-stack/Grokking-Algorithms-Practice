import numpy as np

class hashtable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.data = [None] * self.capacity
    
    def __repr__(self):
        output_arr = [[] for i in range(len(self.data))]
        for i in range(len(self.data)):
            current_node = self.data[i]
            while current_node:
                output_arr[i].append((str(current_node)))
                current_node = current_node.next
        return str(output_arr)

    def insert(self, key, value):
        self.size += 1
        ind = self.hash(key)
        if self.data[ind] is None:
            self.data[ind] = node(key, value)
            return
        else:
            current_node = self.data[ind]
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node(key, value)
            return


    def hash(self, key):
        # A basic hash function used for this simple implementation
        ind_sum = 0
        for ind, c in enumerate(key):
            ind_sum += (ind + len(key)) ** ord(c)
            ind_sum = ind_sum % self.capacity
        return ind_sum
    
    
    

class node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return "{}: {}".format(str(self.key), str(self.value))


if __name__ == "__main__":
    table = hashtable(20)
    for i in range(30):
        table.insert(str(i), round(np.random.rand(), 2))
    print(table)
