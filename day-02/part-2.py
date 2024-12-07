safeReports = 0

with open('./input.txt') as f:
    for line in f:
        unsafe = False
        line = line.strip().split(' ')
        errors = 0


        def isSafe(line):
            increment = int(line[0]) - int(line[1]) < 0

            for i in range(len(line) - 1):
                first = int(line[i])
                second = int(line[i + 1])

                diff = first - second
                if increment and diff > -1 or diff < -3:
                    return False
                elif not increment and (diff < 1 or diff > 3):
                    return False

            return True

        if (isSafe(line)):
            safeReports += 1
            continue

        for i in range(0, len(line)):
            poppedLine = line[:i] + line[i + 1:]
            if isSafe(poppedLine) == False:
                errors += 1

        if errors < len(line):
            safeReports += 1
