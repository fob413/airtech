from app.models.user import User
from app.utils.tools import generate_hash


user_data = [
    {
        "firstname": "testuserfirstname",
        "lastname": "testuserlastname",
        "tel": "12345678900",
        "email": "testuser@email.com",
        "password": "password"
    },
    {
        "lastname": "testuserlastname",
        "email": "testuser@email.com",
        "tel": "12345678900",
        "password": "testuserpassword"
    },
    {
        "firstname": "testuserfirstname",
        "tel": "12345678900",
        "email": "testuser@email.com",
        "password": "password"
    },
    {
        "firstname": "testuserfirstname",
        "lastname": "testuserlastname",
        "email": "testuser@email.com",
        "password": "password"
    },
    {
        "firstname": "testuserfirstname",
        "lastname": "testuserlastname",
        "tel": "12345678900",
        "password": "password"
    },
    {
        "firstname": "testuserfirstname",
        "lastname": "testuserlastname",
        "tel": "12345678900",
        "email": "testuser@email.com",
    },
    {
        "firstname": "testuserfirstname1",
        "lastname": "testuserlastname1",
        "tel": "12345678900",
        "email": "testuser1@email.com",
        "password": "password"
    },
    {
        "email": "admintestuser@email.com",
        "password": "asdf;lkj"
    },
    {
        "firstname": "testuserfirstname2",
        "lastname": "testuserlastname2",
        "tel": "12345678900",
        "email": "testuser2@email.com",
        "password": "password"
    },
    {
        "email": "testuser2@email.com",
        "password": "asdf;lkj"
    },
    {
        "email": "testuser1@email.com",
        "password": "asdf;lkj"
    },
    {
        "email": "nouser@email.com",
        "password": "asdf;lkj"
    },
    {
        "firstname": "  ",
        "lastname": "  ",
        "tel": "12345678900",
        "email": "testuser@email.com",
        "password": "password"
    },
    {
        "firstname": "existinguser",
        "lastname": "existinguser",
        "tel": "12345678900",
        "email": "existing@email.com",
        "password": "password"
    },
    {
        "firstname": "testuser",
        "lastname": "testuser",
        "tel": "12345678900",
        "email": "testuser",
        "password": "password"
    }
]

admin_user = User(
    firstname= 'admintestuser',
    lastname='admintestuser',
    tel='12345678900',
    email='admintestuser@email.com',
    password=generate_hash('asdf;lkj'),
    is_admin=True
)
