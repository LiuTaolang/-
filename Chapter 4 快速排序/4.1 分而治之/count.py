def count(arr):
    try:
        arr.pop()
        return 1+count(arr)
    except IndexError:
        return 0

print(count([1,2,3,4]))