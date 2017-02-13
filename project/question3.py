class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []

class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def reset(self):
        self.nodes = []
        self.edges = []

    def insert_node(self, new_node_val):
        new_node = Node(new_node_val)
        self.nodes.append(new_node)
        
    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        from_found = None
        to_found = None
        for node in self.nodes:
            if node_from_val == node.value:
                from_found = node
            if node_to_val == node.value:
                to_found = node
        if from_found == None:
            from_found = Node(node_from_val)
            self.nodes.append(from_found)
        if to_found == None:
            to_found = Node(node_to_val)
            self.nodes.append(to_found)
        new_edge = Edge(new_edge_val, from_found, to_found)
        from_found.edges.append(new_edge)
        to_found.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_edge_list(self):
        if self.edges:
            edge_tuples = []
            for e in self.edges:
                edge_tuples.append((e.value, e.node_from.value, e.node_to.value))
            return edge_tuples
            
        return []

    def get_adjacency_list(self):
        if self.nodes:
            adj_list = {}
            for n in self.nodes:
                e_list = []
                for e in n.edges:
                    if e.node_from.value == n.value:
                        e_list.append((e.node_to.value, e.value))
                    if e.node_to.value == n.value:
                        e_list.append((e.node_from.value, e.value))
                if e_list != []:
                    adj_list[n.value] = e_list
            return adj_list
        return {}

def find(graph, parents, node):
    if parents[node] == None:
        return node
    else:
        return find(graph, parents, parents[node])

def union(graph, parents, node1, node2):
    node1_set = find(graph, parents, node1)
    node2_set = find(graph, parents, node2)
    parents[node1_set] = node2_set


def check_loop(graph, parents, edges):
    for edge in edges:
        node_from_set = find(graph, parents, edge[1])
        node_to_set = find(graph, parents, edge[2])
        if node_from_set == node_to_set:
            return True
        union(graph, parents, edge[1], edge[2])
        
    return False
  

def question3(graph_adj_list):
    edge_list = []
    for node_from in graph_adj_list:
        for node_to, value in graph_adj_list[node_from]:
            edge_list.append((value, node_from, node_to))
    sorted_edge_list = sorted(edge_list)
    graph = Graph(nodes = [], edges = [])
    for edge in sorted_edge_list:
        new_nodes = set([node.value for node in graph.nodes] + [edge[1], edge[2]])
        new_edges = graph.get_edge_list() + [edge]
        parents = dict.fromkeys(new_nodes)
        if (not check_loop(graph, parents, new_edges)):
            graph.insert_edge(edge[0], edge[1], edge[2])
    return graph.get_adjacency_list()
