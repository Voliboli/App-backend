import requests
import unittest
from sgqlc.types import String, Type, Field, ID, Boolean, list_of
from sgqlc.operation import Operation

class Player(Type):
    name = String
    votes = String

class PlayerResult(Type):
  success = Boolean
  errors =  list_of(String)
  player = Player

class PlayersResult(Type):
    success = Boolean
    errors = list_of(String)
    players = list_of(Player)

class Query(Type):
    getPlayer = Field(PlayerResult, args={'name': String})
    getPlayers = Field(PlayersResult)

class Mutation(Type):
    createPlayer = Field(PlayerResult, args={'name': String, 'votes': String})
    updatePlayer = Field(PlayerResult, args={'name': String, 'votes': String})
    deletePlayer = Field(PlayerResult, args={'name': String})

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.BASE = "http://172.34.1.3:5000"
        self.query = Operation(Query)
        self.mutation = Operation(Mutation)

    def test_1_get_players(self):
        self.query.getPlayers()
        print(self.query)
        resp = requests.post(self.BASE + "/players", json={'query': str(self.query)})
        self.assertEqual(resp.status_code, 200)

    def test_2_get_player(self):
        self.query.getPlayer(name='Teo')
        print(self.query)
        resp = requests.post(self.BASE + "/players", json={'query': str(self.query)})
        self.assertEqual(resp.status_code, 200)

    def test_3_create_player(self):
        self.mutation.createPlayer(name='Gaspa', votes='null')
        print(self.mutation)
        resp = requests.post(self.BASE + "/players", json={'query': str(self.mutation)})
        self.assertEqual(resp.status_code, 200)

    def test_4_update_player(self):
        self.mutation.updatePlayer(name='Gaspa', votes='not null')
        print(self.mutation)
        resp = requests.post(self.BASE + "/players", json={'query': str(self.mutation)})
        self.assertEqual(resp.status_code, 200)

    def test_5_delete_player(self):
        self.mutation.deletePlayer(name='Gaspa')
        print(self.mutation)
        resp = requests.post(self.BASE + "/players", json={'query': str(self.mutation)})
        self.assertEqual(resp.status_code, 200)

if __name__ == '__main__':
    unittest.main()
