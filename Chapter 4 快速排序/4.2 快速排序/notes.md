### 快速排序
对排序算法来说，最简单的数组是根本不需要排序的数组——空数组或者只有一个元素的数组。

```Python
def quicksort(array):
	if len(array) < 2:
		return array
```
此为基线条件。快速排序的原理：先从数组中选择一个元素，这个元素被称为基准值（pivot）。将剩余的元素与基准值作比较，原数组被拆成三个部分：小于基准值的数组，基准值，大于基准值的数组。对于两个子数组，利用递归继续分解直到满足基线条件。

```Python
def qsort(arr):
    if len(arr)<2:
        return arr
    return qsort([x for x in arr[1:] if x<arr[0] ]) + [arr[0]] + qsort([y for y in arr[1:] if y>=arr[0]])

print(qsort([1,3,2,4]))
```

课本中的代码：

```Python
def quicksort(array):
	if len(array) < 2:
		return array
	else:
		pivot = array[0]
		less = [i for i in array[1:] if i<=pivot]
		greater = [i for i in array[1:] if i> pivot]
		return quicksort(less) + [pivot] + quicksort(greater)
		
print(quicksort([10, 5, 2, 3]))
```