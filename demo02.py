#判断
'''a = 1
b = 2
if a > b:
    print("a比b大")
else:
    print("b更大")
'''

'''age = int(input("请输入你的年龄:"))
if age > 60 and age <= 70:
    print("为")
elif age > 30 and age <= 40:
    print("人")
elif age >20 and age <= 30:
    print("师")
else:
    print("表")    '''

'''a = input("请输入：")
if a in "0123456789":
    a = int(a)
else:
    print("请输入正确的年龄")
    exit()
if a > 5:
    print("da")
else:
    print("xiao")'''

'''a = 10
if type(a) is int:
    print("shi zhengshu")
elif type(a) is str:
    print("shi zifuchuan")
else:
    print("shi biede")
    '''

#现在有十个学生，分别录入10个成绩 分别是一二三四五六七八九十
#成绩60以上和60以下分开存放
'''highchengji = {}
lowchengji = {}
student = ["一","二","三","四","五","六","七","八","九","十"]
a = 0#定义了一个变量，用于控制数组下标的变化
while a < len(student):
    chengji = int(input(student[a]+"的成绩为："))
    if chengji >= 60:
        highchengji[student[a]] = chengji 
    else:
        lowchengji[student[a]] = chengji
    a = a + 1
print(highchengji,lowchengji)
'''


#遍历
#a = "你还，今天你吃了吗？"
'''a = ["一","二","三","四","五","六","七","八","九","十"]
for i in a:
    print(i)'''

'''b = list(range(0,100))
print(b)'''

'''for i in range(0,100):
    print(i)'''

'''b = list(range(0,100,2))#步进
print(b)'''

'''for i in range(10):
    print(i)'''

'''
用for循环解决这个问题
highchengji = {}
lowchengji = {}
student = ["一","二","三","四","五","六","七","八","九","十"]
for i in student:
    chengji = int(input(i +"的成绩为："))
    if chengji >= 60:
        highchengji[i] = chengji 
    else:
        lowchengji[i] = chengji
print(highchengji,lowchengji)'''


#99乘法表

'''for i in range(1,10):
    for j in range(1,i+1):
        print(i,"*",j,"=",i*j,end="|")
    print()
'''


'''
student = ["一","二","三","四","五","六","七","八","九","十"]
for i in student:
    print(i,end=" ")
    print("------------",end=" ")##一 ------------ 二 ------------ 三 ------------ 四 ------------ 五 ------------ 六 ------------ 七 ------------ 八 ------------ 九 ------------ 十 ------------
'''

#通过print打印，实现红绿灯，红灯30次，绿灯35次，黄灯3次
'''light = {"红灯":30,"绿灯":35,"黄灯":3}
#light["红灯"]=50
while True:
    for i in light:#对字典中用in那就指的是key 这里是红灯绿灯黄灯
        for j in range(light[i]):
            print (i,"倒计时还有",light[i]-j,"秒")'''
#为什么用字典的原因？是因为可以随意修改删除 就像上面的light["红灯"]=50

#实现一个注册功能，用户输入账号和密码，账号长度5-8位，密码6-12位，并且账号必须小写开头，储存到字典中，{username,password}
'''
zhuce = {}
username = input ("请输入账号:")
password = input ("请输入密码:")
if len(username) >= 5 and len(username) <=8:
    if username[0] in "abcdefghijklmnopqrstuvwxyz":
        if len(password) >= 6 and len(password) <= 12:
            print("注册成功")    
            zhuce[username] = password
            print("您的账号密码是",{username,password})
            
            ???zhuce.upadate(username=password) 
            print(zhuce{})#这个不行???  
        
        else:
            print("密码必须是6-12位")
    else:
        print("首字母必须小写开头")
else:
    print("账号的长度不符合规范，请输入5-8位的账号")
'''

# for i in range(10):
#     if i == 4:
#         #continue #跟java差不多
#         break
#     print(i)


#函数/方法
'''
自动的判断账号长度是不是5-8位，并且账号必须小写开头
'''

'''def checkname(username):
    if len(username) >= 5 and len(username) <= 8:
        if username[0] in "abcdefghijklmnopqrstuvwxyz":
            print("ok")
        else:
            print("首字母必须小写") 
    else:
        print("长度必须5-8位")           

checkname("s232432")
checkname("121233")
#def 方法的声明
#checkhome 方法的名字
#username 方法的参数
#方法的逻辑代码
#方法的说明
'''


'''def jiafa(a,b):
    
    
    #方法的作用是实现两个数字相加 #这儿想实现这个方法说明，必须上面和下面都有三个单引号，且中间一行必须第一个和上下两个三个单引号对齐，这样能做到方法说明
    
    
    if type(a) is int and type(b) is int:
        print(a+b)
    else:
        print("输入类型不对")

jiafa(1,2)
jiafa("a",2)
'''
#方法的返回值 把上面那个print换成return 那么print(jiafa(1,1))值就不是None了，那就是2了
#返回值，返回后我们可以对这个值做其他的操作而print不能

'''def checkname01(username):
    if len(username) >= 5 and len(username) <=8:
        if username[0] in "abcdefghijklmnopqrstuvwxyz":
                return True
        else:
            return ("首字母必须小写开头")   #这一段代码说明了这个return的作用，上面一段什么时候是True，就是当账号符合要求的时候，但是当不符合的时候，他就是下面那段代码的最后的else，正常打印出来，
                                            但是如果返回值就是true，那么就继续往下运行代码，即判断password，方便。
    else:
        return ("账号的长度不符合规范，请输入5-8位的账号")

username = input ("请输入账号：")
password = input ("请输入密码：")
if checkname01(username) == True:
    if len(password) >= 8 and len(password) <=12:
        print("注册成功")
    else:
        print("密码长度不对，应该是8-12位")
else:
    print(checkname01(username))'''


#异常捕获
try:
    print("11"+1)
except Exception as e:
    print("上面的代码写错了",e)

#包 ———>类 ————>方法—————>变量    并列关系

#异常类