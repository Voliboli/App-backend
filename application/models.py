#!/usr/bin/env python

from . import db

class PlayerModel(db.Model):
    id_player = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    votes = db.Column(db.String(1000), nullable=True)

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
        }
