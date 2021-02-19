# 练习1：定义一个列表，分别使用for循环和while循环对列表进行遍历
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
for i in my_list:
    print(i)

count = 0
while count < len(my_list):
    print(my_list[count])
    count += 1
