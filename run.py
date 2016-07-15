from parsers import task1
from parsers.utils import jsonify

if __name__ == "__main__":
    game_matches = task1.parse_game_kills("games.log")
    games_json = jsonify(game_matches)
    print(games_json)
