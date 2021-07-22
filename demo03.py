'''a = input("请输入你的名字：")
b = input("请输入你的年龄：")
try:
    if int (b) >= 18:
        print(a,"成年了")
    else:
        print(a,"未成年")    
except Exception as e:
    print("请输入正确的年龄！")'''

#处理用户输入的数据

'''代码的单位
包  自带的包  import
    第三方的  pip install 包名
              pip uninstall 包名
              pip list
    常见的第三方的包pymysql selenium appium requests xlrd xlwt ...
模块
类 #class 
class 声明类的名字首字母必须要大写 继承 重写
class Test():
面向对象工程
类里面所有的方法，都必须要传一个参数，叫self


class GirlFriend():
    def__init__(self):#def __init__(self,sex,high,weight,hair,age):
        self.sex = "女"          #self.sex = sex
        self.high = "170cm"      #self.high = high
        self.weight = "55kg"     #self.weight = weight
        self.hair = "大波浪"     #self.hair = hair
        self.age = "18岁"        #self.age = age
    def caiyi(self,num):
        if num == 1:    
            print("胸口碎大石");
        elif num == 2:    
            print("唱跳")
        else:    
            print("单手开瓶盖")
    def work(self):
        print("开挖掘机")


#类的实例化

zhangsan = GirlFriend()#zhangsan = GirlFriend("男 ","183","90kg","锡纸烫","32岁")
zhangsan.caiyi(1)
zhangsan.work()
print(zhangsan.high)

class Nvpengyou(GirlFriend):
    pass
zhangsan = Nvpengyou("""""""""")
zhangsan.work()

def work(self)
    print("修电脑")

#GirlFriend 父类
 Nvpengyou 子类



方法
变量   
'''


'''import time   #引用
import random'''

'''for i in range(10):
    time.sleep(10)
    print(i)'''
'''a = random.randint(1,1000)
print (a)'''    



class Car():
    def __init__(self, pingpai,yanse,neishi,jilun):
        self.pingpai = pingpai
        self.yanse = yanse
        self.neishi = neishi 
        self.jilun = jilun
    def bianxing(self):
        print("车子变身成喜羊羊")
    def fly(self):
        print("车子飞")
zhangsan = Car("aodi","hua","haokan","dulun")
print(zhangsan.neishi)
zhangsan.bianxing()










