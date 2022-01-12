#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 13:03:45 2022

@author: miyagawatakuya
"""

"""
#for i in range(15):
#  print(i)

my_life = 5
while my_life:  #0で処理が止まる
    my_life -= 1
    print(my_life)
    
my_life = -5
while my_life:  #0で処理が止まる
    my_life += 1
    print(my_life)
"""
"""
for item in ["M","A","T"]:
    print(item)
    
idx=0
while True:
    if idx >5:
        break
    print(idx)
    idx +=1
"""
"""
users = ["Yo","Takuya","Akira","Nao","Lee"]
print(users[1])
print(users[0:2])
print(users[1:3])
print(users[1:])  
print(users[::3])
print(users[:3])  #0から3のてまえ(2番目)までの値を返す
users.append("Kanon")
print(users)
users.remove("Yo")
print(users)
users[4]="Lion"
print(users)

users = [u.lower() for u in users if u.find("o") != -1]  #該当する文字列を小文字に変える
print(users)
"""
"""
user_dict ={"Takuya":32,"Tsubasa":25,"Mayo":42}
print(user_dict["Takuya"])
print(user_dict.get("Takkun",45))  #第二引数は値がなかった場合のデフォルト値

for k,v in user_dict.items():   #全ての値を取得する
    print(k,v)
    
del user_dict["Mayo"]
for k,v in user_dict.items():   #全ての値を取得する
    print(k,v)
"""
"""
#tuple 変更できないリスト構造
nums = "One", "Two", "Three"
numss = ("One", "Two", "Three")
print(numss)
"""
"""
#演習<2>
jumon ="じこーだずまあさかんでのみしーゅっみてはたなのんしだいろな"
print(jumon[0::2])  #0初め2刻み　偶数番目の値を拾う  
print(jumon[1::2])   #01から2刻み　奇数番目の値を拾う 
#演習<3>
gintetsu = "天の川の形はちょうどこんななのです。このいちいちの光るつぶがみんな私どもの太陽と同じようにじぶんで光っている星だと考えます。私どもの太陽がこのほぼ中ごろにあって地球がそのすぐ近くにあるとします。みなさんは夜にこのまん中に立ってこのレンズの中を見まわすとしてごらんなさい。こっちの方はレンズが薄うすいのでわずかの光る粒即すなわち星しか見えないのでしょう。"
#for s in gintetsu:
#    print(s)
set_gin = set(gintetsu)
print(set_gin) 
"""
"""
#演習<4>
#for i in range(101):  #0から101の手前までの値(100)をとる
#    print(i)
hundredArray = [str(u) + "円" for u in range(101)] 
print(hundredArray)
"""
"""
def add(a,b):
    return a + b * 2
result = add(20,10)
print(result)

def pow(a,b=99):
    return a * b
result = pow(20)
print(result)
result = pow(20,3)
print(result)

def create_date(year=0,month=1,date=1):
    return "今日は" + str(year) + "年," + str(month) + "月," + str(date) + "日"
print(create_date())
print(create_date(year=2022,date=30))

#複数のreturn
def tow():
    return "Yohey",555
name, age = tow()
print(name)
print(age)

#演習<5> 関数
def two(x,y=20):
    return "私の名前は" + x +"で" + str(y) + "歳です"
print(two("Takuya"))
print(two("Takuya",32))
"""

#クラス
class User:
    def __init__(self, name):
        self.name = name
    def say(self, name2):
        self.name2 = name2
        print("Hi!!" + name2)

user = User("Yohei") #インスタンスの生成の仕方がC#と違う
print(user.name) 
user.say("Takuya")  #メソッドの中にprint処理が既に入っている




