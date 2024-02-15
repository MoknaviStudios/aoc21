file = open("input.txt", "r")

i = 0
counter = 0
values = file.readlines()
values = [int(i) for i in values]

while i <= len(values) - 4:
    if values[i] + values[i + 1] + values[i + 2] < values[i + 1] + values[i + 2] + values[i + 3]:
        counter += 1
    i += 1

file.close()
print(counter)