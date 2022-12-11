import hashlib
import os
import pickle
from typing import Any


class Database:

    def __init__(self, database: str, type: type = dict):
        self.type = type()
        self.size = os.path.getsize(database)
        self.file = open(database, 'rb')
        self.database = pickle.load(self.file) if self.size else self.type
        self.path = database

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.close()
        self.dump()

    def __len__(self):
        return len(self.database)

    def set(self, key: str, value: Any, algo: str = None) -> None:
        if algo is not None and algo in hashlib.algorithms_available:
            hash_func = hashlib.__getattribute__(algo)
            value = hash_func(bytes(value, 'utf-8'), usedforsecurity=True)
            value = value.hexdigest()

        self.database[key] = value

    def get(self, key: str) -> Any:
        if key not in self.database:
            return None

        return self.database[key]

    def append(self, value: Any, key: str = None) -> None:
        if isinstance(self.type, list):
            self.database.append(value)

        elif self.exists(key):
            self.database[key].append(value)

    def rename(self, key: str, name: str) -> None:
        if key in self.database:
            self.database[name] = self.database.pop(key)

    def remove(self, key: str) -> None:
        self.database.pop(key)

    def query(self, function: object) -> list:
        result = []

        for key, value in self.database.items():
            if function(key, value):
                result.append((key, value))

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

    def close(self) -> None:
        self.file.close()
