def binary_search(num, lst):
    beg = 0
    end = len(lst) - 1
    while beg < end:
        mid = (end + beg) // 2
        pos = -1
        if num == lst[mid]:
            pos = mid
            print("found!")
            return pos
        elif lst[mid] > num:
            end = mid - 1
            print("left")
            print("end : ", end)
        elif lst[mid] < num:
            beg = mid + 1
            print("right")
            print("right : ", beg)


print(binary_search(43, [3, 4, 5, 7, 9, 32, 43, 56, 65]))
