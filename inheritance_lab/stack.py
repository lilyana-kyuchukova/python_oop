from typing import List


class Stack:
    def __init__(self):
        self.data: List[str] = list()

    def push(self, element: str) -> None:
        self.data.append(element)

    def pop(self) -> str:
        return self.data.pop()

    def top(self) -> str:
        return self.data[-1]

    def is_empty(self) -> bool:
        return len(self.data) == 0

        # if self.data:
        #     return True
        #
        # return False

    def __str__(self):
        return "[" + ", ".join([f"{self.data[i]}" for i in range(len(self.data) - 1, -1, -1)]) + "]"
