from typing import List
from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = list()
        self.workers: List[Worker] = list()

    def add_animal(self, animal: Animal, price: int):
        if self.__budget < price:
            return "Not enough budget"

        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        try:
            worker = next(filter(lambda w: w.name == worker_name, self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        sum_salary = sum(s.salary for s in self.workers)
        if sum_salary > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= sum_salary
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        sum_needs = sum(s.money_for_care for s in self.animals)
        if sum_needs > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= sum_needs
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = list(filter(lambda a: a.__class__.__name__ == "Lion", self.animals))
        tigers = list(filter(lambda a: a.__class__.__name__ == "Tiger", self.animals))
        cheetahs = list(filter(lambda a: a.__class__.__name__ == "Cheetah", self.animals))
        result = [
            f"You have {len(self.animals)} animals",
            f"----- {len(lions)} Lions:"]

        result.extend(*lions)

        result.append(f"----- {len(tigers)} Tigers:")
        result.extend(*tigers)

        result.append(f"----- {len(cheetahs)} Cheetahs:")
        result.extend(*cheetahs)

        return "\n".join(result)

    def workers_status(self):
        info = {"Keeper": list(),
                "Caretaker": list(),
                "Vet": list()}
        [info[w.__class__.__name__].append(str(w)) for w in self.workers]

        result = [f'You have {len(self.workers)} workers',
                  f'----- {len(info["Keeper"])} Keepers:',
                  *info["Keeper"],
                  f'----- {len(info["Caretaker"])} Caretakers:',
                  *info["Caretaker"],
                  f'----- {len(info["Vet"])} Vets:',
                  *info["Vet"]
                  ]

        return "\n".join(result)


