import sys


def kata03():
    s = 'The right format'
    s = '{:->42}'.format(s)
    print(s, end="")


if __name__ == '__main__':
    kata03()
    sys.exit()
