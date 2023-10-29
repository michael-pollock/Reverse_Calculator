import re


class Equation_Solver:
    def __init__(self, equation):
        self.accepted_operations = ['^', '*', '/', '+', '-']
        self.equation = equation
        self.answer = None
        self.operations = []
        self.variables = []
        self.currVariable = 'a'

        parenthesisValidator(equation)
        # self.__parseEquation__()

    def __parseEquation__(self):
        # gets pos or negative num. check that num is preceeded by newline or math op, then possibly a -,
        # a number, then possibly a decimal and more num
        pattern = "(?:(?<=[\^\+\-\*\/(])|(?<=^))\-?\d+(?:[.]\d+)?"
        numbers = re.findall(pattern, self.equation)
        operations = re.split(pattern, self.equation)
        operations.pop(-1)
        operations.pop(0)
        print(numbers)
        print(operations)


def add(numA, numB):
    numA = numCast(numA)
    numB = numCast(numB)
    return numA + numB


def subtract(numA, numB):
    numA = numCast(numA)
    numB = numCast(numB)
    return numA - numB


def multiply(numA, numB):
    numA = numCast(numA)
    numB = numCast(numB)
    return numA * numB


def divide(numA, numB):
    numA = numCast(numA)
    numB = numCast(numB)
    if (numB == 0):
        raise ValueError("Error: Cannot divide by 0 you fool.")
    return numA / numB


def power_aToB(numA, numB):
    numA = numCast(numA)
    numB = numCast(numB)
    return numA**numB


def root_aRootOfB(numA, numB):
    numA = numCast(numA)
    numB = numCast(numB)
    if (numA % 2 == 0):
        return [-1*(numB**(1/numA)), numB**(1/numA)]
    return [numB**(1/numA)]


def isNum(num):
    try:
        int(num)
        return True
    except ValueError:
        try:
            float(num)
            return True
        except ValueError:
            return False


def numCast(num):
    val = None
    if (type(num) != str):
        return num
    try:
        return int(num)
    except ValueError:
        try:
            return float(num)
        except ValueError:
            return 0


def parenthesisValidator(equation):
    if (equation.count('(') != equation.count(')')):
        return False
    eqLevels = ['']
    currLevel = 0
    prevLevel = 0
    maxLevel = 0
    write = False
    for char in equation:
        if (char == '('):
            maxLevel += 1
            eqLevels[currLevel] += '{'+str(maxLevel)+'}'
            prevLevel = currLevel
            currLevel = maxLevel
            eqLevels.append('')
            continue
        if (char == ')'):
            currLevel = prevLevel
            prevLevel -= 1
            continue
        eqLevels[currLevel] += char
    pemdas = ['^', '*', '/', '+', '-']
    numRegex = "(?:(?<=[\^\+\-\*\/(])|(?<=^))\-?\d+(?:[.]\d+)?"
    answer = None
    index = len(eqLevels) - 1
    while (index >= 0):
        print("Solving level " + str(index) + ": " + eqLevels[index])
        for operator in pemdas:
            for subIndex in range(index, len(eqLevels)):
                eqLevels[index] = eqLevels[index].replace(
                    "{" + str(subIndex) + "}", eqLevels[subIndex])
            regex = numRegex + "\\" + operator + numRegex
            found = re.search(regex, eqLevels[index])
            while (found):
                answer = evaluateOp(operator, found.group())
                print(found.group() + " = " + str(answer))
                eqLevels[index] = eqLevels[index].replace(
                    found.group(), str(answer))
                found = re.search(regex, eqLevels[index])
        index -= 1
    # for level in range(len(eqLevels)-1, 0):
    print("Final answer: " + str(answer))
    return eqLevels


def evaluateOp(operator, equation):
    nums = equation.split(operator)
    if (operator == '^'):
        return power_aToB(nums[0], nums[1])
    if (operator == '*'):
        return multiply(nums[0], nums[1])
    if (operator == '/'):
        return divide(nums[0], nums[1])
    if (operator == '+'):
        return add(nums[0], nums[1])
    if (operator == '-'):
        return subtract(nums[0], nums[1])
    raise ValueError("Unknown operator: " + operator)
