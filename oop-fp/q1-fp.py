def double_a(lst):
    return [ele * 2 for ele in lst]

def double_b(lst):
    if len:
        return [lst[0]*2] + double_b(lst[1:])
    else:
        return []

def double_c(lst):
    return list(map(lambda x: x * 2, lst))

if __name__ == "__main__":
    print(double_a([2,3,-4]))
    print(double_b([2,3,-4]))
    print(double_c([2,3,-4]))