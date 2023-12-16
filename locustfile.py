from locust import HttpUser, task
from faker import Faker

faker = Faker()

class HelloWorldUser(HttpUser):
    @task
    def create_user(self):
        name = faker.first_name()
        last_name = faker.last_name()
        password = '12345678'
        email = name + last_name + '@gmail.com'
        payload = {'name': name, 'password': password, 'email': email, 'role': 'admin'}
        self.client.post("/users", json=payload)
