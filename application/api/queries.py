from ..models import PlayerModel
from ariadne import convert_kwargs_to_snake_case

@convert_kwargs_to_snake_case
def getPlayer_resolver(obj, info, id):
    try:
        player = PlayerModel.query.get(id)
        payload = {
            "success": True,
            "player": player.to_json()
        }
    except AttributeError: 
        payload = {
            "success": False,
            "errors": ["Player item matching {id} not found"]
        }

    return payload

def getPlayers_resolver(obj, info):
    try:
        players = [player.to_json() for player in PlayerModel.query.all()]
        payload = {
            "success": True,
            "players": players
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }

    return payload
