#!/usr/bin/python3
"""script fetchs webpage"""

import sys
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers['X-Request-Id'])
