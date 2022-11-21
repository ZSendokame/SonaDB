import os

import arguing

from . import Database


def main():
    db_file = arguing.set('--database', mandatory=True, help='Database file.')

    if not os.path.exists(db_file):
        open(db_file, 'x').close()

    database = Database(open(db_file, 'wb'))

    while True:
        command = input('>>> ').lower()
        parsed = command.split()

        if not parsed:
            pass

        elif parsed[0] == 'exit':
            exit(0)

        elif parsed[0] in database.__dir__():
            try:
                output = database.__getattribute__(parsed[0])(*parsed[1:])

            except TypeError:
                output = database.__getattribute__(parsed[0])

            print(output)

        else:
            print('Unkown function/command.')


if __name__ == '__main__':
    main()
