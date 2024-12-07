safeReports = 0

with open('./input.txt') as f:
    for line in f:
      unsafe = False
      line = line.strip().split(' ')

      increment = int(line[0]) - int(line[1]) < 0

      for i in range(len(line) - 1):
          first = int(line[i])
          second = int(line[i + 1])

          diff = first - second
          if increment and diff > -1 or diff < -3:
              unsafe = True
              break
          elif not increment and (diff < 1 or diff > 3):
              unsafe = True
              break

      if not unsafe:
          safeReports += 1


print(safeReports)

