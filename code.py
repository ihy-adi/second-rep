lim = 5
low = 0
point = 1
flg = True

while True:
    if point == 13:
        print("*", end="")
        break
    if flg:
        print("*", end="")
        low = low + 1
        flg = False
        if low == lim:
            print("\n", end="")
            low = 0
    if not flg:
        print(point, end="")
        point = point + 1
        low = low + 1
        flg = True
        if low == lim:
           print("\n", end="")
           low = 0

#
