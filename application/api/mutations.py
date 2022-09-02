from ariadne import convert_kwargs_to_snake_case
import psycopg2 
from .. import db
from ..models import PlayerModel

def add_elem_to_string(string, elem):
    if string is None:
        return elem
    return string + ',' + elem

def average(x, y):
    if x is None:
        return y
    elif y is None:
        return x
    array = x.split(',')
    array = [eval(i) for i in array]
    array.append(y)
    return sum(array) / len(array)

@convert_kwargs_to_snake_case
def createPlayer_resolver(obj, 
                          info, 
                          name, 
                          votes=None,
                          total_points=None,
                          break_points=None,
                          winloss=None,
                          total_serve=None,
                          error_serve=None,
                          points_serve=None,
                          total_reception=None,
                          error_reception=None,
                          pos_reception=None,
                          exc_reception=None,
                          total_attacks=None,
                          error_attacks=None,
                          blocked_attacks=None,
                          points_attack=None,
                          pos_attack=None,
                          points_block=None,
                          errors=None):
    try:
        player = PlayerModel(
            name=name, 
            votes=votes,
            total_points=total_points,
            break_points=break_points,
            winloss=winloss,
            total_serve=total_serve,
            error_serve=error_serve,
            points_serve=points_serve,
            total_reception=total_reception,
            error_reception=error_reception,
            pos_reception=pos_reception,
            exc_reception=exc_reception,
            total_attacks=total_attacks,
            error_attacks=error_attacks,
            blocked_attacks=blocked_attacks,
            points_attack=points_attack,
            pos_attack=pos_attack,
            points_block=points_block,
            errors=errors,
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
def updatePlayer_resolver(obj, 
                          info,
                          name, 
                          votes=None,
                          total_points=None,
                          break_points=None,
                          winloss=None,
                          total_serve=None,
                          error_serve=None,
                          points_serve=None,
                          total_reception=None,
                          error_reception=None,
                          pos_reception=None,
                          exc_reception=None,
                          total_attacks=None,
                          error_attacks=None,
                          blocked_attacks=None,
                          points_attack=None,
                          pos_attack=None,
                          points_block=None,
                          errors=None):
    try:
        player = PlayerModel.query.filter_by(name=name).first()
        if player:
            if votes is not None:
                player.votes = add_elem_to_string(player.votes, votes)
            if total_points is not None:
                player.total_points = add_elem_to_string(player.total_points, total_points)
                player.points_avg = average(player.total_points, player.points_avg)
            if break_points is not None:
                player.break_points = add_elem_to_string(player.break_points, break_points)
            if winloss is not None:
                player.winloss = add_elem_to_string(player.winloss, winloss)
            if total_serve is not None:
                player.total_serve = add_elem_to_string(player.total_serve, total_serve)
            if error_serve is not None:
                player.error_serve = add_elem_to_string(player.error_serve, error_serve)
            if points_serve is not None:
                player.points_serve = add_elem_to_string(player.points_serve, points_serve)
            if total_reception is not None:
                player.total_reception = add_elem_to_string(player.total_reception, total_reception)
            if error_reception is not None:
                player.error_reception = add_elem_to_string(player.error_reception, error_reception)
            if pos_reception is not None:
                player.pos_reception = add_elem_to_string(player.pos_reception, pos_reception)
            if exc_reception is not None:
                player.exc_reception = add_elem_to_string(player.exc_reception, exc_reception)
            if total_attacks is not None:
                player.total_attacks = add_elem_to_string(player.total_attacks, total_attacks)
            if error_attacks is not None:
                player.error_attacks = add_elem_to_string(player.error_attacks, error_attacks)
            if blocked_attacks is not None:
                player.blocked_attacks = add_elem_to_string(player.blocked_attacks, blocked_attacks)
            if points_attack is not None:
                player.points_attack = add_elem_to_string(player.points_attack, points_attack)
            if pos_attack is not None:
                player.pos_attack = add_elem_to_string(player.pos_attack, pos_attack)
                player.attack_avg = average(player.pos_attack, player.attack_avg)
            if points_block is not None:
                player.points_block = add_elem_to_string(player.points_block, points_block)
            if errors is not None:
                player.errors = add_elem_to_string(player.errors, errors)
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
