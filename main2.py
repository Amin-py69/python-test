def subway(li1: list, li2: list) -> int:
    result = 0
    for i in range(len(li1)):
        if li1[i] == 1 and li2[i]:
            result += 1
    return result


li1 = input().split()   # split can convert string to list
li1 = [int(seat) for seat in li1]

li2 = input().split()
li2 = [int(seat) for seat in li2]

results = subway(li1, li2)
print(results)

