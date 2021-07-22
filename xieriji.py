#python的读写
import time
now = time.strftime("%y-%m-%d %H:%M:%S")
print(now)
text = input("请输入今天的心情：")
with open(。 "日记.txt","a",encoding="utf8") as f:#w每次都是新的内容 而a是追加
    f.write(now+"\n")
    f.write(text+"\n") #换行