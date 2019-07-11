import json
from locust import HttpLocust, TaskSet, task


class AppTaskSet(TaskSet):
    
    def on_start(self):
        self.login()

    def login(self):
        data = {'email': 'admin@email.com', 'password': 'asdf;lkj'}
        json_data = json.dumps(data)
        response = self.client.post("/api/v1/auth/signin", json_data, headers={'Content-Type': 'application/json'})
        response_data = json.loads(response._content).get('data')
        self.token = response_data[0]['token']

    @task(1)
    def get_flights(self):
        self.client.get("/api/v1/flight", headers={'auth_token': self.token})

    @task(2)
    def get_a_flight(self):
        self.client.get("/api/v1/flight/2", headers={'auth_token': self.token})

    @task(3)
    def get_booked_flight_users(self):
        self.client.get("/api/v1/flight/2/booked", headers={'auth_token': self.token})

    @task(4)
    def get_available_airline_ticket(self):
        self.client.get("/api/v1/airline", headers={'auth_token': self.token})


class WebsiteUser(HttpLocust):
    task_set = AppTaskSet
    min_wait = 4000
    max_wait = 8000
