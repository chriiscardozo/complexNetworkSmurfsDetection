import json
from graph_tool.all import *
from graph_tool import topology as gt
import sys

DATA_PATH='files/steam_users_json.txt'
CS_ID='730'
PE_ID='238960'

def convert_all():
	convert(filename='steam_all.gml')

def convert_csgo():
	convert(game_id=CS_ID,filename='steam_csgo.gml')

def convert_path_exile():
	convert(game_id=PE_ID,filename='steam_poe.xml.gz')

def convert_limited(n):
	convert(filename='limited.gml',limit=n)

def convert(game_id=None,filename='steam.gml',limit=None):
	print("Converting Steam network...")
	g = Graph(directed=False)


	users = {}
	mapping = {}

	print("Creating nodes...")
	with open(DATA_PATH, 'r') as f:
		i = 0
		
		v_prop = g.new_vertex_property("string")

		for line in f:
			obj = json.loads(line)
			if(game_id is not None and game_id not in obj['games']):
				continue
			user = {}
			user['steamid'] = obj['steamid']
			user['friends'] = obj['friends']

			v = g.add_vertex()
			v_prop[v] = user['steamid']
			users[user['steamid']] = user
			mapping[user['steamid']] = v

			i += 1
			if( i % 1000 == 0): print(str(i) + '\r', end='')
			if( limit is not None and i == limit): break

		g.vertex_properties["label"] = v_prop

	print("Creating edges...")
	i = 0
	for user in users:
		u = mapping[user]
		for fr in users[user]['friends']:
			if fr not in mapping: continue
			v = mapping[fr]
			g.add_edge(u, v)
		i += 1
		if( i % 1000 == 0): print(str(i) + '\r', end='')

	print("Saving at file: " + filename)
	g.save('files/'+filename)



def main():
	if('all' in sys.argv):
		convert_all()
	if('cs' in sys.argv):
		convert_csgo()
	if('lim' in sys.argv):
		convert_limited(1000)
	if('poe' in sys.argv):
		convert_path_exile()

if __name__ == '__main__':
	main()