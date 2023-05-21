import random
import string
import requests
import unittest
from sgqlc.types import String, Type, Field, ID, Boolean, list_of
from sgqlc.operation import Operation

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)
    return result_str

class Player(Type):
    name = String
    votes = String
    dateTeam = String

class PlayerResult(Type):
    success = Boolean
    errors =  list_of(String)
    player = Player

class PlayersResult(Type):
    success = Boolean
    errors = list_of(String)
    players = list_of(Player)

class Team(Type):
    name = String
    players = list_of(Player)

class TeamResult(Type):
    success = Boolean
    errors = list_of(String)
    team = Team

class TeamsResult(Type):
    success = Boolean
    errors = list_of(String)
    teams = list_of(Team)

class Query(Type):
    getTeams = Field(TeamsResult)
    getPlayer = Field(PlayerResult, args={'name': String})
    getPlayers = Field(PlayersResult)

class Mutation(Type):
    createTeam = Field(TeamResult, args={'name': String})
    deleteTeam = Field(TeamResult, args={'name': String})
    createPlayer = Field(PlayerResult, args={'name': String, 'teamName': String, 'votes': String})
    updatePlayer = Field(PlayerResult, args={'name': String, 'votes': String, 'dateTeam': String})
    deletePlayer = Field(PlayerResult, args={'name': String})

class TestAPI(unittest.TestCase):
    RNAME = get_random_string(6)
    
    def setUp(self):
        self.BASE = "http://172.34.1.3:5000"
        self.query = Operation(Query)
        self.mutation = Operation(Mutation)
        self.query.__to_graphql__(auto_select_depth=3)
        self.mutation.__to_graphql__(auto_select_depth=3)

    '''
    def test_1_create_team(self):
        self.mutation.createTeam(name='ACH Volley Ljubljana')
        #print(self.mutation)
        resp = requests.post(self.BASE + "/teams", json={'query': str(self.mutation)})
        print(resp.json())
        self.assertEqual(resp.status_code, 200)
    '''
        
    def test_2_create_player(self):
        self.mutation.createPlayer(name=self.RNAME, teamName='ACH Volley Ljubljana', votes='null')
        #print(self.mutation)
        resp = requests.post(self.BASE + "/players", json={'query': str(self.mutation)})
        print(resp.json())
        self.assertEqual(resp.status_code, 200)
     
    '''
    def test_3_get_teams(self):
        self.query.getTeams()
        #print(self.query)
        resp = requests.post(self.BASE + "/teams", json={'query': str(self.query)})
        print(resp.json())
        self.assertEqual(resp.status_code, 200)
    '''
        
    def test_4_get_player(self):
        self.query.getPlayer(name=self.RNAME)
        #print(self.query)
        resp = requests.post(self.BASE + "/players", json={'query': str(self.query)})
        print(resp.json())
        self.assertEqual(resp.status_code, 200)
    
    '''
    def test_5_get_players(self):
        self.query.getPlayers()
        #print(self.query)
        resp = requests.post(self.BASE + "/players", json={'query': str(self.query)})
        print(resp.json())
        self.assertEqual(resp.status_code, 200)
    '''
        
    def test_6_update_player(self):
        self.mutation.updatePlayer(name=self.RNAME, votes='not null', dateTeam='test')
        #print(self.mutation)
        resp = requests.post(self.BASE + "/players", json={'query': str(self.mutation)})
        self.assertEqual(resp.status_code, 200)

    def test_7_get_player(self):
        self.query.getPlayer(name=self.RNAME)
        #print(self.query)
        resp = requests.post(self.BASE + "/players", json={'query': str(self.query)})
        print(resp.json())
        self.assertEqual(resp.status_code, 200)
    
    '''
    def test_8_get_players(self):
        self.query.getPlayers()
        #print(self.query)print(self.query)
        resp = requests.post(self.BASE + "/players", json={'query': str(self.query)})
        print(resp.json())
        self.assertEqual(resp.status_code, 200)
    '''
        
    def test_9_delete_player(self):
        self.mutation.deletePlayer(name=self.RNAME)
        #print(self.mutation)
        resp = requests.post(self.BASE + "/players", json={'query': str(self.mutation)})
        self.assertEqual(resp.status_code, 200)
        
if __name__ == '__main__':
    unittest.main()