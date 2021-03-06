from locust import HttpUser, TaskSet, task, between, tag

"""
Run locus with:
locust -f ./tests/load_test.py
"""


class ElomiaPredict(TaskSet):
    @tag('Predictions')
    @task
    def predict(self):
        request_body = {"data": {"text":['The argument was about her ex-friend I tried to take up for her but she just started cursing at me. I think she reacted this way because she also said you and my ex bsf can be friends then I tried helping her taking up for her and I think she just went mad we argued on discord a very bad app for people we argued in front of 100 people. I feel sad and frustrated about this situation.',
 " I wanted to do my nails because just like 39 minutes ago I wanted to do my nails but I couldn't do it because I started crying and going all manic. I have no hobbies because it makes me feel better about my fat ass fingers. No, I don't like to do any hobbies.",
 'I am upset. I have been feeling upset.  It is not fair I think.',
 ' I know he’s unwell because I spoke to him recently. So I know that’s true. But I don’t know if he’s unwell enough not to see me. As I said before, I‘m scared to confront him with my suspicions. If they‘re untrue then I’ll do damage to the relationship. If I damage the relationship, then it won’t be beautiful anymore and his feelings for me will cool down and then disappear.',
 ' If I become too needy or difficult, I will lose my partner. I don’t mean by "being very understanding" and "accomodating" in this context. I actually try to be very understanding and accommodating. I mean that I try to be very patient and understanding. I avoid conflict.']
                     }}
        self.client.post('/v1/elomia/predict', json=request_body)

    @tag('Baseline')
    @task
    def health_check(self):
        self.client.get('/')


class ElomiaLoadTest(HttpUser):
    tasks = [ElomiaPredict]
    host = 'http://127.0.0.1'
    stop_timeout = 200
    wait_time = between(1, 5)
