'''definition of graph'''

class vertex:
    color = 'none'
    adj_list = []
    pos = ''

    def __init__(self, val):
        self.val = val

    def add_adj(self, v):
        self.adj_list.append(v)

    def get_adj(self):
        return self.adj_list

    def rm_adj(self, v):
        self.adj_list.remove(v)

    def set_color(self, c):
        self.color = c

    def get_color(self):
        return self.color

    def set_pos(self, p):
        self.pos = p

    def get_pos(self):
        return self.pos

class graph:
    vertex_list = []
    edge_list = []

    def add_vertex(self, v):
        self.vertex_list.append(vertex(v))

    def add_edge(self, e):
        self.edge_list.append(e)
        (v0, v1) = e
        v0.add_adj(v1)
        v1.add_adj(v0)

    def rm_vertex(self, v):
        for v0 in v.adj_list:
            v0.rm_adj(v)
            if (v, v0) in edge_list:
                self.edge_list.remove((v, v0))
            if (v0, v) in edge_list:
                self.edge_list.remove((v0, v))
        vertex_list.remove(v)

    def rm_edge(self, e):
        if e in self.edge_list:
            (v0, v1) = e
            v0.rm_adj(v1)
            v1.rm_adj(v0)

    def get_vertex_list(self):
        return self.vertex_list


