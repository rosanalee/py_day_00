import sys


def kata04():
    t = (0, 4, 132.42222, 10000, 12345.67)
    print(
        'day_{:0>2}, ex_{:0>2} : {:05.2f}, {:.2e}, {:.2e}'.format(
            t[0], t[1], t[2], t[3], t[4])
    )


if __name__ == '__main__':
    kata04()
    sys.exit()
