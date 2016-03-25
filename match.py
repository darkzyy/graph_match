import graph


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
    print vertex_set
    print edge_list
        

def test():
    graph_input()


if __name__ == '__main__':
    test()
