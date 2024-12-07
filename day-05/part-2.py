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

def isUpdatesValid(pages, rulesDict):
    for i in range(len(pages) - 1):
        if pages[i + 1] in rulesDict[pages[i]]:
            continue
        else:
            return False

    return True

def reOrderInvalidUpdates(pages, rulesDict):
    for i in range(len(pages) - 1):
        if pages[i + 1] in rulesDict[pages[i]]:
            continue
        else:
            temp = pages[i]
            pages[i] = pages[i + 1]
            pages[i + 1] = temp

    return pages

correctedUpdatesSum = 0
for update in updates:
    pages = update.split(',')
    isUpdateValid = isUpdatesValid(pages, rulesDict)

    if not isUpdateValid:
        while not isUpdateValid:
            pages = reOrderInvalidUpdates(pages, rulesDict)
            isUpdateValid = isUpdatesValid(pages, rulesDict)

        correctedUpdatesSum += int(pages[len(pages) // 2])


print(correctedUpdatesSum)