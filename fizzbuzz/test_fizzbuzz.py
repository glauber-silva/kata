"""
Regras do FizzBuzz
1. Se a posição for multipla de 3: Fizz
2. Se a posição for multipla de 5: Buzz
3. Se a posição for multipla de 3 e 5: FizzBuzz
4. Para qualquer outra posição fale o próprio nº
"""
from unittest import TestCase
import fizzbuzz

def assert_true(expr, line):
    try:
        assert expr
    except AssertionError:
        print(expr)

class TestFizzBuzz(TestCase):
    
    def test_fizzbuzz(self):

        self.assertEqual(fizzbuzz.robot(1) == '1')

        assert(robot(1) == '1')
        assert(robot(2) == '2')
        assert(robot(4) == '4')

        assert(robot(3) == 'fizz')
        assert(robot(6) == 'fizz')
        assert(robot(9) == 'fizz')

        assert(robot(5)  == 'buzz')
        assert(robot(10) == 'buzz')
        assert(robot(20) == 'buzz')

        assert(robot(15) == 'fizzbuzz')
        assert(robot(30) == 'fizzbuzz')
        assert(robot(45) == 'fizzbuzz')