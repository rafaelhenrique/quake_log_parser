
def report(parsed_game_matches):

    message = ""
    for game_match, values in parsed_game_matches.items():
        # import ipdb; ipdb.set_trace()
        players = ", ".join(values['players'])
        total_kills = values['total_kills']
        kills = values['kills']

        message += "\n\n{}{}{}\n\n".format("-~"*20, game_match, "-~"*20)
        message += "Total kills on this game: \n- {}\n\n".format(total_kills)
        message += "Players on this game: \n- {}\n\n".format(players)
        message += "Kills on this game:\n"

        kills_by_player = 0
        for player_name, kills in kills.items():
            message += "- {}: {}\n".format(player_name, kills)
            kills_by_player += kills

        world_kills = total_kills - kills_by_player

        message += "\nWorld kills on this game: \n- {}".format(world_kills)
    return message
