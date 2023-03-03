#!/usr/bin/env python

from . import db

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    players = db.relationship('Player', backref='team')

    def __repr__(self):
        return '<Team - %s>' % self.name
    
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'players': [player for player in self.players],
        }

class Player(db.Model):
    idPlayer = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    votes = db.Column(db.String(1000), nullable=True)
    totalPoints = db.Column(db.String(1000), nullable=True)
    breakPoints = db.Column(db.String(1000), nullable=True)
    winloss = db.Column(db.String(1000), nullable=True)
    totalServe = db.Column(db.String(1000), nullable=True)
    errorServe = db.Column(db.String(1000), nullable=True)
    pointsServe = db.Column(db.String(1000), nullable=True)
    totalReception = db.Column(db.String(1000), nullable=True)
    errorReception = db.Column(db.String(1000), nullable=True)
    posReception = db.Column(db.String(1000), nullable=True)
    excReception = db.Column(db.String(1000), nullable=True)
    totalAttacks = db.Column(db.String(1000), nullable=True)
    errorAttacks = db.Column(db.String(1000), nullable=True)
    blockedAttacks = db.Column(db.String(1000), nullable=True)
    pointsAttack = db.Column(db.String(1000), nullable=True)
    posAttack = db.Column(db.String(1000), nullable=True)
    pointsBlock = db.Column(db.String(1000), nullable=True)
    errors = db.Column(db.String(1000), nullable=True)
    pointsAvg = db.Column(db.Float, nullable=True)
    attackAvg = db.Column(db.Float, nullable=True)
    dateTeam = db.Column(db.String(1000), nullable=True)
    teamID = db.Column(db.Integer, db.ForeignKey('team.id'))

    def __repr__(self):
        return '<Player - %s>' % self.name

    def get_id(self):
        '''DO NOT REMOVE: Required override by Flask internals'''
        return (self.idPlayer)

    def to_json(self):
        return {
            'idPlayer': self.idPlayer,
            'name': self.name,
            'votes': self.votes,
            'totalPoints': self.totalPoints,
            'breakPoints': self.breakPoints,
            'winloss': self.winloss,
            'totalServe': self.totalServe,
            'errorServe': self.errorServe,
            'pointsServe': self.pointsServe,
            'totalReception': self.totalReception,
            'errorReception': self.errorReception,
            'posReception': self.posReception,
            'excReception': self.excReception,
            'totalAttacks': self.totalAttacks,
            'errorAttacks': self.errorAttacks,
            'blockedAttacks': self.blockedAttacks,
            'pointsAttack': self.pointsAttack,
            'posAttack': self.posAttack,
            'pointsBlock': self.pointsBlock,
            'errors': self.errors,
            'pointsAvg': self.pointsAvg,
            'attackAvg': self.attackAvg,
            'dateTeam': self.dateTeam,
            'teamID': self.teamID
        }