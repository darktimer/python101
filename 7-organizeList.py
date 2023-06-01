# sort()方法，按字母表顺序排列元素，对列表操作是不可逆的，参数recverse=True表示反向排序。
cars = ['bmw', 'audi', 'toyota']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
print('-----------------------\n')

# sorted()函数，参数是列表名，不会改变原始顺序，也可以使用参数reverse=True
cars.sort(reverse=False)
print(cars)
print(sorted(cars, reverse=True))
print(cars)
print('-----------------------\n')

# reverse()方法，反转元素排列顺序，调用两次即可恢复倒原始排列顺序。
print(cars)
cars.reverse()
print(cars)
print('-----------------------\n')

# 3-8
wonderlandlist = ['berlin', 'peking', 'dc', 'tokyo', 'rome']
print('原排列')
print(wonderlandlist)
print('sorted(原排列)')
print(sorted(wonderlandlist))
print('原排列检验')
print(wonderlandlist)
print('sorted(原排列，反转)')
print(sorted(wonderlandlist, reverse=True))
print('原排列检验')
print(wonderlandlist)
print('原排列.reverse()')
wonderlandlist.reverse()
print(wonderlandlist)
print('新排列.reverse()')
wonderlandlist.reverse()
print(wonderlandlist)
print('原排列.sort()')
wonderlandlist.sort()
print(wonderlandlist)
print('新排列.sort(reverse=True)')
wonderlandlist.sort(reverse=True)
print(wonderlandlist)

# 3-9
print(f'there\'s {len(wonderlandlist)} wonderland.')
