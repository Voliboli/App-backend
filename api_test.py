import requests
import unittest
from sgqlc.types import String, Type, Field, ID, Boolean, list_of
from sgqlc.operation import Operation

class Player(Type):
    name = String
    teamName = String

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
    createPlayer = Field(PlayerResult, args={'name': String, 'teamName': String})
    updatePlayer = Field(PlayerResult, args={'name': String, 'votes': String, 'dateTeam': String})
    deletePlayer = Field(PlayerResult, args={'name': String})

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.BASE = "http://172.34.1.3:5000"
        self.query = Operation(Query)
        self.mutation = Operation(Mutation)

    def test_a_create_team(self):
        self.mutation.createTeam(name='Calcit Volley')
        resp = requests.post(self.BASE + "/teams", json={'query': str(self.mutation)})
        print(resp.json())
        self.assertTrue(resp.json()["data"]["createTeam"]["success"])

    def test_b_create_team(self):
        self.mutation.createTeam(name='ACH Volley')
        resp = requests.post(self.BASE + "/teams", json={'query': str(self.mutation)})
        print(resp.json())
        self.assertTrue(resp.json()["data"]["createTeam"]["success"])
        
    def test_c_create_player(self):
        self.mutation.createPlayer(name='Mark', teamName='Calcit Volley')
        resp = requests.post(self.BASE + "/players", json={'query': str(self.mutation)})
        print(resp.json())
        self.assertTrue(resp.json()["data"]["createPlayer"]["success"])

    def test_d_create_player(self):
        self.mutation.createPlayer(name='Teo', teamName='Calcit Volley')
        resp = requests.post(self.BASE + "/players", json={'query': str(self.mutation)})
        print(resp.json())
        self.assertTrue(resp.json()["data"]["createPlayer"]["success"])

    def test_e_create_player(self):
        self.mutation.createPlayer(name='Klemen', teamName='ACH Volley')
        resp = requests.post(self.BASE + "/players", json={'query': str(self.mutation)})
        print(resp.json())
        self.assertTrue(resp.json()["data"]["createPlayer"]["success"])

    def test_f_create_preexist_player(self):
        self.mutation.createPlayer(name='Klemen', teamName='ACH Volley')
        resp = requests.post(self.BASE + "/players", json={'query': str(self.mutation)})
        print(resp.json())
        self.assertFalse(resp.json()["data"]["createPlayer"]["success"])

    def test_g_get_teams(self):
        self.query.getTeams()
        resp = requests.post(self.BASE + "/teams", json={'query': str(self.query)})
        print(resp.json())
        self.assertTrue(resp.json()["data"]["getTeams"]["success"])

    def test_h_get_player(self):
        self.query.getPlayer(name='Mark')
        resp = requests.post(self.BASE + "/players", json={'query': str(self.query)})
        print(resp.json())
        self.assertTrue(resp.json()["data"]["getPlayer"]["success"])
      
    def test_i_get_players(self):
        self.query.getPlayers()
        resp = requests.post(self.BASE + "/players", json={'query': str(self.query)})
        print(resp.json())
        self.assertTrue(resp.json()["data"]["getPlayers"]["success"])
    
    def test_j_update_player(self):
        self.mutation.updatePlayer(name='Mark', votes='not null', dateTeam='test')
        resp = requests.post(self.BASE + "/players", json={'query': str(self.mutation)})
        print(resp.json())
        self.assertTrue(resp.json()["data"]["updatePlayer"]["success"])

    def test_k_get_players(self):
        self.query.getPlayers()
        resp = requests.post(self.BASE + "/players", json={'query': str(self.query)})
        print(resp.json())
        self.assertTrue(resp.json()["data"]["getPlayers"]["success"])

    def test_l_delete_player(self):
        self.mutation.deletePlayer(name='Teo')
        resp = requests.post(self.BASE + "/players", json={'query': str(self.mutation)})
        print(resp.json())
        self.assertTrue(resp.json()["data"]["deletePlayer"]["success"])

    def test_m_delete_player(self):
        self.mutation.deletePlayer(name='Mark')
        resp = requests.post(self.BASE + "/players", json={'query': str(self.mutation)})
        print(resp.json())
        self.assertTrue(resp.json()["data"]["deletePlayer"]["success"])
    
    def test_n_delete_player(self):
        self.mutation.deletePlayer(name='Klemen')
        resp = requests.post(self.BASE + "/players", json={'query': str(self.mutation)})
        print(resp.json())
        self.assertTrue(resp.json()["data"]["deletePlayer"]["success"])

    def test_o_delete_team(self):
        self.mutation.deleteTeam(name='Calcit Volley')
        resp = requests.post(self.BASE + "/teams", json={'query': str(self.mutation)})
        print(resp.json())
        self.assertTrue(resp.json()["data"]["deleteTeam"]["success"])

    def test_p_delete_team(self):
        self.mutation.deleteTeam(name='ACH Volley')
        resp = requests.post(self.BASE + "/teams", json={'query': str(self.mutation)})
        print(resp.json())
        self.assertTrue(resp.json()["data"]["deleteTeam"]["success"])

    def test_r_get_players(self):
        self.query.getPlayers()
        resp = requests.post(self.BASE + "/players", json={'query': str(self.query)})
        print(resp.json())
        self.assertTrue(resp.json()["data"]["getPlayers"]["success"])

if __name__ == '__main__':
    unittest.main()
