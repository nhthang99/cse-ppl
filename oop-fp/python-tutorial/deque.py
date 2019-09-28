from collections import deque

n = int(input())
d = deque()
for line_commands in range(n):
    command, *numbers = input().split()
    if numbers :
        numbers = list(map(int, numbers))
    print(type(numbers))
    getattr(d, command)(*numbers)
print(' '.join(map(str, d)))