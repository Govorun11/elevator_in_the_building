from random import randint
from typing import List

from run import MAX_FLOOR_NUMBER


class Floor:

    def __init__(self, passengers: List[int], number: int) -> None:
        self.passengers = passengers
        self.number = number

    def __repr__(self) -> str:
        return f'Этаж номер {self.number}, ожидают лифт{self.passengers}.\n'

    def add_new_passengers(self, new_passengers: List[int]) -> None:
        """
        The method adds new passengers to the current floor while regenerating the number of the next floor for them.
        """
        for new_pas in new_passengers:
            if new_pas == 1:
                continue

            num = self._assign_passenger_to_new_floor()
            self.passengers.append(num)

    def _assign_passenger_to_new_floor(self) -> int:
        """
        The method generates a new target floor value different from the current one.
        """
        num = randint(1, MAX_FLOOR_NUMBER)
        while self.number == num:
            num = randint(1, MAX_FLOOR_NUMBER)
        return num

    def remove_passengers(self, old_passengers: List[int]) -> None:
        for passenger in old_passengers:
            self.passengers.remove(passenger)
