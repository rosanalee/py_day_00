import sys
from sys import argv


def operations(var1, var2, _usage):
    if var1.isdigit() is False or var2.isdigit() is False:
        print('InputError: only numbers\n')
        print(_usage)
        return
    var1 = int(var1)
    var2 = int(var2)
    sum = var1 + var2
    sub = var1 - var2
    prod = var1 * var2
    if var2 == 0:
        quot = 'ERROR (div by zero)'
        rem = 'ERROR (modulo by zero)'
    else:
        quot = var1 / var2
        rem = var1 % var2
    print(
        f"""Sum:            {sum}
Difference:     {sub}
Product:        {prod}
Quotient:       {quot}
Remainder:      {rem}"""
    )


if __name__ == '__main__':
    _usage = """Usage: python operations.py <number1> <number2>
Example:
    pythonoperations.py 10 3"""
    if len(argv) < 3:
        print(_usage)
        sys.exit()
    if len(argv) > 3:
        print("Input error: too many arguments\n")
        print(_usage)
        sys.exit()
    operations(argv[1], argv[2], _usage)
    sys.exit()
