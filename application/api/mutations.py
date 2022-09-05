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

def createPlayer_resolver(obj, 
                          info, 
                          name, 
                          votes=None,
                          totalPoints=None,
                          breakPoints=None,
                          winloss=None,
                          totalServe=None,
                          errorServe=None,
                          pointsServe=None,
                          totalReception=None,
                          errorReception=None,
                          posReception=None,
                          excReception=None,
                          totalAttacks=None,
                          errorAttacks=None,
                          blockedAttacks=None,
                          pointsAttack=None,
                          posAttack=None,
                          pointsBlock=None,
                          dateTeam=None):
    try:
        if errorServe is None or errorReception is None or errorAttacks is None:
            errors = 'null'
        else:
            errors = int(errorServe) + int(errorReception) + int(errorAttacks)
        player = PlayerModel(
            name=name, 
            votes=votes,
            totalPoints=totalPoints,
            breakPoints=breakPoints,
            winloss=winloss,
            totalServe=totalServe,
            errorServe=errorServe,
            pointsServe=pointsServe,
            totalReception=totalReception,
            errorReception=errorReception,
            posReception=posReception,
            excReception=excReception,
            totalAttacks=totalAttacks,
            errorAttacks=errorAttacks,
            blockedAttacks=blockedAttacks,
            pointsAttack=pointsAttack,
            posAttack=posAttack,
            pointsBlock=pointsBlock,
            errors=str(errors),
            dateTeam=dateTeam,
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

def updatePlayer_resolver(obj, 
                          info,
                          name, 
                          votes=None,
                          totalPoints=None,
                          breakPoints=None,
                          winloss=None,
                          totalServe=None,
                          errorServe=None,
                          pointsServe=None,
                          totalReception=None,
                          errorReception=None,
                          posReception=None,
                          excReception=None,
                          totalAttacks=None,
                          errorAttacks=None,
                          blockedAttacks=None,
                          pointsAttack=None,
                          posAttack=None,
                          pointsBlock=None,
                          dateTeam=None):
    try:
        player = PlayerModel.query.filter_by(name=name).first()
        if player:
            payload = {
                "success": False,
                "errors": [f'Player {name} does not exist!']
            }
            return payload

        errors = int(errorServe) + int(errorReception) + int(errorAttacks)
        if dateTeam not in player.dateTeam:
            if votes is not None:
                player.votes = add_elem_to_string(player.votes, votes)
            if totalPoints is not None:
                player.totalPoints = add_elem_to_string(player.totalPoints, totalPoints)
                player.pointsAvg = average(player.totalPoints, player.pointsAvg)
            if breakPoints is not None:
                player.breakPoints = add_elem_to_string(player.breakPoints, breakPoints)
            if winloss is not None:
                player.winloss = add_elem_to_string(player.winloss, winloss)
            if totalServe is not None:
                player.totalServe = add_elem_to_string(player.totalServe, totalServe)
            if errorServe is not None:
                player.errorServe = add_elem_to_string(player.errorServe, errorServe)
            if pointsServe is not None:
                player.pointsServe = add_elem_to_string(player.pointsServe, pointsServe)
            if totalReception is not None:
                player.totalReception = add_elem_to_string(player.totalReception, totalReception)
            if error_reception is not None:
                player.error_reception = add_elem_to_string(player.error_reception, error_reception)
            if posReception is not None:
                player.posReception = add_elem_to_string(player.posReception, posReception)
            if excReception is not None:
                player.excReception = add_elem_to_string(player.excReception, excReception)
            if totalAttacks is not None:
                player.totalAttacks = add_elem_to_string(player.totalAttacks, totalAttacks)
            if errorAttacks is not None:
                player.errorAttacks = add_elem_to_string(player.errorAttacks, errorAttacks)
            if blockedAttacks is not None:
                player.blockedAttacks = add_elem_to_string(player.blockedAttacks, blockedAttacks)
            if pointsAttack is not None:
                player.pointsAttack = add_elem_to_string(player.pointsAttack, pointsAttack)
            if posAttack is not None:
                player.posAttack = add_elem_to_string(player.posAttack, posAttack)
                player.attackAvg = average(player.posAttack, player.attackAvg)
            if pointsBlock is not None:
                player.pointsBlock = add_elem_to_string(player.pointsBlock, pointsBlock)
            if str(errors) is not None:
                player.errors = add_elem_to_string(player.errors, str(errors))
            if dateTeam is not None:
                player.dateTeam = add_elem_to_string(player.dateTeam, dateTeam)
            db.session.add(player)
            db.session.commit()
            payload = {
                "success": True,
                "post": player.to_json()
            }
        else:
            payload = {
                "success": False,
                "errors": [f"Stats for player {name} already saved this game"]
            }
    except AttributeError as e:  # todo not found
        payload = {
            "success": False,
            "errors": [e]
        }
    return payload

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
