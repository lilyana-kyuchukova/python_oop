import itertools


class Customer:

    personal_id = itertools.count(1)

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.id = self.get_next_id()

        next(Customer.personal_id)

    @staticmethod
    def get_next_id():
        return next(Customer.personal_id)

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"
