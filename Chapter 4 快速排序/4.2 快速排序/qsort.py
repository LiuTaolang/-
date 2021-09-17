def qsort(arr):
    if len(arr)<2:
        return arr
    return qsort([x for x in arr[1:] if x<arr[0] ]) + [arr[0]] + qsort([y for y in arr[1:] if y>=arr[0]])

print(qsort([1,3,2,4]))