import unittest
import os
import json

from app.app import create_app, db
from app.config import app_config
from tests.data import admin_user4, new_airline3, flight, user_data


class FlightTestCase(unittest.TestCase):
    """This class represents the flight test cases"""
    
    @classmethod
    def setUpClass(self):
        """Define test variables and initialize app."""
        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client

        db.session.add(admin_user4)
        db.session.add(new_airline3)
        db.session.commit()

    @classmethod
    def tearDownClass(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_flight_creation(self):
        """Test API successfully creates a flight"""

        res1 = self.client().post('/api/v1/auth/signin', data=json.dumps(user_data[16]), content_type="application/json")
        res1 = json.loads(res1.data)
        token = res1['data'][0]['token']

        res = self.client().post(
            '/api/v1/flight',
            data=json.dumps(flight[0]),
            headers={
                'content-type': 'application/json',
                'auth-token': token
            }
        )
        self.assertEqual(res.status_code, 201)
        response = json.loads(res.data)
        self.assertTrue(response['data'][0]['id'])

    def test_flight_creation_without_airlineID(self):
        """Test API won't create flight without airlineID"""

        res1 = self.client().post('/api/v1/auth/signin', data=json.dumps(user_data[16]), content_type="application/json")
        res1 = json.loads(res1.data)
        token = res1['data'][0]['token']

        res = self.client().post(
            '/api/v1/flight',
            data=json.dumps(flight[1]),
            headers={
                'content-type': 'application/json',
                'auth-token': token
            }
        )
        self.assertEqual(res.status_code, 400)
        response = json.loads(res.data)
        self.assertTrue(response['error'])

    def test_flight_creation_without_departureTime(self):
        """Test API won't create flight without departureTime"""

        res1 = self.client().post('/api/v1/auth/signin', data=json.dumps(user_data[16]), content_type="application/json")
        res1 = json.loads(res1.data)
        token = res1['data'][0]['token']

        res = self.client().post(
            '/api/v1/flight',
            data=json.dumps(flight[2]),
            headers={
                'content-type': 'application/json',
                'auth-token': token
            }
        )
        self.assertEqual(res.status_code, 400)
        response = json.loads(res.data)
        self.assertTrue(response['error'])

    def test_flight_creation_without_departureDate(self):
        """Test API won't create flight without departureDate"""

        res1 = self.client().post('/api/v1/auth/signin', data=json.dumps(user_data[16]), content_type="application/json")
        res1 = json.loads(res1.data)
        token = res1['data'][0]['token']

        res = self.client().post(
            '/api/v1/flight',
            data=json.dumps(flight[3]),
            headers={
                'content-type': 'application/json',
                'auth-token': token
            }
        )
        self.assertEqual(res.status_code, 400)
        response = json.loads(res.data)
        self.assertTrue(response['error'])

    def test_flight_creation_without_noOfSeats(self):
        """Test API won't create flight without noOfSeats"""

        res1 = self.client().post('/api/v1/auth/signin', data=json.dumps(user_data[16]), content_type="application/json")
        res1 = json.loads(res1.data)
        token = res1['data'][0]['token']

        res = self.client().post(
            '/api/v1/flight',
            data=json.dumps(flight[4]),
            headers={
                'content-type': 'application/json',
                'auth-token': token
            }
        )
        self.assertEqual(res.status_code, 400)
        response = json.loads(res.data)
        self.assertTrue(response['error'])

    def test_flight_creation_without_arrivalTime(self):
        """Test API won't create flight without arrivalTime"""

        res1 = self.client().post('/api/v1/auth/signin', data=json.dumps(user_data[16]), content_type="application/json")
        res1 = json.loads(res1.data)
        token = res1['data'][0]['token']

        res = self.client().post(
            '/api/v1/flight',
            data=json.dumps(flight[5]),
            headers={
                'content-type': 'application/json',
                'auth-token': token
            }
        )
        self.assertEqual(res.status_code, 400)
        response = json.loads(res.data)
        self.assertTrue(response['error'])

    def test_flight_creation_without_price(self):
        """Test API won't create flight without price"""

        res1 = self.client().post('/api/v1/auth/signin', data=json.dumps(user_data[16]), content_type="application/json")
        res1 = json.loads(res1.data)
        token = res1['data'][0]['token']

        res = self.client().post(
            '/api/v1/flight',
            data=json.dumps(flight[6]),
            headers={
                'content-type': 'application/json',
                'auth-token': token
            }
        )
        self.assertEqual(res.status_code, 400)
        response = json.loads(res.data)
        self.assertTrue(response['error'])

    def test_flight_creation_without_status(self):
        """Test API won't create flight without status"""

        res1 = self.client().post('/api/v1/auth/signin', data=json.dumps(user_data[16]), content_type="application/json")
        res1 = json.loads(res1.data)
        token = res1['data'][0]['token']

        res = self.client().post(
            '/api/v1/flight',
            data=json.dumps(flight[7]),
            headers={
                'content-type': 'application/json',
                'auth-token': token
            }
        )
        self.assertEqual(res.status_code, 400)
        response = json.loads(res.data)
        self.assertTrue(response['error'])

    def test_flight_creation_without_departureLocation(self):
        """Test API won't create flight without departureLocation"""

        res1 = self.client().post('/api/v1/auth/signin', data=json.dumps(user_data[16]), content_type="application/json")
        res1 = json.loads(res1.data)
        token = res1['data'][0]['token']

        res = self.client().post(
            '/api/v1/flight',
            data=json.dumps(flight[8]),
            headers={
                'content-type': 'application/json',
                'auth-token': token
            }
        )
        self.assertEqual(res.status_code, 400)
        response = json.loads(res.data)
        self.assertTrue(response['error'])

    def test_flight_creation_without_arrivalLocation(self):
        """Test API won't create flight without arrivalLocation"""

        res1 = self.client().post('/api/v1/auth/signin', data=json.dumps(user_data[16]), content_type="application/json")
        res1 = json.loads(res1.data)
        token = res1['data'][0]['token']

        res = self.client().post(
            '/api/v1/flight',
            data=json.dumps(flight[9]),
            headers={
                'content-type': 'application/json',
                'auth-token': token
            }
        )
        self.assertEqual(res.status_code, 400)
        response = json.loads(res.data)
        self.assertTrue(response['error'])

if __name__ == "__main__":
    unittest.main()