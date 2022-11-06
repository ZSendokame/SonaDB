# KDB
*KDB* is a small library for Key-Value databases.<br>
It can load binary files as Dictionaries, consumes little space on disk.

# Install
```
pip install git+https://github.com/ZSendokame/KDB.git
```

# Use
```py
import kdb

db = kdb.Database(open('database.db', 'rb'))

# Keys:
db.set('key', 'value')  # Create a new key, None.
db.get('key')  # Get a key, Any.
db.remove('key')  # Remove a key, None.
db.exists('key')  # Check if a key exists, Bool.
db.rename('key', 'new_name')  # Rename a key, None.
```