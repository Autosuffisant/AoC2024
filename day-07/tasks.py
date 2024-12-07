equations = []
with open("./input.txt") as f:
    for line in f:
        result, operand = line.split(":")
        operand = operand.strip().split(" ")

        equations.append((result, operand))

def evaluate(result, operands, operators):
    if len(operands) == 1:
      if operands[0] == result:
        return result
      else:
        return None

    for operator in operators:
        copyOperands = operands.copy()
        computed = operator(copyOperands[0], copyOperands[1])

        copyOperands.pop(0)
        copyOperands.pop(0)
        copyOperands.insert(0, computed)

        if evaluate(result, copyOperands, operators) == result:
            return result

    return None

task1 = 0
operatorsTask1 = {
    lambda x, y: x * y,
    lambda x, y: x + y,
}

for equation in equations:
    result, operands = equation
    result = int(result)
    operands = [int(operand) for operand in operands]

    if evaluate(result, operands, operatorsTask1) == result:
        task1 += result

print(task1)

task2 = 0
operatorsTask2 = {
    lambda x, y: x * y,
    lambda x, y: x + y,
    lambda x, y: int(str(x) + str(y))
}

for equation in equations:
    result, operands = equation
    result = int(result)
    operands = [int(operand) for operand in operands]

    if evaluate(result, operands, operatorsTask2) == result:
        task2 += result

print(task2)