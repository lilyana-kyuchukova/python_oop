import itertools


class Trainer:
    trainer_id = itertools.count(1)

    def __init__(self, name: str):
        self.name = name
        self.id = self.get_next_id()

    @staticmethod
    def get_next_id():
        return next(Trainer.trainer_id)

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"
