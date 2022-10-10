class HashTable:
    min_length = 4

    def __init__(self):
        self.__keys = [None] * HashTable.min_length
        self.__values = [None] * HashTable.min_length

    def __getitem__(self, item):
        index = self.__keys.index(item)
        return self.__values[index]

    def __setitem__(self, key, value):
        if key in self.__keys:
            key = self.__keys.index(key)
            self.__values[key] = value
            return
        if self.size() == self.min_length:
            self.resize()
        index = self.__calculate_index(key)
        index = self.__find_available_index(index)
        self.__keys[index] = key
        self.__values[index] = value

    def add(self, key: str, value: any):
        return self.__setitem__(key, value)

    def get(self, key: str):
        index = self.__keys.index(key)
        value = self.__values[index]
        return value

    def __calculate_index(self, key):
        index = sum(ord(x) for x in key) % HashTable.min_length
        return index

    def __find_available_index(self, index):
        if index == len(self.__keys):
            index = 0
        if self.__keys[index] is None:
            return index
        return self.__find_available_index(index + 1)

    def size(self):
        return len([x for x in self.__keys if x is not None])

    def resize(self):
        self.__keys.extend([None] * len(self.__keys))
        self.__values.extend([None] * len(self.__values))

    def __len__(self):
        return len([x for x in self.__keys if x is not None]) + len([x for x in self.__values if x is not None])

    def __str__(self):
        key_value_pairs = [f"{self.__keys[idx]}: {self.__values[idx]}" for idx in
                           range(len(self.__keys)) if self.__keys[idx] is not None]
        return "{" + ", ".join(key_value_pairs) + "}"


table = HashTable()

table["name"] = "Peter"
table["age"] = 25

print(table)
print(table.get("name"))
print(table["age"])
print(len(table))
