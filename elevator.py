from typing import List

from floor import Floor


class Elevator:
    MAX_PASSENGER: int = 5

    def __init__(self, direction: int, passengers: List[int], current_floor: int):
        self.direction = direction
        self.passengers = passengers
        self.current_floor = current_floor

    def count_free_places(self) -> int:
        return self.MAX_PASSENGER - len(self.passengers)

    def escape_passenger(self, floor: Floor) -> List[int]:
        """
        The method drops arriving passengers from the elevator to the desired floor
        """
        left_passenger: List[int] = [pas for pas in self.passengers if pas == floor.number]
        self.passengers = [pas for pas in self.passengers if pas != floor.number]
        return left_passenger

    def change_direction(self, direction: int) -> int:
        self.direction = direction
        return self.direction

