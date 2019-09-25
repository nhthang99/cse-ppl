def lessThan_a(n, lst):
    return [ele for ele in lst if ele < n]
def lessThan_b(n, lst):
    if lst:
        return lessThan_b(n, lst[1:]) if lst[0] >=n else  [lst[0]] + lessThan_b(n, lst[1:])
    else:
        return []
def lessThan_c(n, lst):
    return list(filter(lambda ele: ele < n, lst))

if __name__ == "__main__":
    print(lessThan_a(50, [1,55,6,2]))
    print(lessThan_b(50, [1,55,6,2]))
    print(lessThan_c(50, [1,55,6,2]))