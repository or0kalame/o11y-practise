from locust import HttpUser, task, between
import random
import string

def random_string(length=8):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

class GetPackageUser(HttpUser):
    wait_time = between(0.5, 1.5)

    def on_start(self):
        try:
            resp = self.client.get("/tracking_numbers", timeout=10)
            if resp.status_code == 200:
                self.tracking_numbers = [tn for tn in resp.json() if isinstance(tn, str)][:21]
            else:
                self.tracking_numbers = []
        except Exception as e:
            self.tracking_numbers = []

    @task
    def get_package(self):
        if not self.tracking_numbers:
            return
        tn = random.choice(self.tracking_numbers)
        self.client.get("/get", params={"tracking_number": tn})


