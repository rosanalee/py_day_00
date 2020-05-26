import sys
from sys import argv


def thejob():
    args = []
    i = 0
    input_len = len(argv)
    if len(argv) == 1:
        return
    while i < input_len:
        if i == 0:
            i += 1
            continue
        args.append(argv[i])
        i += 1
    s = ''
    if len(args) == 1:
        final = args[0][::-1]
        print(final.swapcase())
    else:
        s = ' '.join(args)
        s = s[::-1]
        s = s.swapcase()
        print(s)


if __name__ == '__main__':
    thejob()
    sys.exit()
