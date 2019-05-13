from app.models.user import User
from app.models.airline import Airline
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
    },
    {
        "email": "admintestuser2@email.com",
        "password": "asdf;lkj"
    },
    {
        "email": "admintestuser4@email.com",
        "password": "asdf;lkj"
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

new_airline1 = Airline(
    name= "Delta Airways",
    name_abb="DA"
)

new_airline2 = Airline(
    name= "Air Peace",
    name_abb="AP"
)

new_airline3 = Airline(
    name= "Arik Air",
    name_abb="AA"
)

admin_user2 = User(
    firstname= 'admintestuser2',
    lastname='admintestuser2',
    tel='12345678900',
    email='admintestuser2@email.com',
    password=generate_hash('asdf;lkj'),
    is_admin=True
)

admin_user3 = User(
    firstname= 'admintestuser3',
    lastname='admintestuser3',
    tel='12345678900',
    email='admintestuser3@email.com',
    password=generate_hash('asdf;lkj'),
    is_admin=True
)

admin_user4 = User(
    firstname= 'admintestuser4',
    lastname='admintestuser4',
    tel='12345678900',
    email='admintestuser4@email.com',
    password=generate_hash('asdf;lkj'),
    is_admin=True
)

airline = [
    {
        "name": "Delta Airline",
        "nameAbb": "DL"
    },
    {
        "nameAbb": "AP"
    },
    {
        "name": "Delta Airline"
    },
    {
        "name": "Arik",
        "nameAbb": "AK"
    },
    {
        "name": "British",
        "nameAbb": "AK"
    },
    {
        "name": "Arik",
        "nameAbb": "BH"
    },
    {
        "name": "Delta AirlineS",
        "nameAbb": "DAS"
    },
    {
        "name": "Air Peace",
        "nameAbb": "DA"
    },
    {
        "name": "Delta Airways",
        "nameAbb": "AP"
    }
]

flight = [
    {
        "airlineID": "1",
        "departureTime": "22:05",
        "departureDate": "2019-09-09",
        "noOfSeats": 10,
        "arrivalTime": "05:30",
        "price": 600,
        "status": "active",
        "departureLocation": "Lagos",
        "arrivalLocation": "Los Angeles"
    },
    {
        "departureTime": "22:05",
        "departureDate": "2019-09-09",
        "noOfSeats": 10,
        "arrivalTime": "05:30",
        "price": 600,
        "status": "active",
        "departureLocation": "Lagos",
        "arrivalLocation": "Los Angeles"
    },
    {
        "airlineID": "1",
        "departureDate": "2019-09-09",
        "noOfSeats": 10,
        "arrivalTime": "05:30",
        "price": 600,
        "status": "active",
        "departureLocation": "Lagos",
        "arrivalLocation": "Los Angeles"
    },
    {
        "airlineID": "1",
        "departureTime": "22:05",
        "noOfSeats": 10,
        "arrivalTime": "05:30",
        "price": 600,
        "status": "active",
        "departureLocation": "Lagos",
        "arrivalLocation": "Los Angeles"
    },
    {
        "airlineID": "1",
        "departureTime": "22:05",
        "departureDate": "2019-09-09",
        "arrivalTime": "05:30",
        "price": 600,
        "status": "active",
        "departureLocation": "Lagos",
        "arrivalLocation": "Los Angeles"
    },
    {
        "airlineID": "1",
        "departureTime": "22:05",
        "departureDate": "2019-09-09",
        "noOfSeats": 10,
        "price": 600,
        "status": "active",
        "departureLocation": "Lagos",
        "arrivalLocation": "Los Angeles"
    },
    {
        "airlineID": "1",
        "departureTime": "22:05",
        "departureDate": "2019-09-09",
        "noOfSeats": 10,
        "arrivalTime": "05:30",
        "status": "active",
        "departureLocation": "Lagos",
        "arrivalLocation": "Los Angeles"
    },
    {
        "airlineID": "1",
        "departureTime": "22:05",
        "departureDate": "2019-09-09",
        "noOfSeats": 10,
        "arrivalTime": "05:30",
        "price": 600,
        "departureLocation": "Lagos",
        "arrivalLocation": "Los Angeles"
    },
    {
        "airlineID": "1",
        "departureTime": "22:05",
        "departureDate": "2019-09-09",
        "noOfSeats": 10,
        "arrivalTime": "05:30",
        "price": 600,
        "departureLocation": "Lagos",
        "arrivalLocation": "Los Angeles"
    },
    {
        "airlineID": "1",
        "departureTime": "22:05",
        "departureDate": "2019-09-09",
        "noOfSeats": 10,
        "arrivalTime": "05:30",
        "price": 600,
        "status": "active",
        "arrivalLocation": "Los Angeles"
    },
    {
        "airlineID": "1",
        "departureTime": "22:05",
        "departureDate": "2019-09-09",
        "noOfSeats": 10,
        "arrivalTime": "05:30",
        "price": 600,
        "status": "active",
        "departureLocation": "Lagos",
    }
]