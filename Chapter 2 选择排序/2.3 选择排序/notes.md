### 选择排序
挑出列表中元素最大的，放入新的列表；然后重复此操作，直到新的列表完全有序。为了找出列表中最大的元素，需要遍历该列表，即操作 n 次；每挑一个元素都得执行一次遍历，那么需要操作 n × 1/2 × n，大 O表示法省略常数，即得 O(n<sup>2</sup>)

### 示例代码
```Python
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))
```

列表的pop() method，会改变列表变量；它可以接收~~元素~~ **序号**作为参数，当参数为空时，默认 pop 序号最大的元素；~~接收不存在的元素参数时，~~当序号参数超出范围时，报 IndexError: pop index out of range.