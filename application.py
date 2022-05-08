from random import randint
from typing import List
from time import sleep

from elevator import Elevator
from floor import Floor
from run import MAX_FLOOR_NUMBER, UP, DOWN


class Application:
    OUTPUT_SEPARATOR: str = '---------------'

    def __init__(self) -> None:
        self.all_floors = self._init_floors()
        self.elevator = Elevator(
            direction=UP,
            passengers=[],
            current_floor=1
        )

    def run(self) -> None:
        while len(self.elevator.passengers) or self._get_total_passenger_number():
            for floor in self.all_floors:
                # sleep(2)
                self.elevator.current_floor = floor.number
                self._show_elevator_details()

                self._change_elevator_direction_needed()
                if not self.elevator.passengers and not floor.passengers:
                    print(f'No one on the floor and in the elevator')
                    print(self.OUTPUT_SEPARATOR)
                    continue

                escaping_people = self.elevator.escape_passenger(floor)  # passengers get off the elevator
                floor.add_new_passengers(escaping_people)
                elevator_free_place_number = self.elevator.count_free_places()

                if elevator_free_place_number == 0:
                    print("Elevator doesn't have free places")
                    print(self.OUTPUT_SEPARATOR)
                    continue

                new_elevator_passenger = self._find_new_elevator_passengers(
                    floor=floor,
                    elevator_free_place_number=elevator_free_place_number
                )

                self._show_total_floors_details()
                self.elevator.passengers.extend(new_elevator_passenger)
                floor.remove_passengers(new_elevator_passenger)

        print(f'Total passengers number on the floors: {self._get_total_passenger_number()}')

    def _change_elevator_direction_needed(self) -> None:
        """
        The method changes the direction of the elevator if it reaches the upper and lower floors
        """
        if self.elevator.direction == UP and self.elevator.current_floor == MAX_FLOOR_NUMBER:
            self.elevator.change_direction(DOWN)
            self.all_floors.reverse()

        elif self.elevator.direction == DOWN and self.elevator.current_floor == 1:
            self.elevator.change_direction(UP)
            self.all_floors.reverse()

    def _find_new_elevator_passengers(self, floor: Floor, elevator_free_place_number: int) -> List[int]:
        new_elevator_passenger = []
        for fl_pas in floor.passengers:
            if len(new_elevator_passenger) == elevator_free_place_number:
                break

            if not self.elevator.passengers:
                new_elevator_passenger.append(fl_pas)

            elif self.elevator.direction == UP and fl_pas > floor.number:
                new_elevator_passenger.append(fl_pas)

            elif self.elevator.direction == DOWN and fl_pas < floor.number:
                new_elevator_passenger.append(fl_pas)

        return new_elevator_passenger

    def _show_elevator_details(self) -> None:
        print(
            f'Elevator floor: {self.elevator.current_floor} - '
            f'Elevator passengers: {self.elevator.passengers} - '
            f'Direction {"UP" if self.elevator.direction == UP else "DOWN"}'
        )

    def _show_total_floors_details(self) -> None:
        print(self.all_floors)
        print(self.OUTPUT_SEPARATOR)

    def _get_total_passenger_number(self) -> int:
        return sum([len(f.passengers) for f in self.all_floors])

    @staticmethod
    def _init_floors() -> List[Floor]:
        """
        The method generates the maximum number of floors,
        generates a random number of passengers on each floor from 1 to 10,
        and assigns each passenger a random floor.
        """
        floors = []
        for number_floor in range(1, MAX_FLOOR_NUMBER + 1):
            floor = Floor(passengers=[], number=1)

            floor.number = number_floor
            floor.passengers = []

            for _ in range(1, randint(1, 10)):

                num = randint(1, MAX_FLOOR_NUMBER)
                while floor.number == num:
                    num = randint(1, MAX_FLOOR_NUMBER)
                floor.passengers.append(num)

            floors.append(floor)
        return floors
