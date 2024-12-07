equations = []
with open("./input.txt") as f:
    for line in f:
        result, operand = line.split(":")
        operand = operand.strip().split(" ")

        equations.append((result, operand))

operators = {
    lambda x, y: x * y,
    lambda x, y: x + y,
}

def evaluate(result, operands):
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
        print(copyOperands)

        if evaluate(result, copyOperands) == result:
            return result

    return None

task1 = 0

for equation in equations:
    result, operands = equation
    result = int(result)
    operands = [int(operand) for operand in operands]

    if evaluate(result, operands) == result:
        task1 += result

print(task1)

