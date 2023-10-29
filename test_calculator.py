import unittest
import calculator


class TestCalculator(unittest.TestCase):

    def test_isNum(self):
        numA = 42
        numB = '42'
        numC = 42.0
        numD = '42.0'
        numE = 'fourty two'
        validNums = [numA, numB, numC, numD]
        for num in validNums:
            self.assertTrue(calculator.isNum(num))
        self.assertFalse(calculator.isNum(numE))

    def test_numCast(self):
        numA = 42
        numB = '42'
        numC = 42.0
        numD = '-42.0'
        numE = 'fourty two'
        self.assertEqual(calculator.numCast(numA), 42)
        self.assertEqual(calculator.numCast(numB), 42)
        self.assertEqual(calculator.numCast(numC), 42.0)
        self.assertEqual(calculator.numCast(numD), -42.0)
        self.assertEqual(calculator.numCast(numE), 0)

    def test_add(self):
        self.assertEqual(calculator.add(1, 1), 2)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(0, 0), 0)
        self.assertEqual(calculator.add('1', '-1'), 0)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(1, 1), 0)
        self.assertEqual(calculator.subtract(-1, 1), -2)
        self.assertEqual(calculator.subtract(0, 0), 0)
        self.assertEqual(calculator.subtract('1', '-1'), 2)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(1, 1), 1)
        self.assertEqual(calculator.multiply(-1, 1), -1)
        self.assertEqual(calculator.multiply(0, 0), 0)
        self.assertEqual(calculator.multiply('10', '-10'), -100)

    def test_divide(self):
        self.assertEqual(calculator.divide(1, 1), 1)
        self.assertEqual(calculator.divide(-1, 1), -1)
        self.assertEqual(calculator.divide('3', '2'), 1.5)
        with self.assertRaises(Exception):
            calculator.divide(0, 0)

    def test_power_aToB(self):
        self.assertEqual(calculator.power_aToB(1, 2), 1)
        self.assertEqual(calculator.power_aToB(-1, 2), 1)
        self.assertEqual(calculator.power_aToB(0, 3), 0)
        self.assertEqual(calculator.power_aToB('-3', '3'), -27)

    def test_root_aRootOfB(self):
        self.assertEqual(calculator.root_aRootOfB(2, 4), [-2, 2])
        self.assertEqual(calculator.root_aRootOfB(3, 27), [3])
        self.assertEqual(calculator.root_aRootOfB(2, 100), [-10, 10])
        self.assertEqual(calculator.root_aRootOfB('4', '16'), [-2, 2])
