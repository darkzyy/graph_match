import graph
import viz


def graph_input():
    g = graph.graph()
    useless = raw_input()
    vertex_set = set()
    edge_list = []
    while True:
        text = raw_input()
        (v0,v1) = text.split(',')
        if int(v0) == -1 and int(v1) == -1:
            break
        e = set([v0, v1])
        vertex_set |= set(v0)
        vertex_set |= set(v1)
        if e not in edge_list:
            edge_list.append(e)
    # print vertex_set
    # print edge_list
    for v in vertex_set:
        g.add_vertex(v)
    for e in edge_list:
        g.add_edge(e)
    return g
        

def test():
    g = graph_input()
    viz.viz(g, 'test.gv')
    


if __name__ == '__main__':
    test()
