from datetime import datetime
import sys


def kata02():
    t = (3, 30, 2019, 9, 25)
    print(
        '{:%m/%d/%Y %H:%M}'.format(datetime(t[2], t[3], t[4], t[0], t[1])))


if __name__ == '__main__':
    kata02()
    sys.exit()
