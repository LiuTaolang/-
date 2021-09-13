### 递归
函数自己调用自己，最后查出结果。

伪代码如下：
```
def look_for_key(box):
	for item in box:
		if item.is_a_box():
			look_for_key(item)
		elif item.is_a_key():
			print("found the key!")
```

递归只是让解决方案更清晰，并没有性能上的优势。实际上，有些情况下使用循环的性能更好。 Leigh Caldwell 在 Stack Overflow 上说的一句：“如果使用循环，程序的性能可能更高；如果使用递归，程序可能更容易理解。如何选择要看什么对你来说更重要。”