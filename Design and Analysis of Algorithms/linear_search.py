def linear_search(num, arr):
    if len(arr) > 0:
        for i in range(len(arr)):
            if i == num:
                return arr.index(i)
    else:
        print("List is empty!")


print(linear_search(4, [1, 3, 4, 6, 57]))