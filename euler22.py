f = open("names.txt", "r")

name_input = f.read()

names_with_quotes = name_input.split(",")

names = sorted([x.strip('"') for x in names_with_quotes])

total = 0

for i, name in enumerate(names):
    total += (i + 1) * sum([ord(x) - 64 for x in name])


print total
