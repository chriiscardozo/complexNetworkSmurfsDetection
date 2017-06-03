import numpy as np
import graph_tool.all as gt
import matplotlib
FILE='10000vertices.xml.gz'

print('loading '+ FILE + ' graph')
g = gt.load_graph(FILE)

N = len(list(g.vertices()))
M = len(list(g.edges()))

arr = []

for v in g.vertices():
	arr.append(v.out_degree())

max_degree = max(arr)
min_degree = min(arr)
avg_degree = np.mean(arr)
std_degree = np.std(arr)

print(str(N) + ' vertices')
print(str(M) + ' edges')
print('Max degree: ' + str(max_degree))
print('Min degree: ' + str(min_degree))
print('Avg degree: ' + str(avg_degree) + ' / S.D.: ' + str(std_degree))
print('Density: ' + str((2.0*M)/(N*(N-1.0))))
print('Pseudo-diameter: ' + str(gt.pseudo_diameter(g)[0]))
print('Global clustering: ' + str(gt.global_clustering(g)))

# gt.graph_draw(g, output_size=(5000, 5000), vertex_size=1,
#            vcmap=matplotlib.cm.gist_heat_r, output="view.png")