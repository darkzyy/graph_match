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
        vertex_set |= set([v0])
        vertex_set |= set([v1])
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
    # print 'processing', v.get_val()

    if v.get_pos() == 'left':
        for adj in v.get_adj():
            if set([v.get_val(), adj]) not in cur_match \
               and graph.get_vertex(adj).get_color() != 'red':
                if not in_match(cur_match, adj):
                    return [adj, v.get_val()]
                ret_list = dfs(graph, graph.get_vertex(adj), cur_match)
                if ret_list:
                    ret_list.append(v.get_val())
                    return ret_list
        return []
    else: # right
        for adj in v.get_adj():
            # print 'adj of', v.get_val(), ':', adj
            if set([v.get_val(), adj]) in cur_match \
               and graph.get_vertex(adj).get_color() != 'red':
                ret_list = dfs(graph, graph.get_vertex(adj), cur_match)
                if ret_list:
                    ret_list.append(v.get_val())
                    return ret_list
        return []



def find_match(graph):
    left_set = set()
    right_set = set()
    for vertex in graph.get_vertex_list():
        if vertex.get_pos() == '':
            vertex.set_pos('left')
            bipart(graph, vertex)


    for v in graph.get_vertex_list():
        if v.get_pos() == 'left':
            left_set.add(v)

    match = []
    saturated_set = set()

    while True:
        left_vertex_amt = 0
        none_amt = 0
        for v in left_set:
            if v.get_val() in saturated_set:
                continue
            # print 'start from', v.get_val()
            left_vertex_amt += 1
            graph.clean()
            path_list = dfs(graph, v, match)
            if path_list:
                # print path_list
                # print match
                for i in range(0, len(path_list)-1):
                    graph.get_vertex(path_list[i]).set_color('finish')
                    if i%2 == 0:
                        match.append(set([path_list[i], path_list[i+1]]))
                        saturated_set.add(path_list[i])
                        saturated_set.add(path_list[i + 1])
                    else:
                        match.remove(set([path_list[i], path_list[i+1]]))
                graph.get_vertex(path_list[len(path_list)-1]).set_color('finish')
            else:
                none_amt += 1
        if left_vertex_amt == 0:
            break
        if none_amt == left_vertex_amt:
            break

    # print '-'*50
    print len(match)
    # print match
    match_list = []
    for st in match:
        match_list.append((sorted(list(map(int, st)))))

    for item in sorted(match_list):
        print str(item[0])+','+str(item[1])



def test():
    g = graph_input()
    find_match(g)
    # viz.viz(g, 'test.gv')
    

if __name__ == '__main__':
    test()
