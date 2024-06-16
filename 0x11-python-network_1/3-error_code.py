#!/usr/bin/python3
"""script fetchs webpage"""

import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as er:
        print('Error code:', er.code)
