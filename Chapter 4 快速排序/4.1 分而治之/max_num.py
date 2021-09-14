def bigger_num(a,b):
    if a>b:
        return a
    else:
        return b

def max_num(arr):
    if len(arr)==2:
        return bigger_num(arr[0],arr[1])
    else:
        return bigger_num(arr.pop(),max_num(arr))

print(max_num([1,2,3,4]))