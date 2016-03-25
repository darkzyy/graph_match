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
    

def bipart(graph, v):
    if v.get_pos() == 'left':
        pos = 'right'
    else:
        pos = 'left'
    for val in v.get_adj():
        if graph.get_vertex(val).get_pos() == '':
            graph.get_vertex(val).set_pos(pos)
            bipart(graph, graph.get_vertex(val))


def in_match(m, vertex):
    for e in m:
        if vertex in e:
            return True
    return False


def dfs(graph, v, cur_match):
    v.set_color('red')

    if v.get_pos() == 'left':
        for adj in v.get_adj():
            if set([v, adj]) not in cur_match and graph.get_vertex(adj).get_color() != 'red':
                if not in_match(cur_match, adj):
                    return [adj, v.get_val()]
                ret_list = dfs(graph, graph.get_vertex(adj), cur_match)
                if ret_list:
                    return ret_list.append(v.get_val())
                else:
                    return []
    else: # right
        for adj in v.get_adj():
            if set([v, adj]) in cur_match and graph.get_vertex(adj).get_color() != 'red':
                ret_list = dfs(graph, graph.get_vertex(adj), cur_match)
                if ret_list:
                    return ret_list.append(v.get_val())
                else:
                    return []



def find_match(graph):
    left_set = set()
    right_set = set()
    graph.get_vertex_list()[0].set_pos('left')
    bipart(graph, graph.get_vertex_list()[0])

    # print bipartite graph
    for v in graph.get_vertex_list():
        print v.get_val(), v.get_pos()

    for v in graph.get_vertex_list():
        if v.get_pos() == 'left':
            left_set.add(v)

    match = set()
    '''
    for v in left_set:
        graph.clean()
        match = set()
        print dfs(graph, v, match)
        '''
    while True:
      




def test():
    g = graph_input()
    find_match(g)
    # viz.viz(g, 'test.gv')
    
    


if __name__ == '__main__':
    test()
