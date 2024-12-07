with open('./input.txt') as f:
    data = f.read().split('\n\n')
    rules = data[0].splitlines()
    updates = data[1].splitlines()

rulesDict = {}
for rule in rules:
    pages = rule.split('|')
    key = pages[0]
    value = pages[1]

    if key not in rulesDict:
        rulesDict[key] = [value]
    else:
        rulesDict[key] += [value]

validUpdates = 0
for update in updates:
    isUpdateValid = True
    pages = update.split(',')

    for i in range(len(pages) - 1):
        if pages[i + 1] in rulesDict[pages[i]]:
            continue
        else:
            isUpdateValid = False
            break

    if isUpdateValid:
        validUpdates += int(pages[len(pages) // 2])

print(validUpdates)

