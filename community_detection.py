from igraph import *
from graph_tool import topology as gt
from graph_tool.all import *

filepath="files/poegraph.gml"

print("*** Community detection ***")
print("Loading graph...")
g = load_graph(filepath)
l = gt.label_largest_component(g)
u = gt.GraphView(g, vfilt=l)
print(u.num_vertices(), " in largest C.C.")
print("Saving temp file...")
u.save("files/tmp.xml.gz")
g = load_graph('files/tmp.xml.gz')
g.save('files/tmp.gml')

print("Computing communities...")
g = load("files/tmp.graphml",format='graphml	')
p = g.community_multilevel()
q = g.modularity(p)
print(p)
print(q)

f = open('files/communities.txt', 'w')
f.write(str(p))