### 基线条件与递归条件
base case and recursive case

一个死循环案例：

```Python
def countdown(i):
	print(i)
	countdown(i-1)
```

* 递归条件指的是函数调用自己
* 基线条件则指的是函数不再调用自己，避免形成无限循环。

添加基线条件后的countdown：

```Python
def countdown(i):
	print(i)
	if i <= 1:	#基线条件
		return
	else:		#递归条件
		countdown(i-1)
```