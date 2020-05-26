import sys


def kata00():
    t = (19, 42, 21)
    t_len = len(t)
    phrase = f"The {t_len} numbers are: "
    i = 0
    for n in t:
        if i < 2:
            cond = True
        else:
            cond = False
        liaison = (' ', ', ')[cond]
        phrase += str(n) + liaison
        i += 1
    print(str(phrase))


if __name__ == '__main__':
    kata00()
    sys.exit()
