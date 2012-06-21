total = 0

current = 2
prev = 1

while True:
    if current >= 4000000:
        break

    if current % 2 == 0:
        total += current

    new_current = current + prev

    prev = current
    current = new_current

print total
