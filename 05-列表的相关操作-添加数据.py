
# 练习1：定义一个列表，往列表中追加一个数据(李四)
my_list = ['张三','王五','赵六']
my_list.append("李四")

# 练习2：定义一个列表，在下标0的位置插入一个数据(王五)
my_list.insert(0,'王五')
# 练习3: 定义两个列表，把第二个列表中的数据扩展到第一个列表中，输出第一个列表数据
my_list1 = [1,2,3,4,5]
my_list.extend(my_list1)

print(my_list)


