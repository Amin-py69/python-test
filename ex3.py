

n = int(input())

table = []
for row in range(1, 2*n):
    row_str = ""
    for col in range(1, 2*n):
        if col == n or row + col == 2*n:
            row_str += "D"
        else:
            row_str += "."
    table.append(row_str)

for row in table:
    print(row)