#!/usr/bin/python3
output = ""
for digit1 in range(10):
    for digit2 in range(digit1 + 1, 10):
        if digit2 < 9:
            output += "{}{},".format(digit1, digit2)
        else:
            output += "{}{}".format(digit1, digit2)
print(output.rstrip(","))
