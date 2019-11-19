def swap_case(s):
    str = ''
    for letter in s:
        if letter.islower():
            letter = letter.upper()
        else:
            letter = letter.lower()
        str += ''.join(letter)
    return str

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)