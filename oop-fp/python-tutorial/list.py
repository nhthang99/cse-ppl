if __name__ == '__main__':
    N = int(input())
    lst = list()
    for i in range(N):
        cmd, *numbers = input().split()
        if numbers:
            numbers = list(map(int, numbers))
        if cmd != 'print':
            getattr(lst, cmd)(*numbers)
        else:
            print(lst)