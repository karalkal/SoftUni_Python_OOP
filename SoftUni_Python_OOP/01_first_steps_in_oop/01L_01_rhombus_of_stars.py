number = int(input())

for n1 in range(number):
    spaces = number - n1 + 1
    row = spaces * " " + n1 * "* "
    print(row)

for n2 in range(number, -1, -1):
    spaces = number - n2 + 1
    row = spaces * " " + n2 * "* "
    print(row)