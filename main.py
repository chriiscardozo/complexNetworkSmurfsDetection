from graph_tool.all import *
from sybil_rank import sybilrank
import numpy as np
import random
import operator
from graph_tool import topology as gt

def graph_to_dict(g):
	print("Converting network to dict...")
	network = {}

	for n in g.vertices():
		label = g.vp.label[n]
		network[label] = {}

	for e in g.edges():
		w = g.ep.weight[e]
		u, v = e
		label1 = g.vp.label[u]
		label2 = g.vp.label[v]
		network[label1][label2] = w

	return network

def get_largest_cc(g):
	l = gt.label_largest_component(g)
	to_remove = []
	for index, v in enumerate(l):
		if(v == 0): to_remove.append(index)
	to_remove.reverse()
	for i in to_remove:
		g.remove_vertex(g.vertex(i))
	return g

def get_trusted_nodes(trust_file):
	print('Loading trusted nodes')
	trust = []
	with open(trust_file, 'r') as f:
		for line in f:
			trust.append(line.split()[0])
	return trust

def save_rank_outuput(rank,result_file):
	with open(result_file, 'w') as f:
		for index, item in enumerate(rank):
			line = [str(index+1), str(item[0]), str(item[1])]
			f.write(','.join(line) + '\n')

def run(graph_file,trust_file,result_file):
	print('Loading graph...')
	g = load_graph(graph_file)
	length = len(list(g.vertices()))
	print(length, 'vertices')

	g = get_largest_cc(g)
	print('C.C. vertices ', g.num_vertices())
	
	trusted = get_trusted_nodes(trust_file)
	network = graph_to_dict(g)
	result = sybilrank(network,int(round(np.log10(length))),trusted,100/len(trusted))

	sorted_result = sorted(result.items(), key=operator.itemgetter(1))
	sorted_result.reverse()
	save_rank_outuput(sorted_result,result_file)

def main():
	graph_file='files/poegraph.gml'
	trust_file='files/poe_confiaveis.txt'
	result_file='files/poe_rank.txt'
	run(graph_file,trust_file,result_file)

	# graph_file='files/csgograph.gml'
	# trust_file='files/csgo_confiaveis.txt'
	# result_file='files/csgo_rank.txt'
	# run(graph_file,trust_file,result_file)

if __name__ == '__main__':
	main()