lim = 5
lo = 0
point = 1
flg = True

while True:
    if flg:
        print("*")
        low = low + 1
        flg = False
    elif not flg:
        print(point)
        point = point + 1
        low = low + 1
        flg = True
    if low == lim:
        print("\n")
    if point == 12:
        print("*")
        break
