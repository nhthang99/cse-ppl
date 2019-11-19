from functools import reduce

def compose(*args):
    def inner(arg):
        for f in reversed(args):
            arg = f(arg)
        return arg
    return inner

def compose_a(*args):
    cps = compose_a(*args[:-1]) if len(args) > 2 else args[-2]
    return lambda num: cps(args[-1](num))


def compose_b(*args):
    def h(arg):
        return reduce(lambda x, y: y(x), reversed(args), arg)
    return h

def square(num):
    return num * num

def increase(num):
    return num + 1

def double(num):
    return num * 2

if __name__ == "__main__":
    cps = compose(double, increase, square)
    a = compose_a(double, increase, square)
    b = compose_b(double, increase, square)
    print(cps(5))
    print(a(5))
    print(b(5))
