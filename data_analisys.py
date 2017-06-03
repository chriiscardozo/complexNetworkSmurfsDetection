import numpy as np
import json

DATA_PATH='files/steam_users_json.txt'
CS_ID='730'

def main():
    f = open(DATA_PATH, 'r')
    friend_count = []
    game_count = []
    CSGO_friend_count = []
    CSGO_game_count = []

    for line in f:
        u = json.loads(line)
        friend_count.append(u['friend_count'])
        game_count.append(u['game_count'])

        if(CS_ID in u['games']):
            CSGO_friend_count.append(u['friend_count'])
            CSGO_game_count.append(u['game_count'])

    print('*** General Stats ***')
    print(str(len(friend_count)) + ' users')

    print('Friends count avg: ' + str(np.mean(friend_count)))
    print('Friends count std dev: ' + str(np.std(friend_count)))
    print('Max friends count: ' + str(max(friend_count)))
    print('Min friends count: ' + str(min(friend_count)))

    print('Games count avg: ' + str(np.mean(game_count)))
    print('Games count std dev: ' + str(np.std(game_count)))
    print('Max game count: ' + str(max(game_count)))
    print('Min game count: ' + str(min(game_count)))

    print('*** CG:GO Stats ***')
    print(str(len(CSGO_friend_count)) + ' users')

    print('CS:GO Friends count avg: ' + str(np.mean(CSGO_friend_count)))
    print('CS:GO Friends count std dev: ' + str(np.std(CSGO_friend_count)))
    print('CS:GO Max friends count: ' + str(max(CSGO_friend_count)))
    print('CS:GO Min friends count: ' + str(min(CSGO_friend_count)))

    print('CS:GO Games count avg: ' + str(np.mean(CSGO_game_count)))
    print('CS:GO Games count std dev: ' + str(np.std(CSGO_game_count)))
    print('CS:GO Max game count: ' + str(max(CSGO_game_count)))
    print('CS:GO Min game count: ' + str(min(CSGO_game_count)))

if __name__ == '__main__':
    main()
