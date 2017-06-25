"""

This file contains all the various heuristics for the Isolation game.

"""


def baseline_score(game, player):
    """ returns the simple heuristic score as difference of moves"""

    other_player = game.get_opponent(player)
    our_moves = len(game.get_legal_moves(player))
    their_moves = len(game.get_legal_moves(other_player))

    return game.utility(player) + float(our_moves - their_moves)


def improved_baseline_score(game, player):
    """ returns alternative baseline score, weighting their moves """

    other_player = game.get_opponent(player)
    our_moves = len(game.get_legal_moves(player))
    their_moves = len(game.get_legal_moves(other_player))

    return game.utility(player) + our_moves - (2.0 * their_moves)


def ratio_score(game, player):
    """ returns score as a ratio of valid moves to blank spaces """

    blank_count = len(game.get_blank_spaces())
    result = baseline_score(game, player)

    if blank_count > 0:
        result = (result / blank_count)

    return result


def ratio_count_score(game, player):
    """ returns ratio score from available moves by difference"""

    other_player = game.get_opponent(player)
    our_moves = len(game.get_legal_moves(player))
    their_moves = len(game.get_legal_moves(other_player))

    diff = float(our_moves - their_moves)

    if diff != 0:
        return game.utility(player) + (game.move_count / diff)
    else:
        return game.utility(player)


def ratio_blank_score(game, player):
    """ available legal moves compared to blank spaces """

    blank_count = len(game.get_blank_spaces())
    result = game.utility(player)

    if blank_count > 0:
        result = result + (len(game.get_legal_moves(player)) / blank_count)

    return result
