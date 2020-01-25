"""CLI die hallo zegt
Usage:
    hello.py
    hello.py <naam>
    hello.py -h|--help
    hello.py -v|--version
Options:
    <naam>  Optioneel naam argument.
    -h --help  Dit scherm laten zien.
    -v --version  Versie laten zien.
"""

from docopt import docopt

def say_hello(name):
    return("Dag {}!".format(name))

if __name__ == '__main__':
    arguments = docopt(__doc__, version='DEMO 1.0')
    if arguments['<naam>']:
        print(say_hello(arguments['<naam>']))

    if arguments['<naam>'] == 'Hans':
        print("Hallo Hans!")