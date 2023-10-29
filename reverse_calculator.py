import math
import random
import string

# could come in handy: https://www.tutorialspoint.com/how-do-i-use-strings-to-call-functions-methods-in-python#:~:text=Python%20Functions%20are%20generally%20called,locals()%20and%20globals().


class Equation_Generator:
    def __init__(self, answer, numRange, opList):
        # symbols to support eventually
        # +, -, x or *, /, !, ? (random), <, >, v
        self.acceptedSymbols = ['x', '*', '/', '+', '-']
        self.operationList = []
        self.__parseOpList(opList)
        self.equationVars = {}
        self.equationString = ""
        self.__generateEquationVarsAndString()
        self.appliedSymbols = set()
        self.answerIsFloat = type(answer) == float
        self.finalAnswer = answer
        self.step = self.__calculateStep()
        self.numMin = 0  # math.pow(10, numRange)*(-1)
        self.numMax = int(math.pow(10, numRange))
        self.numOperations = len(self.operationList)
        self.currOpNum = 0
        self.equation = []
        self.finalOp = self.currOpNum == self.numOperations
        self.__initFirstNum()

    def __calculateStep(self):
        # get smallest factor of final answer if one exists, otherwise, use final answer as the step.
        for i in range(2, self.finalAnswer):
            if (self.finalAnswer % i == 0):
                return i
        return self.finalAnswer

    def __parseOpList(self, opList):
        for op in opList:
            if (not op in self.acceptedSymbols):
                opList.remove(op)
                print("Sorry, no functionality yet for " + str(op))

        for op in opList:
            self.operationList.append(op)

    def __generateEquationVarsAndString(self):
        print("Generating equation vars and string")
        cache = {}
        vars = string.ascii_uppercase
        currVar = 'A'
        # ['x', '*', '/', '+', '-'] in pemdas order
        for i in range(0, len(self.acceptedSymbols)):
            for j in range(0, len(self.operationList)):
                if (self.acceptedSymbols[i] == self.operationList[j]):
                    op = []
                    if (str(j-1) in cache.keys()):
                        op.append(cache[str(j-1)])
                    else:
                        op.append(currVar)
                        # Find index of character in letters and Increment index and retrieve next character from letters
                        currVar = vars[vars.index(currVar) + 1]
                    op.append(self.operationList[j])
                    if (str(j+1) in cache.keys()):
                        op.append(cache[str(j+1)])
                    else:
                        op.append(currVar)
                        # Find index of character in letters and Increment index and retrieve next character from letters
                        currVar = vars[vars.index(currVar) + 1]
                    print(op)
                    cache[str(j)] = op
        print("printing cache: ")
        for key in cache:
            print("key: " + str(key))
            for i in cache[key]:
                print(i)

    def __incOpNum(self):
        self.currOpNum += 1
        self.finalOp = self.currOpNum == self.numOperations

    def __initFirstNum(self):
        if (self.finalOp):
            self.currAnswer = self.finalAnswer
            self.equation.append(self.currAnswer)
            return
        self.currAnswer = random.randrange(self.numMin, self.numMax, self.step)
        self.equation.append(self.currAnswer)

    def __insertAddition(self):
        self.__incOpNum()
        self.equation.append('+')
        self.appliedSymbols.add('+')
        if (self.finalOp):
            numToAdd = self.finalAnswer - self.currAnswer
        else:
            numToAdd = random.randrange(self.numMin, self.numMax, self.step)
            # add a number such that currAnswer + numToAdd is a factor of the step (helps multiplication and division be better numbers)
            if (self.currAnswer + numToAdd >= self.step):
                numToAdd -= (self.currAnswer + numToAdd) % self.step
            else:
                numToAdd += self.step % (self.currAnswer + numToAdd)

        self.equation.append(numToAdd)
        self.currAnswer += numToAdd

    def __insertSubtraction(self):
        self.__incOpNum()
        self.equation.append('-')
        self.appliedSymbols.add('-')

        if (self.finalOp):
            numToSubtract = self.currAnswer - self.finalAnswer
        else:
            numToSubtract = random.randrange(
                self.numMin, self.numMax, self.step)
            if (self.currAnswer - numToSubtract >= self.step):
                numToSubtract -= (self.currAnswer - numToSubtract) % self.step
            else:
                numToSubtract += self.step % (self.currAnswer - numToSubtract)

        self.equation.append(numToSubtract)
        self.currAnswer -= numToSubtract

    def __insertMultiplication(self):
        self.__incOpNum()
        # wrap equation in parenthesis
        self.equation.insert(0, '(')
        self.equation.append(')')
        self.equation.append('*')
        self.appliedSymbols.add('*')

        if (self.finalOp):
            # if (not self.answerIsFloat):
            #     if (self.finalAnswer % self.currAnswer == 0):
            #         numToDivide = self.finalAnswer / self.currAnswer
            #     else:
            #         if '+' in self.appliedSymbols:
            #             index = len(self.equation) - 2 # backtrack to insert after last num in parenthesis, behind ')*'
            # else:
            if (self.currAnswer == 0):
                self.equation.append('0')
                self.equation.append('+')
                self.equation.append(self.finalAnswer)
                self.currAnswer = self.finalAnswer
                return
            else:
                numToMultiply = self.finalAnswer / self.currAnswer

        else:
            numToMultiply = random.randrange(
                self.numMin, self.numMax, self.step)

        self.equation.append(numToMultiply)
        self.currAnswer *= numToMultiply

    def __insertDivision(self):
        self.__incOpNum()
        # wrap equation in parenthesis
        self.equation.insert(0, '(')
        self.equation.append(')')
        self.equation.append('/')
        self.appliedSymbols.add('/')

        if (self.finalOp):
            # if (not self.answerIsFloat):
            #     if (self.finalAnswer % self.currAnswer == 0):
            #         numToDivide = self.finalAnswer / self.currAnswer
            #     else:
            #         if '+' in self.appliedSymbols:
            #             index = len(self.equation) - 2 # backtrack to insert after last num in parenthesis, behind ')*'
            # else:
            if (self.finalAnswer == 0):
                self.equation.append('1')
                self.equation.append('-')
                self.equation.append(self.currAnswer)
                self.currAnswer = self.finalAnswer
                return
            else:
                numToDivide = self.currAnswer / self.finalAnswer

        else:
            numToDivide = random.randrange(self.numMin, self.numMax, self.step)

        self.equation.append(numToDivide)
        self.currAnswer /= numToDivide

    def operationHandler(self, operator):
        if (operator == '+'):
            self.__insertAddition()
        if (operator == '-'):
            self.__insertSubtraction()
        if (operator == '*' or operator == 'x'):
            self.__insertMultiplication()
        if (operator == '/'):
            self.__insertDivision()

    def getEquation(self):
        for op in self.operationList:
            self.operationHandler(op)
        self.equation.insert(0, '=')
        self.equation.insert(0, self.finalAnswer)
        self.printEquation()
        return self.equation

    def printEquation(self):
        equation = ""
        for char in self.equation:
            equation += str(char)
        print(equation)


def getNumFromUser(prompt, numIsFloat=False):
    valid = False
    val = -1
    count = 0
    userInput = 0
    userInput = input(prompt)
    while (not valid and count < 3):
        count += 1
        try:
            val = float(userInput) if numIsFloat else int(userInput)
            valid = True
        except ValueError:
            errorMsg = "Please enter a float, ex: 3.14." if numIsFloat else "Please enter an integer, ex: 42"
            userInput = input(errorMsg + " " + prompt)
    return val

# MAIN


answer = getNumFromUser(
    "Enter the number you would like to be the final answer: ")

base10 = math.ceil(math.log10(abs(answer))) if answer != 0 else 0

print("Your number is within the range of -(10^" +
      str(base10) + ") to 10^" + str(base10) + ". The numbers used for calculations prior to the last calculation should be between 0 and " + str(int(math.pow(10, base10))) + ".")

operations = list(input(
    "Please enter the operations you would like to use in the calculation of your answer: ").replace(' ', ''))


equationObj = Equation_Generator(answer, base10, operations)
equationArr = equationObj.getEquation()
