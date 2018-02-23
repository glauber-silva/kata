"""
Regras do FizzBuzz
1. Se a posição for multipla de 3: Fizz
2. Se a posição for multipla de 5: Buzz
3. Se a posição for multipla de 3 e 5: FizzBuzz
4. Para qualquer outra posição fale o próprio nº
"""
from functools import partial
multiple_of = lambda base, num: num % base == 0
multiple_of_5 = partial(multiple_of, 5)
multiple_of_3 = partial(multiple_of, 3




                        )
def robot(pos):
    say = str(pos)

    if multiple_of(3, pos) or multiple_of(5, pos):
        say = 'fizzbuzz'
    elif multiple_of(5, pos):
        say = 'buzz'
    elif multiple_of(3, pos):
        say = 'fizz'


    return say

def assert_true(expr, line):
    try:
        assert expr
    except AssertionError:
        print(expr)

if __name__ == '__main__':
    assert_true(robot(1) == '1')
    assert_true(robot(2) == '2')
    assert_true(robot(4) == '4')

    assert_true(robot(3) == 'fizz')
    assert_true(robot(6) == 'fizz')
    assert_true(robot(9) == 'fizz')

    assert_true(robot(5)  == 'buzz')
    assert_true(robot(10) == 'buzz')
    assert_true(robot(20) == 'buzz')

    assert_true(robot(15) == 'fizzbuzz')
    assert_true(robot(30) == 'fizzbuzz')
    assert_true(robot(45) == 'fizzbuzz')