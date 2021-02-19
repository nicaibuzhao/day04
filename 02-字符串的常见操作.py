

# 练习1: 定义一个字符串类型的变量，利用find方法获取指定数据对应的下标
str = "hello world"
print(str.find("o"))

# 练习2: 定义一个字符串类型的变量，利用index方法获取指定数据对应的下标
print(str.index("o"))
# 练习3: 定义一个字符串类型的变量，利用count方法统计指定数据在字符串中出现的次数
print(str.count("l"))
# 练习4: 定义一个字符串类型的变量，利用replace方法根据指定数据对字符串中的内容进行替换
print(str.replace("l","a"))
# 练习5: 定义一个字符串类型的变量，比如: my_str = "苹果#香蕉#鸭梨",利用split方法对数据进行分割
my_str = "苹果#香蕉#鸭梨"
print(my_str.split("#"))
# 练习6: 使用join方法把列表中的每一个数据进行字符串的拼接操作，比如：my_list = ['a', 'b']
# 拼接后的字符串是 'a#b'
my_list = ['a', 'b']
print("#".join(my_list))








