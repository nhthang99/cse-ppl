from functools import reduce

def flatten_a(lst):
    # r = list()
    # for ele in lst:
    #     r = r + ele
    # return r
    return [x for y in lst for x in y]

def flatten_b(lst):
    if lst:
        return lst[0] + flatten_b(lst[1:])
    else:
        return []

def flatten_c(lst):
    return list(reduce(lambda x, y: x + y, lst))

if __name__ == "__main__":
    print(flatten_a([[1,2,3],['a','b','c'],[1.1,2.1,3.1]]))
    print(flatten_b([[1,2,3],['a','b','c'],[1.1,2.1,3.1]]))
    print(flatten_c([[1,2,3],['a','b','c'],[1.1,2.1,3.1]])) 