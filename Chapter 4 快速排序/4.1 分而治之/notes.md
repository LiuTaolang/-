### 分而治之（divide and conquer， D&C）
这是一种递归式问题解决方法。只能解决一种问题的算法毕竟用处有限，D&C提供了解决问题的思路。

### 欧几里得算法（辗转相除法）
欧几里得算法求取两个数 a 和 b的最大公约数，公式：

```gcd(a,b)=gcd(b,r), a>b, a÷b=q···r```

gcd()表示求取最大公约数，greatest common divisor。这个公式是说，a 和 b的最大公约数等于 a 和 r 的最大公约数，r 是求余数运算。数学上证明此公式，只需证明 (a,b)的公约数集完全等于 (b, r)的公约数集。那么在应用过程中，此公式是递归使用的，第一次出现余数为零的时候，此时的除数即为最初 a,b 的最大公约数。

### 证明：a,b的公约数集等于 b, r的公约数集
```
假设 a÷b=q···r
a=bq+r 
1,
假设 a,b 有公约数 d
a=dm, b=dn
以上所有代数显然是整数。
r=a-bq
r=dm-dn·q
r=d(m-n·q)
可见d整除r, r是d的倍数。那么任意的 a,b公约数都是r的约数。
2,
假设 b,r 有公约数 e
b=ex, r=ey
a=ex·q+ey
a=e(x·q+y)
显然以上各代数都是整数，那么e整除a, a是e的倍数。那么任意的 b,r的公约数都是 a的约数。

以上，综合1和2，得出a与b的公约数集等于 b与r的公约数集。
```

### 练习
4.1 请编写前述sum函数的代码。

```Python
def sum(arr):
    if len(arr)==0:
        return 0
    else:
        return arr.pop()+sum(arr)
'''
答案
def sum(list):
	if list == []:
		return 0
	return list[0] + sum(list[1:])
'''

print(sum([1,2,3,4]))
```


4.2 编写一个递归函数来计算列表包含的元素数。

```Python
def count(arr):
    try:
        arr.pop()
        return 1+count(arr)
    except IndexError:
        return 0
'''
答案
def count(list):
	if list == []:
		return 0
	return 1 + count(list[1:])
'''
print(count([1,2,3,4]))
```

4.3 找出列表中最大的数字。

```Python
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
        
'''
答案
def max(list):
	if len(list)==2:
		return list[0] if list[0]>list[1] else list[1]
	sub_max=max(list[1:])
	return list[0] if list[0]>sub_max else sub_max
'''

print(max_num([1,2,3,4]))
```

4.4 还记得第1章介绍的二分查找吗？它也是一种分而治之算法。你能找出二分查找算法的基线条件和递归条件吗？

基线条件：~~当前元素等于要查找的元素~~ 数组只包含一个元素。如果要查找的值与这个元素相同，就找到了！否则，就说明它不在数组中。

递归条件：~~当前元素大于要查找的元素，则 high = mid；当前元素小于要查找的元素，则 low = mid。~~ 你把数组分成两半，将其中一半丢弃，并对另一半执行二分查找。