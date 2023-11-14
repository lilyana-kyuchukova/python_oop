import itertools


class Subscription:
    sub_id = itertools.count(1)

    def __init__(self, date: str, customer_id: int, trainer_id: int, exercise_id: int):
        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id
        self.id = self.get_next_id()

    @staticmethod
    def get_next_id():
        return next(Subscription.sub_id)

    def __repr__(self):
        return f"Subscription <{self.id}> on {self.date}"
