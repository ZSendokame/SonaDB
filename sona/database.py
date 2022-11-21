import hashlib
import os
import pickle
from io import TextIOWrapper
from typing import Any


class Database(object):

    def __init__(self, database: TextIOWrapper):
        self.size = os.path.getsize(database.name)
        self.database = pickle.load(database) if self.size else {}
        self.path = database.name

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.dump()

    def __len__(self):
        return len(self.database)

    def set(self, key: str, value: Any, algo: str = None) -> None:
        if algo is not None and algo in hashlib.algorithms_available:
            hash_function = hashlib.__getattribute__(algo)
            value = hash_function(bytes(value, 'utf-8')).hexdigest()

        self.database[key] = value

    def get(self, key: str) -> Any:
        if key not in self.database:
            return None

        return self.database[key]

    def rename(self, key: str, name: str) -> None:
        if key in self.database:
            self.database[name] = self.database.pop(key)

    def remove(self, key: str) -> None:
        self.database.pop(key)

    def query(self, function: object) -> list:
        result = []

        for key, value in self.database.items():
            if function(key, value):
                result.append([key, value])

        return result

    def exists(self, key: str) -> bool:
        return key in self.database

    def dump(self) -> None:
        with open(self.path, 'wb') as file:
            pickle.dump(self.database, file)

    def population(self, key: str = None) -> int:
        if key is not None:
            return len(self.database[key])

        return len(self.database)

    def clear(self) -> None:
        self.database.clear()
