import graphviz
import graph

def viz(graph, filename):
    gv = graphviz.Graph()
    for v in graph.vertex_list:
        gv.node(v.val, v.val)
    for e in graph.edge_list:
        (v0, v1) = e
        gv.edge(v0, v1)
    gv.render(filename, './', view=True)

def main():
    gra = graph.graph()
    gra.add_vertex('A')
    gra.add_vertex('B')
    gra.add_vertex('C')
    gra.add_vertex('D')
    gra.add_edge(('A', 'B'))
    gra.add_edge(('D', 'B'))
    gra.add_edge(('A', 'C'))
    gra.add_edge(('A', 'D'))
    gra.add_edge(('A', 'C'))
    for v in gra.vertex_list:
        v.print_adj()
    gra.rm_edge(('A', 'C'))
    for v in gra.vertex_list:
        v.print_adj()
    viz(gra, 'test.gv')

if __name__ == '__main__':
    main()

