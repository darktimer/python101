name = 'harry potter'
name_new1 = name.upper()
name_new2 = name.lower()
name_new3 = name.title()
print(name_new1)
print(name_new2)
print(name_new3)

# 在字符串前加 f ，在字符串中用 {变量名} 可以直接求值变量。
print(f'what are u doing here, Mr {name_new3}?')
first_name='harr'
last_name='pott'
full_name=f'{first_name} {last_name}'
print(full_name)
print(f'hello,{full_name.title()}!')

# 删除字符串末尾空白 .rstrip()
# 删除字符串开头空白 .lstrip()
# 删除字符串两边空白 .strip()
# 注意，这样的删除，只是对该字符串值做了修改，如果要永久保留修改，需要对变量重新赋值。
