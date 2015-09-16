from pyramid.view import view_config
import player;
import strategies;


@view_config(route_name='home', renderer='templates/board.pt')
def my_view(request):
    session = request.session
    player_dao = player.Player()
    strategy = strategies.RubricStrategy('127.0.0.1', 'root', '')
    strategy.registerPlayer(player_dao)
    session['game'] = player_dao
    session['strategy'] = strategy
    return {'grid': player_dao._grid}
    #return {'grid': [[2, 0, 2, 0], [0, 0, 0, 0], [2, 0, 0, 4], [0, 0, 0, 0]]}

@view_config(route_name='get_move', renderer='templates/values.pt')
def get_move(request):
    session = request.session
    player_dao = session['game']
    strategy = session['strategy']
    move = strategy.getMove(player_dao._grid)
    move.execute()
    return {
        'move': move.name,
        'grid': player_dao._grid
    }
    #return {
    #    'move': 'right',
    #    'grid': [[0, 0, 0, 4], [0, 0, 0, 0], [0, 0, 2, 4], [0, 0, 0, 0]]
    #}
