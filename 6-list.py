# 列表里可以存放不同类型的值
fruit = ['apple', 'banana', 'orange', 1, True, None]
# 香蕉-banana
print(fruit)
print(len(fruit))
print(fruit[0])
print(fruit[len(fruit) - 1])
print(fruit[-2])
print(fruit[-3])
print('--------------------\n')

# title()不能对list类型使用
# fruit=fruit.title()
# print(fruit)
print(type(fruit))
print(type(fruit[0]))
print('--------------------\n')

# -1返回倒1，-2返回倒2，以此类推，不知道列表长度下使用
print(fruit[-1])
print(fruit[-3])
print('--------------------\n')

# 3-1
names = ['harry', 'ron', 'hermione']
print(names[0].title())
print(names[1].title())
print(names[-1].title())
print('--------------------\n')

# 3-2
print(f'Good morning, {names[0].title()}.')
print(f'Good morning, {names[1].title()}.')
print(f'Good morning, {names[2].title()}.')
print('--------------------\n')

# 3-3
vehicles = ['motorcycle', 'suv', 'bicycle']
print(f'I would like to own a YAMAHA {vehicles[0]}.')
print(f'I would like to own a Lincoln {vehicles[1]}.')
print(f'I would like to own a RAW {vehicles[2]}.')
print('--------------------\n')

# 列表是动态可修改的，直接给索引赋值。
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
print('--------------------\n')

# 使用append()函数将元素添加到列表末尾，对空列表同样有效。
motorcycles.append('honda')
print(motorcycles)

veg = []
print(veg)
veg.append('potato')
veg.append('tomato')
print(veg)
print('--------------------\n')

# 使用insert()函数将元素插入指定位置，原位置及之后位置的元素都右移一个位置
# 用insert()函数把元素放到-1索引，不会使该元素处在列表最后一个位置，会把原-1元素后移，如果要放到最后直接使用append()函数
veg.insert(0, 'onion')
print(veg)
print(len(veg))
print(veg[-1])
veg.insert(-1, 'cucumber')
print(veg)
print('--------------------\n')

# del，pop()，remove()
print(veg)
# del删除元素，再不可访问该值。
del veg[0]
print(veg)
# pop()可以把弹出的值赋给变量。
poped_veg = veg.pop()
print(veg)
print(poped_veg)
# pop()可指定索引
veg.pop(-1)
print(veg)
# remove()指定值删除，且只能删除第一个符合条件的值，而且会改变列表长度。
veg.append('potato')
print(veg)
veg.remove('potato')
print(veg)
print('--------------------\n')

# 3-4
guestlist = ['harry', 'ron', 'hermione']
print(f'would u like to dinner with me, {guestlist[len(guestlist) - 1]}?')
print(f'would u like to dinner with me, {guestlist[len(guestlist) - 2]}?')
print(f'would u like to dinner with me, {guestlist[len(guestlist) - 3]}?')
print('--------------------\n')

# 3-5
print(f'{guestlist[len(guestlist) - 3]} can\'t come.')
guestlist.remove('harry')
# print(len(guestlist))
# guestlist.insert(len(guestlist)-3,'albus')
guestlist.append('albus')
print(f'would u like to dinner with me, {guestlist[len(guestlist) - 1]}?')
print(f'would u like to dinner with me, {guestlist[len(guestlist) - 2]}?')
print(f'would u like to dinner with me, {guestlist[len(guestlist) - 3]}?')
print('--------------------\n')

# 3-6
print('I find a bigger table, come along u three.')
guestlist.insert(0, 'hager')
guestlist.insert(2, 'nagini')
guestlist.append('navi')
print(f'would u like to dinner with me, {guestlist[0]}?')
print(f'would u like to dinner with me, {guestlist[1]}?')
print(f'would u like to dinner with me, {guestlist[2]}?')
print(f'would u like to dinner with me, {guestlist[3]}?')
print(f'would u like to dinner with me, {guestlist[4]}?')
print(f'would u like to dinner with me, {guestlist[5]}?')
print('--------------------\n')

# 3-7
print('sry, sth wrong, only two can come')
poped_guestlist = guestlist.pop()
print(f'sry {poped_guestlist}, dinner next time.')
poped_guestlist = guestlist.pop()
print(f'sry {poped_guestlist}, dinner next time.')
poped_guestlist = guestlist.pop()
print(f'sry {poped_guestlist}, dinner next time.')
poped_guestlist = guestlist.pop()
print(f'sry {poped_guestlist}, dinner next time.')
print(f'don\'t worry {guestlist[0]}, u can still come.')
print(f'don\'t worry {guestlist[1]}, u can still come.')
print(guestlist)
del guestlist[1]
del guestlist[0]
# del guestlist[1]，用del删除列表元素时索引会立即变化，倒着删就不会发生索引错误。
print(guestlist)
print('--------------------\n')
