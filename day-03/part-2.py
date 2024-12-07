import re

with open('./input.txt') as f:
    data = f.read()

mulRegex = re.compile(r'mul\((\d+),(\d+)\)')
doRegex = re.compile(r'do\(\)')
dontRegex = re.compile(r"don't\(\)")

doIterator = doRegex.finditer(data)
dontIterator = dontRegex.finditer(data)

sum = 0
lastDo = None
lastDont = None
nextDo = next(doIterator)
nextDont = next(dontIterator)
do = True
for mulMatch in mulRegex.finditer(data):
    while nextDo and nextDo.start() < mulMatch.start() and nextDo.end() < mulMatch.end():
        lastDo = nextDo
        nextDo = next(doIterator, None)
    while nextDont and nextDont.start() < mulMatch.start() and nextDont.end() < mulMatch.end():
        lastDont = nextDont
        nextDont = next(dontIterator, None)

    if lastDo and lastDont:
        if lastDo.start() > lastDont.start():
            do = True
        else:
            do = False
    elif lastDo:
        do = True
    elif lastDont:
        do = False

    if do:
        sum += int(mulMatch.group(1)) * int(mulMatch.group(2))

print(sum)
