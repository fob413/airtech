import os
import uuid

from flask_restful import Resource
from flask import request, g
from werkzeug.utils import secure_filename

from app import app
from app.models.user import User
from app.utils.validator import Validator
from app.utils.tools import (
    success_response,
    error_response
)


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_secure_filename(file):
    name = secure_filename(file.filename)
    filename = name.split('.')
    filename[0] = filename[0] + '_' + uuid.uuid1().__str__()
    return '.'.join(filename)


class Profile(Resource):
    """
    Upload profile picture
    """

    @Validator.validate_token()
    def post(self):
        if 'profilePicture' not in request.files:
            return error_response('profilePicture is required', 400)

        picture = request.files['profilePicture']

        if picture.filename == '':
            return error_response('Invalid picture format', 400)
        
        if picture and allowed_file(picture.filename):
            filename = get_secure_filename(picture)
            picture.save(os.path.join('./static', filename))

            # save profile picture name to the database
            user = User.query.filter_by(id=g.user_id).first()

            user.profile = filename
            user.save()

            return success_response({'msg': 'Successfully uploaded the profile picture'}, 200)
        else:
            return error_response('Invalid picture format', 400)
