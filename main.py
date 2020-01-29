"""
CLI die hallo zegt
Versie 1.1.2
Usage:
    main.py
    main.py -h  |--help
    main.py -v | --version
Options:
    -h --help  Dit help scherm laten zien.
    -v --version  Versie laten zien.
"""

from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__, version='1.1.2')

name = input("Naam: ")
print("\n")
print("Dag " + name + "!")