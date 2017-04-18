import graph_tool.all as gt
import matplotlib
FILE='10000vertices.xml.gz'

print('loading '+ FILE + ' graph')
g = gt.load_graph(FILE)

print(len(list(g.vertices())))
print(len(list(g.edges())))

gt.graph_draw(g, output_size=(5000, 5000), vertex_size=1,
           vcmap=matplotlib.cm.gist_heat_r, output="view.png")