class queue:
    def __init__(self, data):
        self.data = data
    
    def insert(self, point):
        self.data.append(point)
    
    def remove(self):
        return self.data.pop(0)
    
    def __repr__(self):
        return str(self.data)

if __name__ == "__main__":
    test_queue = queue([1, 2, 3, 4])
    print(test_queue)
    test_queue.insert(12)
    print(test_queue.remove())
    print(test_queue)
        