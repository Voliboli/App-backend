from ..models import PlayerModel
from ariadne import convert_kwargs_to_snake_case

@convert_kwargs_to_snake_case
def getPlayer_resolver(obj, info, name):
    try:
        player = PlayerModel.query.filter_by(name=name).first()
        payload = {
            "success": True,
            "player": player.to_json()
        }
    except AttributeError: 
        payload = {
            "success": False,
            "errors": [f"Player {name} not found"]
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
