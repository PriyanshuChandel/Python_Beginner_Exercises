# Faulty Calculator
# Design a calculator which will correctly solve all calculation except following one.
# 45*3 = 555, 56+9 = 77, 56/6 = 4
# take input as operator and two numbers from user and return the result

def calc(args):
    if args.x == 45 and args.y == 3 and args.o == 'mul':
        return 'Output is', 555
    elif args.x == 56 and args.y == 9 and args.o == 'add':
        return "Output is", 77
    elif args.x == 56 and args.y == 6 and args.o == 'div':
        return "Output is", 4
    elif args.x == int and args.y == int and args.o == 'sub':
        return "Output is", args.x - args.y

    elif args.o == 'mul':
        return args.x * args.y
    elif args.o == 'add':
        return args.x + args.y
    elif args.o == 'div':
        return args.x / args.y
    elif args.o == 'sub':
        return args.x - args.y
    else:
        return 'Something went wrong'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0,
                        help="Enter first number, this is a utility for calculations. " \
                             "Please contact admin for more info")
    parser.add_argument('--y', type=float, default=3.0,
                        help="Enter second number, this is a utility for calculations."
                             "Please contact admin for more info")
    parser.add_argument('--o', type=str, default='add',
                        help="Enter operator, i.e 'add', 'sub', 'mul', 'div', this is a utility for calculations."
                             "Please contact admin for more info")
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))
