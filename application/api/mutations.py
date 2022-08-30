from ariadne import convert_kwargs_to_snake_case
from .. import db
from ..models import PlayerModel

@convert_kwargs_to_snake_case
def createPlayer_resolver(obj, info, name, votes):
    try:
        player = PlayerModel(
            name=name, 
            votes=votes
        )
        db.session.add(player)
        db.session.commit()

        payload = {
            "success": True,
            "player": player.to_json()
        }
    except ValueError:  
        payload = {
            "success": False,
            "errors": ["Player info provided was not sufficient. Returning error"]
        }

    return payload

@convert_kwargs_to_snake_case
def updatePlayer_resolver(obj, info, id, name, votes):
    try:
        player = PlayerModel.query.get(id)
        if player:
            player.name = name
            player.votes = votes
        db.session.add(player)
        db.session.commit()
        payload = {
            "success": True,
            "post": player.to_json()
        }
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["item matching id {id} not found"]
        }
    return payload

@convert_kwargs_to_snake_case
def deletePlayer_resolver(obj, info, id):
    try:
        player = PlayerModel.query.get(id)
        db.session.delete(player)
        db.session.commit()
        payload = {
            "success": True, 
            "player": player.to_json()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Not found"]
        }
    return payload
