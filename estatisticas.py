from graph_tool.all import *
import graph_tool
from graph_tool import topology as gt
import numpy as np
from matplotlib import pyplot as plt
from statsmodels.distributions.empirical_distribution import ECDF
from scipy.stats.kde import gaussian_kde

def get_largest_cc(g):
	l = gt.label_largest_component(g)
	to_remove = []
	for index, v in enumerate(l):
		if(v == 0): to_remove.append(index)
	to_remove.reverse()
	for i in to_remove:
		g.remove_vertex(g.vertex(i))
	return g

def plot_ccdf(sample):
	ecdf = ECDF(sample)
	x = np.linspace(min(sample), max(sample))
	y = ecdf(x)

	new_y = []
	for i in y:
		new_y.append(1-i)
	y = new_y

	plt.plot(x, y, 'bx')
	plt.gca().set_xscale('log')
	plt.gca().set_yscale('log')
	plt.gca().set_aspect('equal')
	axes = plt.gca()
	axes.set_xlim([min(x),max(x)])
	axes.set_ylim([min(y),max(y)])

	plt.show()

def plot_pdf(data):
	kde = gaussian_kde( data )
	dist_space = np.linspace( min(data), max(data), 100 )
	plt.gca().set_xscale('log')
	plt.gca().set_yscale('log')
	plt.plot( dist_space, kde(dist_space), 'bo' )
	plt.show()

def get_density(g):
	if g.is_directed():
		return g.num_edges()/(g.num_vertices()*(g.num_vertices()-1.0))
	else:
		return (2*g.num_edges())/(g.num_vertices()*(g.num_vertices()-1.0))

def rank(rankfile):
	with open(rankfile, 'r') as f:
		ranks = []
		for line in f:
			v = float(line.split(',')[2])
			ranks.append(v)
		ranks = sorted(ranks)
		plot_ccdf(ranks)
		# plot_pdf(ranks)

def stats(g, name,rankfile=None):
	print('***** ' + name + ' *****')
	print('Directed: ', g.is_directed())
	print('v count entire graph: ', g.num_vertices())
	comp,hist = graph_tool.topology.label_components(g)
	print('Num  C.C.: ', len(hist))
	print('Largest C.C.: ', max(hist))
	g = get_largest_cc(g)
	print('>>>>> Only largest C.C.')

	print('v count: ', g.num_vertices())
	print('e count: ', g.num_edges())
	print('pseudo-diameter: ', gt.pseudo_diameter(g)[0])
	print('density: ', get_density(g))
	print('global clust: ', graph_tool.clustering.global_clustering(g)[0])
	deg = [x.out_degree() for x in g.vertices()]
	deg = sorted(deg)

	print('mean deg+: ', np.mean(deg))
	print('std deg+: ', np.std(deg))
	print('min deg+: ', deg[0])
	print('max deg+: ', deg[-1])
	plot_ccdf(deg)
	if rankfile is not None:
		rank(rankfile)



steam = load_graph('files/steam_all.gml')
stats(steam,'STEAM')
csogo = load_graph('files/csgograph.gml')
stats(csogo,'CSGO', 'files/csgo_rank.txt')
poe = load_graph('files/poegraph.gml')
stats(poe,'POE', 'files/poe_rank.txt')