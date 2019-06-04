import unittest
import os
import json

from app.app import create_app, db
from app.config import app_config
from tests.data import admin, airlines, flight, user_data, user


class FlightSeatCase(unittest.TestCase):
    """This class represents the flight seat test cases"""

    @classmethod
    def setUpClass(self):
        """Define test variables and initialize app."""
        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client

        db.session.add(admin[0])
        db.session.add(airlines[0])
        db.session.add(user[0])
        db.session.commit()

    @classmethod
    def tearDownClass(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_get_all_available_flight_seats(self):
        """Test API successfully gets all available flight seat for a flight"""

        res1 = self.client().post('/api/v1/auth/signin', data=json.dumps(user_data[16]), content_type="application/json")
        res1 = json.loads(res1.data)
        token = res1['data'][0]['token']

        res2 = self.client().post(
            '/api/v1/flight',
            data=json.dumps(flight[0]),
            headers={
                'content-type': 'application/json',
                'auth-token': token
            }
        )
        res2 = json.loads(res2.data)

        res3 = self.client().post('/api/v1/auth/signin', data=json.dumps(user_data[0]), content_type="application/json")
        res3 = json.loads(res3.data)
        token2 = res3['data'][0]['token']

        res4 = self.client().get(
            '/api/v1/flight/%s/seats'%res2['data'][0]['flightCode'],
            headers={
                'content-type': 'application/json',
                'auth-token': token2
            }
        )
        self.assertEqual(res4.status_code, 200)

if __name__ == "__main__":
    unittest.main()

        