from igraph import *

print("*** Community detection ***")
print("Loading graph...")
g = load("files/steam.gml")
print("Computing communities...")
p = g.community_multilevel()
q = g.modularity(p)
print(type(p))
# print(q)
plot(g)