class stack:
    def __init__(self):
        self.data = []

    def add(self, element):
        self.data.append(element)

    def remove(self):
        return self.data.pop(-1)

    def __repr__(self):
        return str(self.data)


if __name__ == "__main__":
    test_stack = stack()
    for i in range(6):
        test_stack.add(i**2)
    print(test_stack)
    item = test_stack.remove()
    print(item)
    print(test_stack)
    