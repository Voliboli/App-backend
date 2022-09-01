from ariadne import convert_kwargs_to_snake_case
from .. import db
from ..models import PlayerModel
import psycopg2 

@convert_kwargs_to_snake_case
def createPlayer_resolver(obj, info, name, votes=None):
    try:
        player = PlayerModel(
            name=name, 
            votes=votes
        )

        try:
            db.session.add(player)
            db.session.commit()
            payload = {
                "success": True,
                "player": player.to_json()
            }
        except:
            payload = {
                "success": False,
                "errors": ["Player already exists"]
            }

    except ValueError as e:  
        payload = {
            "success": False,
            "errors": [e]
        }

    return payload

@convert_kwargs_to_snake_case
def updatePlayer_resolver(obj, info, name, votes=None):
    try:
        player = PlayerModel.query.filter_by(name=name).first()
        if player:
            if votes is not None:
                player.votes = votes
            db.session.add(player)
            db.session.commit()
            payload = {
                "success": True,
                "post": player.to_json()
            }
        else:
            payload = {
                "success": False,
                "errors": [f"Player with this id {id_player} not found"]
            }
    except AttributeError as e:  # todo not found
        payload = {
            "success": False,
            "errors": [e]
        }
    return payload

@convert_kwargs_to_snake_case
def deletePlayer_resolver(obj, info, name):
    try:
        player = PlayerModel.query.filter_by(name=name).first()
        if player:
            db.session.delete(player)
            db.session.commit()
            payload = {
                "success": True, 
                "player": player.to_json()
            }
            return payload
        else:
            payload = {
                "success": False,
                "errors": [f"Player with this id {id_player} not found"]
            }
    except AttributeError as e:
        payload = {
            "success": False,
            "errors": [e]
        }
    return payload
