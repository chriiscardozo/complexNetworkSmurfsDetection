import graph_tool.all as gt
import os

DIR='network'

vertices_map = {}

def main():
	g = gt.Graph(directed=False)
	prop_label = g.new_vertex_property("string")
	g.vertex_properties["label"] = prop_label

	print('Adding vertices...')
	index = 0
	for label in os.listdir(DIR):
		v = g.add_vertex()
		prop_label[v] = label
		vertices_map[label] = index
		index += 1

	print('Adding edges...')
	for label1 in os.listdir(DIR):
		f = open(os.path.join(DIR, label1))

		for label2 in f.read().split(','):
			if(label2 in vertices_map and (not bool(g.edge(vertices_map[label1], vertices_map[label2])))):
				g.add_edge(vertices_map[label1], vertices_map[label2])

	print(len(list(g.vertices())))
	print(len(list(g.edges())))
	g.save(str(len(list(g.vertices()))) + "vertices.xml.gz")

	

main()