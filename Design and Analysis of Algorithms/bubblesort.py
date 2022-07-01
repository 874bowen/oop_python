from swap import swap

""":param
have a list
check if first element is greater than the next
if true swap
"""


def bubblesort(lst, lb, ub):
    for j in range(len(lst)-1):
        print(j)
        for i in range(len(lst)-1-j):
            if lst[i] > lst[i+1]:
                print("Greater")
                print(swap(lst, i, i+1))


bubblesort([25, 3, 14, 6, 23], 0, 4)

