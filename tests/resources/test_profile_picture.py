import unittest
import os
import io
import json

from app.app import create_app, db
from app.config import app_config
from tests.data import user_data


token = ""

class ProfilePictureTestCase(unittest.TestCase):
    """This class represents the profile picture tests"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_successful_profile_upload(self):
        """Test Api can upload a profile picture"""
        # signup a user
        res = self.client().post(
            '/api/v1/auth/signup',
            data=json.dumps(user_data[0]),
            headers={
                'content-type': 'application/json'
            }
            )
        self.assertEqual(res.status_code, 201)
        token = json.loads(res.data)['data'][0]['token']

        # upload a profile picture for the user
        data = dict()
        data['profilePicture'] = (io.BytesIO(b"abcdef"), '../test_file.png')

        response = self.client().post(
            '/api/v1/profile-picture',
            data = data,
            headers={
                'content-type': 'multipart/form-data',
                'auth_token': token
            }
            )
        self.assertEqual(response.status_code, 200)
        res_data = json.loads(response.data)
        self.assertTrue(res_data['data'][0]['msg'])

    def test_no_token_validation(self):
        """Test Api would through an authentication error"""

        # upload a profile picture for the user
        data = dict()
        data['profilePicture'] = (io.BytesIO(b"abcdef"), '../test_file.png')

        response = self.client().post(
            '/api/v1/profile-picture',
            data = data,
            headers={
                'content-type': 'multipart/form-data',
            }
            )
        self.assertEqual(response.status_code, 401)
        res_data = json.loads(response.data)
        self.assertTrue(res_data['error'])

    def test_unsuccessful_profile_upload(self):
        """Test Api throws an error when there's no profile picture"""
        # signup a user
        res = self.client().post(
            '/api/v1/auth/signup',
            data=json.dumps(user_data[0]),
            headers={
                'content-type': 'application/json'
            }
            )
        self.assertEqual(res.status_code, 201)
        token = json.loads(res.data)['data'][0]['token']

        # upload a profile picture for the user
        response = self.client().post(
            '/api/v1/profile-picture',
            headers={
                'content-type': 'multipart/form-data',
                'auth_token': token
            }
            )
        self.assertEqual(response.status_code, 400)
        res_data = json.loads(response.data)
        self.assertTrue(res_data['error'])

