import unittest
import os
import json

from app.app import create_app, db
from app.config import app_config
from tests.data import user_data, admin_user, airline


class AirlineTestCase(unittest.TestCase):
    """This class represents the airline test cases"""

    @classmethod
    def setUpClass(self):
        """Define test variables and initialize app."""
        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client

        db.session.add(admin_user)
        db.session.commit()

    @classmethod
    def tearDownClass(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_airline_successful_creation(self):
        """Test API works fine"""

        res1 = self.client().post('/api/v1/auth/signin', data=json.dumps(user_data[7]), content_type="application/json")
        res1 = json.loads(res1.data)
        token = res1['data'][0]['token']

        res = self.client().post(
            '/api/v1/airline',
            data=json.dumps(airline[0]),
            headers={
                'content-type': 'application/json',
                "auth_token": token
            }
            )
        self.assertEqual(res.status_code, 201)
        response = json.loads(res.data)
        self.assertTrue(response['data'][0]['name'])
        self.assertTrue(response['data'][0]['nameAbb'])

    def test_unauthorized_access_to_create_airline(self):
        """Test API does not allow non-admins to create airline"""

        res = self.client().post(
            '/api/v1/airline',
            data=json.dumps(airline[0]),
            headers={
                'content-type': 'application/json'
            }
            )
        self.assertEqual(res.status_code, 401)
        response = json.loads(res.data)
        self.assertTrue(response['error'])


    def test_incomplete_airline_without_name(self):
        """Test API does not create Airline without name"""

        res1 = self.client().post('/api/v1/auth/signin', data=json.dumps(user_data[7]), content_type="application/json")
        res1 = json.loads(res1.data)
        token = res1['data'][0]['token']

        res = self.client().post(
            '/api/v1/airline',
            data=json.dumps(airline[1]),
            headers={
                'content-type': 'application/json',
                "auth_token": token
            }
            )
        self.assertEqual(res.status_code, 400)
        response = json.loads(res.data)
        self.assertTrue(response['error'])

    def test_incomplete_airline_without_name_abb(self):
        """Test API does not create Airline without name abbrevation"""

        res1 = self.client().post('/api/v1/auth/signin', data=json.dumps(user_data[7]), content_type="application/json")
        res1 = json.loads(res1.data)
        token = res1['data'][0]['token']

        res = self.client().post(
            '/api/v1/airline',
            data=json.dumps(airline[2]),
            headers={
                'content-type': 'application/json',
                "auth_token": token
            }
            )
        self.assertEqual(res.status_code, 400)
        response = json.loads(res.data)
        self.assertTrue(response['error'])

    def test_duplicate_airline_name(self):
        """Test API does not create Airline with a duplicate name"""

        res1 = self.client().post('/api/v1/auth/signin', data=json.dumps(user_data[7]), content_type="application/json")
        res1 = json.loads(res1.data)
        token = res1['data'][0]['token']

        res = self.client().post(
            '/api/v1/airline',
            data=json.dumps(airline[3]),
            headers={
                'content-type': 'application/json',
                "auth_token": token
            }
            )
        
        self.assertEqual(res.status_code, 201)

        res2 = self.client().post(
            '/api/v1/airline',
            data=json.dumps(airline[5]),
            headers={
                'content-type': 'application/json',
                "auth_token": token
            }
        )

        self.assertEqual(res2.status_code, 400)
        response = json.loads(res2.data)
        self.assertTrue(response['error'])

        res3 = self.client().post(
            '/api/v1/airline',
            data=json.dumps(airline[4]),
            headers={
                'content-type': 'application/json',
                "auth_token": token
            }
        )

        self.assertEqual(res3.status_code, 400)
        response1 = json.loads(res3.data)
        self.assertTrue(response1['error'])


if __name__ == "__main__":
    unittest.main()