from graph_tool.all import *
from graph_tool import topology as gt

g=load_graph('files/csgograph.gml')
l = gt.label_largest_component(g)
u = gt.GraphView(g, vfilt=l)


print(g.num_vertices(), '->', u.num_vertices())
print(g.num_edges(), '->', u.num_edges())
