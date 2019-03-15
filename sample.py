#!/usr/bin/env python3

import json
import os
import requests
import time
import sys


def main():
    HOST = os.environ.get('DB_HOST', 'localhost')
    PORT = os.environ.get('DB_PORT', 9200)
    SLEEP = os.environ.get('SLEEP', 30)
    TRIES = os.environ.get('TRIES', 3)

    DB = 'http://{}:{}'.format(
        HOST,
        PORT,
    )

    msg = ''

    for i in range(int(TRIES)):
        print('{}. Connecting on {}...'.format(i, DB))

        try:
            msg = requests.get(DB, stream=True).json()
            break
        except requests.exceptions.RequestException as error:
            print('\nFailed to connect: {}\n'.format(error))
    
        time.sleep(5)
    
    if not msg:
        print('Max retries exceeded')
        sys.exit(1)

    print(
        '\tName: {}\n\tVersion: {}'.format(
            msg['name'],
            msg['version']['number'],
        )
    )

    print('Congrats! Now you are a dockerzao da porra. Wait...')

    time.sleep(float(SLEEP))

if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, SystemExit, OSError, RuntimeError):
        print(' Bye')
