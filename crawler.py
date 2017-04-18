import requests
import os

friends = {}
dict_users = {}
not_explored = []

DIR='network'
KEY='CE838F7FFA092D3BD03A83099A608110'
CAIO_ID = '76561198045605382'
URL = 'http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?relationship=friend&key='+KEY+'&steamid='
MAX_EXPLORED=10000

def main():
	explored_count = 0
	dict_users[CAIO_ID] = False
	not_explored.append(CAIO_ID)

	while len(not_explored) > 0:
		id_user = not_explored.pop(0)
		dict_users[id_user] = True
		explored_count += 1
		friends[id_user] = []

		# if-else to continue from stopping point
		if(id_user not in os.listdir(DIR)):
			r = requests.get(URL+id_user)
			json = r.json()

			if bool(json.get('friendslist')):
				for item in json.get('friendslist').get('friends'):
					friends[id_user].append(item.get('steamid'))
					if item.get('steamid') not in dict_users:
						dict_users[item.get('steamid')] = False
						not_explored.append(item.get('steamid'))

			f = open(os.path.join(DIR, id_user), 'w')
			f.write(str(','.join(friends[id_user])))
		else:
			f = open(os.path.join(DIR, id_user), 'r')
			for item in f.read().split(','):
				if item not in dict_users and len(item) > 0:
					dict_users[item] = False
					not_explored.append(item)

		print (str(explored_count)+' vertices\r',end='')
		if explored_count == MAX_EXPLORED:
			break

main()