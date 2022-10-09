from core.helper import Helper, EmptyList, ValueNotExist
import copy


class CustomList:
    iterables = {
        list: Helper.iter_over_list_or_tuple_or_string,
        tuple: Helper.iter_over_list_or_tuple_or_string,
        dict: Helper.iter_over_dictionary,
        str: Helper.iter_over_list_or_tuple_or_string
    }

    def __init__(self):
        self.__values = []

    def get_list(self):
        return self.__values

    def append(self, value):
        self.__values.append(value)

    def remove(self, index):
        index = Helper.find_index(self.__values, index)
        result = self.__values[index]
        self.__values.pop(index)
        return result

    def get(self, index):
        index = Helper.find_index(self.__values, index)
        return self.__values[index]

    def extend(self, iterable):
        if type(iterable) not in self.iterables:
            raise ValueError("Value not iterable!")
        result = self.iterables[type(iterable)](self.__values, iterable)
        return result

    def insert(self, index, value):
        index = Helper.find_index(self.__values, index)
        values = Helper.insert_value_in_list(self.__values, value, index)
        self.__values = values
        return self.get_list()

    def pop(self):
        if not self.__values:
            raise EmptyList("You cannot pop an item from an empty list")
        value = self.__values[-1]
        self.__values = self.__values[:-1]
        return value

    def clear(self):
        self.__values = []

    def index(self, value):
        for idx in range(len(self.__values)):
            if self.__values[idx] == value:
                return idx
        raise ValueNotExist("The value is not in the list!")

    def count(self, value):
        result = len([x for x in self.__values if x == value])
        return result

    def reverse(self):
        if not self.__values:
            raise EmptyList("You cannot reverse an empty list!")
        result = self.__values[::-1]
        return result

    def copy(self):
        current_copy = copy.deepcopy(self.__values)
        return current_copy

    def size(self):
        return len(self.__values)

    def add_first(self, value):
        new_list = [value]
        new_list.extend(self.get_list())
        return new_list

    def dictionize(self):
        dictionary = Helper.return_list_as_dict(self.__values)
        return dictionary

    def move(self, amount):
        if amount > len(self.__values):
            raise Exception("This list has not enough elements to move!")
        part = self.__values[:amount]
        self.__values.extend(part)
        return self.__values[amount:]

    def sum(self):
        sum_ = Helper.calculate_sum(self.__values)
        return sum_

    def overbound(self):
        biggest = Helper.find_biggest(self.__values)
        return biggest

    def underbound(self):
        lowest = Helper.find_lowest(self.__values)
        return lowest

    def __str__(self):
        return str(list(self.get_list()))

    def __len__(self):
        return len(self.__values)

    def __reversed__(self):
        return self.reverse()

    def __add__(self, other):
        return self.__values + other.values





