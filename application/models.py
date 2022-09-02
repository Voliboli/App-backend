#!/usr/bin/env python

from . import db

class PlayerModel(db.Model):
    id_player = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    votes = db.Column(db.String(1000), nullable=True)
    total_points = db.Column(db.String(1000), nullable=True)
    break_points = db.Column(db.String(1000), nullable=True)
    winloss = db.Column(db.String(1000), nullable=True)
    total_serve = db.Column(db.String(1000), nullable=True)
    error_serve = db.Column(db.String(1000), nullable=True)
    points_serve = db.Column(db.String(1000), nullable=True)
    total_reception = db.Column(db.String(1000), nullable=True)
    error_reception = db.Column(db.String(1000), nullable=True)
    pos_reception = db.Column(db.String(1000), nullable=True)
    exc_reception = db.Column(db.String(1000), nullable=True)
    total_attacks = db.Column(db.String(1000), nullable=True)
    error_attacks = db.Column(db.String(1000), nullable=True)
    blocked_attacks = db.Column(db.String(1000), nullable=True)
    points_attack = db.Column(db.String(1000), nullable=True)
    pos_attack = db.Column(db.String(1000), nullable=True)
    points_block = db.Column(db.String(1000), nullable=True)
    errors = db.Column(db.String(1000), nullable=True)
    points_avg = db.Column(db.Float, nullable=True)
    attack_avg = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return '<Player #%s>' % self.id_player

    def get_id(self):
        '''DO NOT REMOVE: Required override by Flask internals'''
        return (self.id_player)

    def to_json(self):
        return {
            'id_player': self.id_player,
            'name': self.name,
            'votes': self.votes,
            'total_points': self.total_points,
            'break_points': self.break_points,
            'winloss': self.winloss,
            'total_serve': self.total_serve,
            'error_serve': self.error_serve,
            'points_serve': self.points_serve,
            'total_reception': self.total_reception,
            'error_reception': self.error_reception,
            'pos_reception': self.pos_reception,
            'exc_reception': self.exc_reception,
            'total_attacks': self.total_attacks,
            'error_attacks': self.error_attacks,
            'blocked_attacks': self.blocked_attacks,
            'points_attack': self.points_attack,
            'pos_attack': self.pos_attack,
            'points_block': self.points_block,
            'errors': self.errors,
            'points_avg': self.points_avg,
            'attack_avg': self.attack_avg
        }
