import itertools
from typing import List



class Module:
    N = 1

    def __init__(self, f, p):
        self.order = Module.N
        Module.N += 1
        self.f = int(f)
        self.p = int(p)
        self.on = False

    def __repr__(self):
        str_p = f'P->M{self.p}' if self.p else ''
        return f'[M{self.order} F={self.f:03} {str_p} on={self.on}]'

    @staticmethod
    def reset():
        Module.N = 1

    def off(self):
        self.on = False

def main():
    t = int(input())

    for n in range(1, t + 1):
        print(f'Case #{n}:', end=' ')

        n_modules = int(input())
        fun_factors = [int(x) for x in input().split(' ')]
        pointing = [int(x) for x in input().split(' ')]
        modules = [Module(f, p) for f, p in zip(fun_factors, pointing)]

        #print('Modules', *modules, sep='\n\t')
        get_max_fun(modules)
        Module.reset()


def get_max_fun(modules):
    pointing_dest = set([m.p for m in modules])
    initiators = [m for m in modules if m.order not in pointing_dest]
    #print('Initiators', *(i.order for i in initiators))

    max_fun = 0
    for perm in itertools.permutations(initiators):

        #fun_session = 0
        #for switch in perm:
        #    f_sw = trigger(switch, modules)
        #    print(f' Fun: {f_sw}')
        #    fun_session += f_sw
        fun_session = sum(trigger(switch, modules) for switch in perm)
        #print('\nThis session:', fun_session)
        if fun_session >= max_fun:
            max_fun = fun_session

        for m in modules:
            m.off()

    print(max_fun)


def trigger(m, modules):
    if not m:
        return 0

    if isinstance(m, int):
        m = modules[m-1]

    #print(f' Triggering {m}', end='')

    if m.on:
        return 0

    m.on = True
    return max(m.f, trigger(m.p, modules))


if __name__ == '__main__':
    main()
