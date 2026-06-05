class Graph:
    def __init__(self):
        self.graph_dict = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph_dict[u] = []
        if v not in self.graph:
            self.graph [v] = []
        self.graph_dict[u].append(v)
        self.graph_dict[v].append(u)

    def print_graph(self):
        print(self.graph)

g = Graph()
g.add_edge("a", "b")
g.add_edge("a", "c")
g.print_graph()