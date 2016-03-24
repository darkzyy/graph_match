from graph import *

g = graph()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)

print g.get_vertex_list()
for v in g.get_vertex_list():
    v.set_pos('left')
for v in g.get_vertex_list():
    print v.get_pos()
