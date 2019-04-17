from locust import HttpLocust, TaskSet, task


class RandomStresstest(TaskSet):
    @task(2)
    def list(self):
        self.client.get('/random-list')

    @task(1)
    def insert_random_value(self):
        self.client.put('/random', {'lower': 0, 'upper': 10000})


class RandomUsecase(HttpLocust):
    task_set = RandomStresstest
    min_wait = 5000
    max_wait = 9000