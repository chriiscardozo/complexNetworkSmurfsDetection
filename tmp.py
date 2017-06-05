from graph_tool.all import *
from graph_tool import topology as gt

def get_largest_cc(g):
	l = gt.label_largest_component(g)
	to_remove = []
	for index, v in enumerate(l):
		if(v == 0): to_remove.append(index)
	to_remove.reverse()
	for i in to_remove:
		g.remove_vertex(g.vertex(i))
	return g


def get_trusted_nodes(trust_file,g=None,index=False):
	print('Loading trusted nodes')
	trust = []
	with open(trust_file, 'r') as f:
		for line in f:
			trust.append(line.split()[0])

	if(index and g is not None):
		new_trust = []
		for i in trust:
			new_trust.append(g.vp.label[g.vertex(i)])
		trust = new_trust

	return trust

graph_file='files/poegraph.gml'
trust_file='files/poe_confiaveis.txt'
result_file='files/poe_rank.txt'

g = load_graph(graph_file)
length = len(list(g.vertices()))
print(length, 'vertices')

g = get_largest_cc(g)
print('C.C. vertices ', g.num_vertices())
trusted = get_trusted_nodes(trust_file,g=g,index=True)

with open(trust_file, 'w') as f:
	output = ''
	for t in trusted:
		output += t + '\n'
	output = output[:len(output)-1]
	f.write(output)