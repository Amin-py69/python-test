import random

hads = random.randint(1, 99)
print(hads)
javab = input('your javab ')

x = hads

while javab != 'd':
    if javab == 'b':
        hads = random.randint(x, 99)
        print(hads)
        javab = input('your javab ')

    elif javab == 'k':
        hads = random.randint(1, x)
        print(hads)
        javab = input('your javab ')

print('you win')

