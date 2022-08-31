from collections import defaultdict

class graph:
    def __init__(self, edges):
        self.values = defaultdict(set)

        for node1, node2 in edges:
            self.values[node1].add(node2)
            self.values[node2].add(node1)
    
    def remove(self, point):
        for node, edges in self.values.items():
            try:
                edges.remove(node)
            except KeyError:
                pass
        try:
            del self.values[node]
        except KeyError:
            pass
    
    def connected(self, node1, node2):
        return node1 in self.values and node2 in self.values[node1]

    def search(self, value):
        if value in self.values:
            return True, dict(self.values)[value]
        else:
            return False, None
         
            
    def __str__(self):
        return str(dict(self.values))



if __name__ == "__main__":
    edges = [("A", "B"), ("D", "T"), ("C", "A"), ("E", "B"), ("D", "C"), ("C", "B")]
    graph_test = graph(edges)
    print(graph_test)
    print(graph_test.connected("A", "T"))
    print(graph_test.connected("A", "D"))
    print(graph_test.connected("D", "C"))

    print(graph_test.search("B"))
    print(graph_test.search("J"))