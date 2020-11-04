from locust import HttpUser, task, between


class StudentUser(HttpUser):

    @task
    def tutors(self):
        self.client.get('/api/v1/tutors/', headers={
            'Auth':"JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6ImNoZTE4MTIzQHV2Zy5lZHUuZ3QiLCJleHAiOjE2MDA5Mjc0NDQsImVtYWlsIjoiY2hlMTgxMjNAdXZnLmVkdS5ndCIsIm9yaWdfaWF0IjoxNjAwMDYzNDQ0fQ.73RGVnVOPq5z57PeI-Ai-ovPXSAG7sK6o0Eiu9g2V_8",
            'Content-Type':'application/json'
        })