'''definition of graph'''

class vertex:
    def __init__(self, val):
        self.val = val
        self.adj_list = []
        self.pos = ''
        self.color = 'none'

    def get_val(self):
        return self.val

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
    
    def print_adj(self):
        print self.val,'adjs : '
        for v in self.adj_list:
            print v,
        print ''

class graph:
    vertex_list = []
    edge_list = []

    def add_vertex(self, v):
        self.vertex_list.append(vertex(v))

    def add_edge(self, e):
        (v0, v1) = e
        s = set([v0, v1])
        if s in self.edge_list: 
            print 'already in edge list'
            return
        self.edge_list.append(s)
        for vit in self.vertex_list:
            if vit.val == v0:
                vit.add_adj(v1)
                vit.print_adj()
            if vit.val == v1:
                vit.add_adj(v0)
                vit.print_adj()
        # print '------'

    def rm_vertex(self, v):
        for v0 in v.adj_list:
            v0.rm_adj(v)
            if set([v, v0]) in edge_list:
                self.edge_list.remove(set([v, v0]))
        vertex_list.remove(v)

    def rm_edge(self, e):
        (v0, v1) = e
        s = set([v0, v1])
        if s in self.edge_list: 
            self.edge_list.remove(s)
            for vit in self.vertex_list:
                if vit.val == v0:
                    vit.rm_adj(v1)
                if vit.val == v1:
                    vit.rm_adj(v0)

    def get_vertex_list(self):
        return self.vertex_list


