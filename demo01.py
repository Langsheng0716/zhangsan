'''
print("hello world!") # 字符串
print(2333) # 整数
print(2.3333) # 小数
print(True) # 布尔
print(()) # 元祖
print([]) # 数组 
print({}) # 字典
锄禾日当午
汗滴禾下土
谁知盘中餐
粒粒皆辛苦
print("哈哈",2333,2.333)
print("哈哈"+"嘻嘻")
print("haha"*100)#一百遍
print(((100+2.89)-50)/2)
'''
'''a = float(input("请输入："))
b = float(input("请输入："))
print("输出的内容：",float(a+b))'''

'''a = input()
b = input()
print("输入的值：",a+b)'''

'''name = "张三"
print (name)'''

'''a = input () #只要是通过input输入的全是字符串，所以这里需要用到数据类型转换，type可以读取数据格式，例如type(2333) print(type(2333)) /// c = type(2333) print(c)
print("input获取的内容:",a)'''   #str int float bool tuple list dict

'''a = int(2333)
print(type(2333))# class int  、、任何数据都可以转换为字符串 整数和小数可以互相转换 字符串转换为其他类型的数据 ，必须满足 【长得像】这个规律 哈哈哈三个字不能转换成int 一也不能转换成1'''
#len 方法是计算长度 只支持字符串 元组数据字典
''' a = 'asf'
print(len(a))'''

'''随机输入两个内容
a = input("请输入：")
b = input("请输入：")
print("两个内容的长度之和是:",len(a)+len(b))
计算他们两个内容的长度之和'''


#元组

a = (1,2,3,4,"哈哈","嘻嘻",True,False)  
#print (a)
#print (a[-1])#最后一个false

#切片
'''print (a[0:4])#左闭右开
print(a[4:6])
print(a[6:])#或者6:8'''


#print(a.index("嘻嘻"))如果很多个相同的值的时候，搜的结果是第一个的下标
#print(a.count("嘻嘻"))用来统计某个值的数量
#这两个只能用一维的元组

#二维元组
'''b = (a)
b = (a,"嘻嘻","哈哈")#三个值
print(b[0][3])#套娃'''



#数组
a = [1,2,3,4,"哈哈","嘻嘻",True,False]
'''print (a[1])
a.append("append")#往数组中追加数据，放最后，比如下一行代码运行后看出效果
print(a)
a.insert(2,"insert")
print(a)'''

#b = a.pop(4)
#print (b)# 答案是哈哈 这个差不多就是剪切的作用

'''b = a.pop(0)
c = a.pop(0)
print(b+c)#为3 b是1 1没了 那c就是2'''

'''a.clear()
print(a)'''#清空数组

'''xx = ["你好","不好"]
a.extend(xx)  #合并数组的作用
print(a)
print(a+xx)
#[1, 2, 3, 4, '哈哈', '嘻嘻', True, False, '你好', '不好']
 [1, 2, 3, 4, '哈哈', '嘻嘻', True, False, '你好', '不好', '你好', '不好']'''

'''b = a.remove("哈哈")#删除某个值
print(a)#去掉哈哈
print(b)#None'''

'''a.remove(0)
print(a)'''#这儿结果是[1, 2, 3, 4, '哈哈', '嘻嘻', True]默认false是0

#下标不要超出范围 超过就叫超界
#元组和数组的区别是，元组写好后不可以修改(优点)，而数组可以修改的'''


'''
所有的方法都是小括号结尾  input() print() len()
元组 数组 字典的取值 都是中括号 ，比如 a[0]
元组 数组 字典 分别是 () [] {}
'''

'''
字典的特点 
1.字典中的值没有顺序
2.字典的结构必须是键值对的结构   key:value
3.字典的取值必须是用key取value
'''
a = {"name":"张三",0:"哈哈","age":22}#字符串都需要加引号
#取值
'''print(a["name"])
print(a["age"])
print(a[0])

#新增
a["height"] = 174
print (a)
a["weight"] = 58
print (a)

#修改
a["name"] = "李四"
print(a)

#经常使用的方法 get()新增 pop()剪切 update()新增或修改
b = a.get("name")
print(b)

b = a.pop("name")
print(b)
print(a)

a.update(name=1111)  #这里name就得看成是一个变量 不用加引号 后面的如果是字符串必须加引号 这里是1111所以不用
print(a)
'''

'''print(a.get("name"))
print(a["name"])
 两个效果是一样
 '''

'''print(a.get("name11"))#上面是None
print(a["name11"])#下面是报错 这里就不一样了
'''

#数组和字典的删除
'''del a["name"]
print (a)
'''

'''del a[0]#数组的删除
print (a)'''

#print(a["name"])

'''
获取用户输入的个人信息，并且存储到字典中
个人信息包括了 name,age,sex

'''
'''name = input("请输入你的姓名：")
age = input("请输入你的年龄：")
sex = input("请输入你的性别:")
b = {}

方法一
#b.update(name=name,age=age,sex=sex)
方法二
#b = {"name":name,"age":age,"sex":sex}

print(b)'''


