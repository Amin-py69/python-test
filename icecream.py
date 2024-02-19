
def ice_cream(degree:int)->str:

    if 100 < degree:
        print('Steam')
    elif 0 > degree:
        print('Ice')
    else:
        print('Water')


degree = int(input())
result = ice_cream(degree)

