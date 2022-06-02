from locust import HttpUser, task

class TestUser(HttpUser):
	@task
	def hello(self):
		self.client.get("/")
