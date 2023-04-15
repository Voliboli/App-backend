import requests
import unittest
from voliboli_sgqlc_types.main import Mutation, Query
from sgqlc.operation import Operation

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.BASE = "http://172.35.1.3:5000"
        self.query = Operation(Query)
        self.mutation = Operation(Mutation)

    def test_a_create_team(self):
        self.mutation.createTeam(name='Calcit Volley')
        resp = requests.post(self.BASE + "/teams", json={'query': str(self.mutation)})
        #print(resp.json())
        self.assertTrue(resp.json()["data"]["createTeam"]["success"])

    def test_b_create_team(self):
        self.mutation.createTeam(name='ACH Volley')
        resp = requests.post(self.BASE + "/teams", json={'query': str(self.mutation)})
        #print(resp.json())
        self.assertTrue(resp.json()["data"]["createTeam"]["success"])
        
    def test_c_create_player(self):
        self.mutation.createPlayer(name='Mark', teamName='Calcit Volley')
        resp = requests.post(self.BASE + "/players", json={'query': str(self.mutation)})
        #print(resp.json())
        self.assertTrue(resp.json()["data"]["createPlayer"]["success"])

    def test_d_create_player(self):
        self.mutation.createPlayer(name='Teo', teamName='Calcit Volley')
        resp = requests.post(self.BASE + "/players", json={'query': str(self.mutation)})
        #print(resp.json())
        self.assertTrue(resp.json()["data"]["createPlayer"]["success"])

    def test_e_create_player(self):
        self.mutation.createPlayer(name='Klemen', teamName='ACH Volley')
        resp = requests.post(self.BASE + "/players", json={'query': str(self.mutation)})
        #print(resp.json())
        self.assertTrue(resp.json()["data"]["createPlayer"]["success"])

    def test_f_create_preexist_player(self):
        self.mutation.createPlayer(name='Klemen', teamName='ACH Volley')
        resp = requests.post(self.BASE + "/players", json={'query': str(self.mutation)})
        #print(resp.json())
        self.assertFalse(resp.json()["data"]["createPlayer"]["success"])

    def test_g_get_teams(self):
        self.query.getTeams()
        resp = requests.post(self.BASE + "/teams", json={'query': str(self.query)})
        #print(resp.json())
        self.assertTrue(resp.json()["data"]["getTeams"]["success"])

    def test_h_get_player(self):
        self.query.getPlayer(name='Mark')
        resp = requests.post(self.BASE + "/players", json={'query': str(self.query)})
        #print(resp.json())
        self.assertTrue(resp.json()["data"]["getPlayer"]["success"])
      
    def test_i_get_players(self):
        self.query.getPlayers()
        resp = requests.post(self.BASE + "/players", json={'query': str(self.query)})
        #print(resp.json())
        self.assertTrue(resp.json()["data"]["getPlayers"]["success"])
    
    def test_j_update_player(self):
        self.mutation.updatePlayer(name='Mark', votes='not null', dateTeam='test')
        resp = requests.post(self.BASE + "/players", json={'query': str(self.mutation)})
        #print(resp.json())
        self.assertTrue(resp.json()["data"]["updatePlayer"]["success"])

    def test_k_get_players(self):
        self.query.getPlayers()
        resp = requests.post(self.BASE + "/players", json={'query': str(self.query)})
        #print(resp.json())
        self.assertTrue(resp.json()["data"]["getPlayers"]["success"])

    def test_l_get_team(self):
        self.query.getTeam(name="Calcit Volley")
        resp = requests.post(self.BASE + "/teams", json={'query': str(self.query.__to_graphql__(auto_select_depth=3))})
        print(resp.json())
        self.assertTrue(resp.json()["data"]["getTeam"]["success"])

    def test_m_delete_player(self):
        self.mutation.deletePlayer(name='Teo')
        resp = requests.post(self.BASE + "/players", json={'query': str(self.mutation)})
        #print(resp.json())
        self.assertTrue(resp.json()["data"]["deletePlayer"]["success"])

    def test_n_delete_player(self):
        self.mutation.deletePlayer(name='Mark')
        resp = requests.post(self.BASE + "/players", json={'query': str(self.mutation)})
        #print(resp.json())
        self.assertTrue(resp.json()["data"]["deletePlayer"]["success"])
    
    def test_o_delete_player(self):
        self.mutation.deletePlayer(name='Klemen')
        resp = requests.post(self.BASE + "/players", json={'query': str(self.mutation)})
        #print(resp.json())
        self.assertTrue(resp.json()["data"]["deletePlayer"]["success"])

    def test_p_delete_team(self):
        self.mutation.deleteTeam(name='Calcit Volley')
        resp = requests.post(self.BASE + "/teams", json={'query': str(self.mutation)})
        #print(resp.json())
        self.assertTrue(resp.json()["data"]["deleteTeam"]["success"])

    def test_r_delete_team(self):
        self.mutation.deleteTeam(name='ACH Volley')
        resp = requests.post(self.BASE + "/teams", json={'query': str(self.mutation)})
        #print(resp.json())
        self.assertTrue(resp.json()["data"]["deleteTeam"]["success"])

    def test_s_get_players(self):
        self.query.getPlayers()
        resp = requests.post(self.BASE + "/players", json={'query': str(self.query)})
        #print(resp.json())
        self.assertTrue(resp.json()["data"]["getPlayers"]["success"])

if __name__ == '__main__':
    unittest.main()
