def swap(lst, pos1, pos2):
    lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
    return lst


def partition(lst, lb, ub):
    pivot = lst[0]
    start = lb
    end = ub

    while start < end:
        while lst[start] <= pivot:
            start = start + 1
            # print("start", start)
            break
        while lst[end] > pivot:
            end = end - 1
            # print("end", end)
            break
        if start < end:
            swap(lst, start, end)

        swap(lst, lst.index(pivot), end)
    return end

