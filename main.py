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
DagName = "Dag " + name + "!\n"
if name == "Hans":
    print("\n")
    print("Hallo Hans!\n"*10)
else:
    print("\n")
    print(DagName*10)