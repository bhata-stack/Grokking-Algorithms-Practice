class linkedlist:
    def __init__(self, data=None):
        if data:
            for i in range(len(data) - 1):
                data[i] = node(data[i])
                data[i].next = node(data[i+1])
            data[-1] = node(data[-1])
            self.head = data[0]
        else:
            self.head = None

    def __repr__(self):
        current_node = self.head
        nodes = []
        while current_node:
            nodes.append(current_node.data)
            current_node = current_node.next
        return str(nodes)


class node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return str(self.data)

if __name__ == "__main__":
    a = linkedlist([1, 2, 3, 4, 5])
    print(a.head.next.next)
