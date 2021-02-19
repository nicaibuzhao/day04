#-*- coding:utf-8 -*-
# @Author : mingyu.ding
# @PROJECT: day04
# @Time : 2021/2/19 17:05

'''
做一个简单的用户信息管理系统：
提示用户依次输入姓名，年龄和爱好
并且在输入完成之后，一次性将用户输入的数据展示出来
'''
# 录入数据，并保存在变量中
name = input("请输入姓名：")
age = input("请输入年龄：")
hobby = input("请输入您的爱好：")
# 格式化输出数据
print("您的姓名是%s, 您的年龄是%s， 您的爱好是%s" % (name, age, hobby))


'''
有一个列表，判断列表中的每一个元素是否以s或e结尾，如果是，则将其放入一个新的列表中，最后输出这个新的列表
list = ["red", "apples", "orange", "pink", "bananas", "blue", "black", "white"]
'''
list = ["red", "apples", "orange", "pink", "bananas", "blue", "black", "white"]
new_list = []
for i in list:
    if i.endswith("s") or i.endswith("e"):
        new_list.append(i)
print(new_list)




'''
给定一个列表，首先删除以s开头的元素，删除后，修改第一个元素为"joke"，并且并且把最后一个元素复制一份，放在joke的后边
list = ["spring", "look", "strange", "curious", "black", "hope"]
'''
list = ["spring", "look", "strange", "curious", "black", "hope"]
for i in list:
    if i.startswith("s"):
        list.remove(i)
# 修改第一个元素为"joke"
list[0] = "joke"

# 获取最后一个元素
last_one = list[-1]

# 将最后一个元素放在joke的后面
list.insert(1, last_one)
print(list)