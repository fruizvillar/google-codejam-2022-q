PRINTERS = 3

COLOUR_AMOUNT = 1e6

N_COLOURS = 4
NO_STR = 'IMPOSSIBLE'

def main():
    t = int(input())

    for n in range(1, t + 1):
        print(f'Case #{n}:', end=' ')

        ink = [[int(x) for x in input().split(' ')] for _ in range(PRINTERS)]

        check_avail(ink)


def check_avail(ink):
    if any(sum(i) < COLOUR_AMOUNT for i in ink):
        print(NO_STR)
        return

    mins = [min([i[x] for i in ink]) for x in range(N_COLOURS)]
    if sum(mins) < COLOUR_AMOUNT:
        print(NO_STR)
        return

    c = []
    for x in range(N_COLOURS):
        c.append(int(min(mins[x], COLOUR_AMOUNT - sum(c))))

    print(*c)


if __name__ == '__main__':
    main()
