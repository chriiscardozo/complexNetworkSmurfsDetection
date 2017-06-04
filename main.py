from graph_tool.all import *
from sybil_rank import sybilrank
import numpy as np
import random
import operator

def graph_to_dict(g):
	print("Converting network to dict...")
	network = {}

	for n in g.vertices():
		label = g.vp.label[n]
		network[label] = []

	for u, v in g.edges():
		label1 = g.vp.label[u]
		label2 = g.vp.label[v]
		network[label1].append(label2)
		network[label2].append(label1)

	return network

def main():
	print('Loading graph...')
	g = load_graph('files/steam_csgo.gml')
	length = len(list(g.vertices()))
	print(length, 'vertices')
	
	network = graph_to_dict(g)

	trusted = list(network.keys())
	random.shuffle(trusted)
	result = sybilrank(network,int(round(np.log10(length))),trusted[:100],10)

	sorted_result = sorted(result.items(), key=operator.itemgetter(1))
	
	print('higher')
	for n in sorted_result[:15]: print(n)
	print('lower')
	for n in sorted_result[len(sorted_result)-15:]: print(n)


if __name__ == '__main__':
	main()