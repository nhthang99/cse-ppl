if __name__ == '__main__':
    s = input()
    alpha, alnum, digit, lower, upper = False, False, False, False, False
    for l in s:
        if l.isalpha():
            alpha = True
        if l.isalnum():
            alnum = True
        if l.isdigit():
            digit = True
        if l.islower():
            lower = True
        if l.isupper():
            upper = True
    print(alpha)
    print(alnum)
    print(digit)
    print(lower)
    print(upper)