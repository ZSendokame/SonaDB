# SonaDB
*Sona* ("Information" in *Toki Pona*) is a small library for Key-Value databases.<br>
It can load binary files as Dictionaries, consumes little space on disk.

# Install
```
# GIT+PIP
pip install git+https://github.com/ZSendokame/SonaDB.git

# PIP
pip install SonaDB
```

# Use
```py
import sonadb

db = sonadb.Database('database.db', type=dict)
# You can specify the type of the object that Pickle will save, by default is a dict.

# Keys:
db.set('key', 'value', algo='md5')  # Create a new key and hash if algorithm defined, None.
db.get('key')  # Get a key, Any.
db.remove('key')  # Remove a key, None.
db.exists('key')  # Check if a key exists, Bool.
db.rename('key', 'new_name')  # Rename a key, None.
db.append('value', 'key')  # Append a value to a key or the database, None.

# Database
db.population()  # Get the length of Database or Key, Int.
db.clear()  # Delete all the Database on memory.
db.dump()  # Saves all the memory to a file.
db.query(lambda key, value: expression)
# Iterate over the Database, giving key-value to the lambda and checking for True.
```