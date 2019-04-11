import unittest
import os
import json

from app.app import create_app, db
from tests.data import user_data, admin_user2
from app.config import app_config


class AuthenticationTestCase(unittest.TestCase):
    """This class represents the authentication test case"""

    @classmethod
    def setUpClass(self):
        """Define test variables and initialize app."""
        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client

        db.session.add(admin_user2)
        db.session.commit()

    @classmethod
    def tearDownClass(self):
        print('===>> I m done oooo!!!')
        db.session.remove()
        db.drop_all()
        self.app_context.pop()


    def test_user_successful_signup(self):
        """Test Api can signup a new user (POST request)"""
        res = self.client().post('/api/v1/auth/signup', data=json.dumps(user_data[0]), content_type="application/json")
        self.assertEqual(res.status_code, 201)
        response = json.loads(res.data)
        self.assertTrue(response['data'][0]['token'])

    def test_white_space_during_signup(self):
        """Test api doesn't signup when there's whitespace (POST request)"""
        res = self.client().post('/api/v1/auth/signup', data=json.dumps(user_data[12]), content_type="application/json")
        self.assertEqual(res.status_code, 400)
        response = json.loads(res.data)
        self.assertTrue(response['error'])

    def test_error_no_data_signup(self):
        """Test Api won't signup when no data is sent (POST request"""
        res = self.client().post('/api/v1/auth/signup', data=json.dumps({}), content_type="application/json")
        self.assertEqual(res.status_code, 400)
        response = json.loads(res.data)
        self.assertTrue(response['error'])

    def test_incomplete_user_firstname_signup(self):
        """Test Api won't signup a user without firstname (POST request)"""
        res = self.client().post('/api/v1/auth/signup', data=json.dumps(user_data[1]), content_type="application/json")
        self.assertEqual(res.status_code, 400)
        response = json.loads(res.data)
        self.assertTrue(response['error'])

    def test_incomplete_user_lastname_signup(self):
        """Test Api won't signup a user without lastname (POST request)"""
        res = self.client().post('/api/v1/auth/signup', data=json.dumps(user_data[2]), content_type="application/json")
        self.assertEqual(res.status_code, 400)
        response = json.loads(res.data)
        self.assertTrue(response['error'])

    def test_incomplete_user_tel_signup(self):
        """Test Api won't signup a user without phone number (POST request)"""
        res = self.client().post('/api/v1/auth/signup', data=json.dumps(user_data[3]), content_type="application/json")
        self.assertEqual(res.status_code, 400)
        response = json.loads(res.data)
        self.assertTrue(response['error'])

    def test_incomplete_user_email_signup(self):
        """Test Api won't signup a user without email (POST request)"""
        res = self.client().post('/api/v1/auth/signup', data=json.dumps(user_data[4]), content_type="application/json")
        self.assertEqual(res.status_code, 400)
        response = json.loads(res.data)
        self.assertTrue(response['error'])

    def test_incomplete_user_password_signup(self):
        """Test Api won't signup a user without password (POST request)"""
        res = self.client().post('/api/v1/auth/signup', data=json.dumps(user_data[5]), content_type="application/json")
        self.assertEqual(res.status_code, 400)
        response = json.loads(res.data)
        self.assertTrue(response['error'])

    def test_invalid_email_user_signup(self):
        """Test Api won't signup a user with an invalid email(POST request)"""
        res = self.client().post('/api/v1/auth/signup', data=json.dumps(user_data[14]), content_type="application/json")
        self.assertEqual(res.status_code, 400)
        response = json.loads(res.data)
        self.assertTrue(response['error'])

    def test_signup_user_exist(self):
        """Test Api won't signup a user that already exists (POST request)"""
        signup_response = self.client().post('/api/v1/auth/signup', data=json.dumps(user_data[13]), content_type="application/json")
        self.assertEqual(signup_response.status_code, 201 )
        res = self.client().post('/api/v1/auth/signup', data=json.dumps(user_data[13]), content_type="application/json")
        self.assertEqual(res.status_code, 400)
        response = json.loads(res.data)
        self.assertTrue(response['error'])

    def test_user_successful_signin(self):
        """Test Api can signin a user (POST request)"""
        signup_response = self.client().post('/api/v1/auth/signup', data=json.dumps(user_data[6]), content_type="application/json")
        self.assertEqual(signup_response.status_code, 201 )
        res = self.client().post('/api/v1/auth/signin', data=json.dumps(user_data[6]), content_type="application/json")
        self.assertEqual(res.status_code, 200)
        response = json.loads(res.data)
        self.assertTrue(response['data'][0]['token'])

    def test_incomplete_user_email_signin(self):
        """Test Api won't signin a user without email (POST request)"""
        res = self.client().post('/api/v1/auth/signin', data=json.dumps(user_data[4]), content_type="application/json")
        self.assertEqual(res.status_code, 400)
        response = json.loads(res.data)
        self.assertTrue(response['error'])

    def test_incomplete_user_password_signin(self):
        """Test Api won't signin a user without password (POST request)"""
        res = self.client().post('/api/v1/auth/signin', data=json.dumps(user_data[5]), content_type="application/json")
        self.assertEqual(res.status_code, 400)
        response = json.loads(res.data)
        self.assertTrue(response['error'])

    def test_user_incorrect_password_signin(self):
        """Test Api won't signin a user with incorrect password (POST request)"""
        signup_response = self.client().post('/api/v1/auth/signup', data=json.dumps(user_data[8]), content_type="application/json")
        self.assertEqual(signup_response.status_code, 201 )
        res = self.client().post('/api/v1/auth/signin', data=json.dumps(user_data[9]), content_type="application/json")
        self.assertEqual(res.status_code, 400)
        response = json.loads(res.data)
        self.assertTrue(response['error'])

    def test_user_incorrect_signin(self):
        """Test Api won't signin a user that does not exist (POST request)"""
        res = self.client().post('/api/v1/auth/signin', data=json.dumps(user_data[10]), content_type="application/json")
        self.assertEqual(res.status_code, 400)
        response = json.loads(res.data)
        self.assertTrue(response['error'])

    def test_signin_admin(self):
        """Test api can signin an admin"""
        res = self.client().post('/api/v1/auth/signin', data=json.dumps(user_data[15]), content_type="application/json")
        response = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(response['data'][0]['token'])
            

    def test_default_route(self):
        """Test Api can get the default route (GET request)"""
        res = self.client().get('/',)
        self.assertEqual(res.status_code, 200)
                
                
if __name__ == "__main__":
    unittest.main()
