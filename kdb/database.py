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

    def set(self, key: str, value: Any) -> None:
        self.database[key] = value

    def get(self, key: str) -> Any:
        return self.database[key]

    def rename(self, key: str, name: str) -> None:
        if key in self.database:
            self.database[name] = self.database.pop(key)

    def remove(self, key: str) -> None:
        self.database.pop(key)

    def query(self, func) -> list:
        result = []

        for key, value in self.database.items():
            if func(key, value):
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
