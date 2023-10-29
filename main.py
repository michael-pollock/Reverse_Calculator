import calculator

equation = '(2*2)^2/(8+9)*2'
parenOpen = equation.count('(')
parenClose = equation.count(')')
if (parenOpen != parenClose):
    errorMsg = "Error: Mismatched number of parenthesis supplied."
    if (parenOpen > parenClose):
        errorMsg += " You are missing " + str(parenOpen -
                                              parenClose) + " ')'"
    else:
        errorMsg += " You are missing " + str(parenClose -
                                              parenOpen) + " '('"
    print(errorMsg)
print(equation)
equationObj = calculator.Equation_Solver(equation)
