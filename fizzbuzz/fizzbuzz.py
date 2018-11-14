from functools import partial
multiple_of = lambda base, num: num % base == 0
multiple_of_5 = partial(multiple_of, 5)
multiple_of_3 = partial(multiple_of, 3)

def robot(pos):
    say = str(pos)
    if multiple_of(3, pos) and multiple_of(5, pos):
        say = 'fizzbuzz'
    elif multiple_of(5, pos):
        say = 'buzz'
    elif multiple_of(3, pos):
        say = 'fizz'

    return say

def main():
    typed = 0
    while typed != -1:
        typed = int(input("input: "))
        print(robot(typed))


if __name__ == '__main__':
    main()