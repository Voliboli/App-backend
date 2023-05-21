from ..models import *


def getPlayer_resolver(obj, info, name):
    try:
        player = Player.query.filter_by(name=name).first()
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
        players = [player.to_json() for player in Player.query.all()]
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

def getTeams_resolver(obj, info):
    try:
        teams = [team.to_json() for team in Team.query.all()]
        payload = {
            "success": True,
            "teams": teams
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }

    return payload


def getTeam_resolver(obj, info, name):
    try:
        team = Team.query.filter_by(name=name).first()
        payload = {
            "success": True,
            "team": team.to_json()
        }
    except AttributeError: 
        payload = {
            "success": False,
            "errors": [f"Team {name} not found"]
        }

    return payload