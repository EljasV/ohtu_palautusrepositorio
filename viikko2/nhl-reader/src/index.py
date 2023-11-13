import requests

from player import Player


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    print("Players from FIN")

    result = list(filter(lambda p: p.nationality == 'FIN', players))
    result.sort(key=lambda p: p.goals + p.assists, reverse=True)
    for player in result:
        print(player)


if __name__ == '__main__':
    main()
