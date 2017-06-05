from igraph import *
from graph_tool import topology as gt
from graph_tool.all import *
from graph_tool import util as gutil


def generate_communities(filepath,destpath):
	tmppath='files/tmp.graphml'

	print("*** Community detection ***")
	g = load_graph(filepath)

	print('Total vertices: ', g.num_vertices())
	l = gt.label_largest_component(g)
	print('Vertices in giant CC: ', sum(l))
	to_remove = []
	for index, v in enumerate(l):
		if(v == 0): to_remove.append(index)
	to_remove.reverse()
	for i in to_remove:
		g.remove_vertex(g.vertex(i))

	print('Final vertices count: ', g.num_vertices())
	g.save(tmppath)


	print("Computing communities...")
	g = load(tmppath)
	g.to_undirected()
	p = g.community_multilevel()
	q = g.modularity(p)

	output = ""

	for i in p:
		output += ' '.join(g.vs[x]['label'] for x in i)
		output += '\n'
	output = output[:len(output)-1]

	f = open(destpath, 'w')
	f.write(output)

generate_communities('files/poegraph.gml', 'files/poe_communities.txt')
generate_communities('files/csgograph.gml', 'files/csgo_communities.txt')