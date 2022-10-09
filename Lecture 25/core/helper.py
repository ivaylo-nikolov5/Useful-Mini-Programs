from collections import deque
import sys


BOOL_VALUE = "The value cannot be bool type of data!"


class EmptyList(Exception):
    pass


class ValueNotExist(Exception):
    pass


class Helper:
    @staticmethod
    def find_index(values, index):
        for idx in range(len(values)):
            if idx == index:
                return idx

        raise IndexError("Invalid index!")

    @staticmethod
    def iter_over_list_or_tuple_or_string(values, iterable):
        for el in iterable:
            values.append(el)

        return values

    @staticmethod
    def iter_over_dictionary(values, iterable: dict):
        for el in iterable.keys():
            values.append(el)

        return values

    @staticmethod
    def insert_value_in_list(values, value, index):
        if index < 0 or index > len(values):
            raise IndexError("Invalid index!")

        new_values = []

        for idx in range(len(values)):
            if idx == index:
                new_values.append(value)
            new_values.append(values[idx])

        return new_values

    @staticmethod
    def return_list_as_dict(values):
        even_values = deque([values[x] for x in range(len(values)) if x % 2 == 0])
        odd_values = deque([values[x] for x in range(len(values)) if x % 2 != 0])
        if len(even_values) > len(odd_values):
            odd_values.append(" ")
        dictionary = {}

        for idx in range(len(even_values)):
            even_val = even_values[idx]
            odd_val = odd_values[idx]
            dictionary[even_val] = odd_val

        return dictionary

    @staticmethod
    def calculate_sum(values):
        sum_ = 0
        for value in values:
            if isinstance(value, bool):
                raise Exception(BOOL_VALUE)
            elif isinstance(value, str):
                sum_ += len(value)
                continue
            sum_ += value

        return sum_

    @staticmethod
    def find_biggest(values):
        if not values:
            raise EmptyList("Cannot find the biggest value in an empty list!")

        biggest = -sys.maxsize
        for value in values:
            if isinstance(value, bool):
                raise Exception(BOOL_VALUE)
            elif isinstance(value, str) and len(value) > biggest:
                biggest = len(value)
                continue
            if value > biggest:
                biggest = value

        return biggest

    @staticmethod
    def find_lowest(values):
        if not values:
            raise EmptyList("Cannot find the lowest value in an empty list!")

        lowest = sys.maxsize
        for value in values:
            if isinstance(value, bool):
                raise Exception(BOOL_VALUE)
            elif isinstance(value, str) and len(value) < lowest:
                lowest = len(value)
                continue
            if value < lowest:
                lowest = value

        return lowest
