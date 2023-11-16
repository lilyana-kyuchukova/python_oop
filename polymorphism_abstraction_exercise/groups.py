from typing import List


class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other):
        if isinstance(other, Person):
            return Person(self.name, other.surname)


class Group:
    def __init__(self, name: str, people: List[Person]):
        self.name = name
        self.people: List[Person] = people

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        if isinstance(other, Group):
            new_group = Group("{first_name} {second_name}", self.people + other.people)
            return new_group

    def __repr__(self):
        return f"Group {self.name} with members {', '.join(map(str, self.people))}"

    def __getitem__(self, item):
        person = self.people[item]
        return f"Person {item}: {person}"


p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3
first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group + second_group
print(len(first_group))
print(second_group)
print(third_group[0])
for person in third_group:
    print(person)