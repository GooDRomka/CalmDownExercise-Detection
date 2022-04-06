from locust import HttpUser, TaskSet, task, between, tag

"""
Run locus with:
locust -f ./tests/load_test.py
"""


class IrisPredict(TaskSet):
    @tag('Predictions')
    @task
    def predict(self):
        request_body = {"data":{"text":"I wanted nails like 39 minutes ago I wanted nails I couldnt I started crying going manic I hobbies makes feel better fat ass fingers No I dont like hobbies"}}
        self.client.post('/v1/iris/predict', json=request_body)

    @tag('Baseline')
    @task
    def health_check(self):
        self.client.get('/')


class IrisLoadTest(HttpUser):
    tasks = [IrisPredict]
    host = 'http://127.0.0.1'
    stop_timeout = 200
    wait_time = between(1, 5)
