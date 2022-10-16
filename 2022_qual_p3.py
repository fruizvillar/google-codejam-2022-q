from typing import List


class Die:
    N = 1

    def __init__(self, n):
        self.order = Die.N
        Die.N += 1
        self.n = int(n)

    def __repr__(self):
        return f'D{self.n:02} ({self.order})'

    @staticmethod
    def reset():
        Die.N = 1


def main():
    t = int(input())

    for n in range(1, t + 1):
        print(f'Case #{n}:', end=' ')

        n_dice = int(input())
        dice_n_unsorted = [int(x) for x in input().split(' ')]
        dice = [Die(x) for x in sorted(dice_n_unsorted)]

        get_max_fast(dice)
        Die.reset()


def get_max_fast(dice):
    #print(dice)
    n = 1
    for i, die in enumerate(dice):
        if die.n >= n:
            #print(f'Die {die} was set to  {n}')

            n += 1

    print(n-1)


if __name__ == '__main__':
    main()
