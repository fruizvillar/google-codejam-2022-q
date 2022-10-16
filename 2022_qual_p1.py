def main():
    t = int(input())

    for n in range(1, t + 1):
        r, c = [int(x) for x in input().split(' ')]

        print(f'Case #{n}:')
        print_punch(r, c)


def print_punch(r, c):
    print('..', end='')
    _print_sep_line(c - 1)
    print('..', end='')
    _print_dot_line(c - 1)

    for _ in range(r - 1):
        _print_sep_line(c)
        _print_dot_line(c)

    _print_sep_line(c)


def _print_sep_line(c):
    print('+-' * c + '+')


def _print_dot_line(c):
    print('|.' * c + '|')


if __name__ == '__main__':
    main()
