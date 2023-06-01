# bool, True和False
# NoneType, None---不是0，不是空字符串，不是False
obj = None
print(obj)

# type()返回变量类型
print(type(obj))
print(type(True))

# 获取字符串长度
mes = 'hello'
print(len(mes))
# 索引单个字符
print(mes[3])
print(mes[len(mes) - 1])
print(type(mes))

# bool
b1 = True
b2 = False
print(type(b1))
print(type(b2))

# None
n1 = None
print(type(n1))

# int float
print(type(1))
print(type(1.0))

# 不要试图写出完美漂亮的代码，先解决问题再说。
print('''>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!''')
