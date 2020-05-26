import sys
from sys import argv


def whois():
    input_len = len(argv)
    if input_len < 2:
        return
    if input_len > 2 or argv[1].isdigit() is False:
        print('ERROR')
    else:
        result = "I'm "
        check_val = int(argv[1])
        if check_val == 0:
            idf = 'Zero.'
            result = f"{result}{idf}"
            print(result)
        else:
            if check_val % 2 == 0:
                idf = 'Even.'
                result = f"{result}{idf}"
                print(result)
            else:
                idf = 'Odd.'
                result = f"{result}{idf}"
                print(result)


if __name__ == '__main__':
    whois()
    sys.exit()
