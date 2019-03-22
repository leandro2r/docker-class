#!/usr/bin/env python3

import json
import os
import requests
import time
import sys


def main():
    HOST = os.environ.get('DB_HOST', '127.0.0.1')
    PORT = os.environ.get('DB_PORT', 9210)
    TRIES = os.environ.get('TRIES', 3)
    INDEX_NAME = os.environ.get('INDEX_NAME', 'docker-class')

    DB = 'http://{}:{}'.format(
        HOST,
        PORT,
    )

    data = {
        'user': 'Leandro Rodrigues',
        'email': 'leandro.l2r@gmail.com',
        'message': 'Good job!'
    }

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

    print('Sending a message... Please wait.')

    try:
        msg = requests.post(
            '{}/{}/typename/1'.format(DB, INDEX_NAME),
            headers={'content-type': 'application/json'},
            json=data,
        )
    except requests.exceptions.RequestException as error:
        print('\nFailed to connect: {}\n'.format(error))
        sys.exit(1)
    
    print('Congrats! Now you are a dockerzao da porra. Bye')

if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, SystemExit, OSError, RuntimeError):
        print(' Bye')
