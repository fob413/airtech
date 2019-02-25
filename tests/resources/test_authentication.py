import unittest
import os
import json

from api.app import create_app, db
from tests.data import user_data


class AuthenticationTestCase(unittest.TestCase):
    """This class represents the authentication test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app("testing")
        self.client = self.app.test_client
    

        with self.app.app_context():
            db.drop_all()
            db.create_all()

    def test_user_successful_signup(self):
        """Test Api can signup a new user (POST request)"""
        res = self.client().post('/api/v1/auth/signup', data=json.dumps(user_data[0]), content_type="application/json")
        self.assertEqual(res.status_code, 201)
        response = json.loads(res.data)
        self.assertTrue(response['data'][0]['token'])

    def test_incomplete_user_firstname_signup(self):
        """Test Api won't signup a user without firstname"""
        res = self.client().post('/api/v1/auth/signup', data=json.dumps(user_data[1]), content_type="application/json")
        self.assertEqual(res.status_code, 400)
        response = json.loads(res.data)
        self.assertTrue(response['error'])

    def test_incomplete_user_lastname_signup(self):
        """Test Api won't signup a user without lastname"""
        res = self.client().post('/api/v1/auth/signup', data=json.dumps(user_data[2]), content_type="application/json")
        self.assertEqual(res.status_code, 400)
        response = json.loads(res.data)
        self.assertTrue(response['error'])

    def test_incomplete_user_tel_signup(self):
        """Test Api won't signup a user without phone number"""
        res = self.client().post('/api/v1/auth/signup', data=json.dumps(user_data[3]), content_type="application/json")
        self.assertEqual(res.status_code, 400)
        response = json.loads(res.data)
        self.assertTrue(response['error'])

    def test_incomplete_user_email_signup(self):
        """Test Api won't signup a user without email"""
        res = self.client().post('/api/v1/auth/signup', data=json.dumps(user_data[4]), content_type="application/json")
        self.assertEqual(res.status_code, 400)
        response = json.loads(res.data)
        self.assertTrue(response['error'])

    def test_incomplete_user_password_signup(self):
        """Test Api won't signup a user without password"""
        res = self.client().post('/api/v1/auth/signup', data=json.dumps(user_data[5]), content_type="application/json")
        self.assertEqual(res.status_code, 400)
        response = json.loads(res.data)
        self.assertTrue(response['error'])
                
                
if __name__ == "__main__":
    unittest.main()
