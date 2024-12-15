# 一、變數與資料型態

"""
宣告變數
大小寫不同
名稱:大小寫英文、數字、中文(不建議)
第一個字母不能是數字
"""



X = 1  #C int float
y = 0.1
a = b = c = 0
age, name = 18 , "資訊管理系"

print(age,name)

"""
2.變數資料型態
整數(int)、浮點數(float)、字串(str)、布林(bool) False/True
查看資料型態type()
資料型態的轉換int(),float(),str()
"""

test = 2.2
print(type(test))


justdoit = False

weight = 123.5
zipcode = "545"
msg = """
Alex
Rooney
Peko
"""
# print(msg)
age = 2
name = "Alex"
print(type(age))
print(type(name))

zipcode = "545"
age = 2
num1 = 8+True
num2 = 8+False
num3 = age + int(zipcode)
num4 = str(age) + zipcode

print(num1,num2,num3)
print(num4)

name1 = "Alex's iphone"

# 二、輸出(print)
"""
print(項目1,[項目2,....(,sep=分隔字元, end =結束字元)])
分隔字元預設' '(空白)，結束字元預設\n(換行)
"""

print(100 ,"資訊管理系", True )
print(str(100) + "資訊管理系" + str(True) )
print(100 ,"資訊管理系", True , sep="#" , end="\n")

"""
2-1 print() 命令參數格式化 (%)
print(項目 % (參數列))
%s (字串)
%d (整數)
%f (浮點數)
"""

print("%s的成績是%d分" % ("班代",80))
print("%5s的成績是%3d分" % ("班代",80))
print("%-5s的成績是%3d分" % ("班代",80))

print("我的體重有%f分" % (80))
print("我的體重有%-6.2f分" % (80.566))

"""
2-2 format
print(字串.format(參數列))
{}:參數位置
{i}: 索引值
{i:格式化指定}
對齊方式:>靠右 <靠左 ^
s字元
d整數
f浮點數
"""
print("班代的成績為80")
print("{}的成績為{}".format("班代",80))
print("{1}的成績為{0}".format("班代",80))
print("{0:^5s}的成績為{1}".format("班代",80))


"""
2-3 (f)
print(f字串)
"""

name3 = "班代"
score = 80
print(f"{name3}的成績為{score}")
print(f"{name3:>5}的成績為{score}")
print(f"{name3:x>5}的成績為{score:03}") #不足會補值

# 課堂練習1
print("B11323222 劉政廷")
print("{0:3s}　{1:3s}　{2:2s}　{3:2s}　{4:2s}".format ("姓名","座號","國文","數學","英文"))
print("{0:3s}　{1:>4d}{2:>5d}{3:>5d}{4:>5d}".format ("林大明",1,100,87,79))
print("{0:3s}　{1:>4d}{2:>5d}{3:>5d}{4:>5d}".format ("陳阿中",2,74,88,100))
print("{0:3s}　{1:>4d}{2:>5d}{3:>5d}{4:>5d}".format ("張小英",11,82,65,8))

# 課堂練習2
print("B11323222 劉政廷")
print("{0:2s}　{1:3s}　{2:3s}　{3:3s}".format ("年度","所得稅","營業稅","證交稅"))
print("{0:2s}　{1:>.2f}　{2:>6.2f}　{3:>.2f}".format ("2017",98.84,90.20,104.79))
print("{0:2s}　{1:>.2f}　{2:>6.2f}　{3:>.2f}".format ("2016",83.00,110.50,82.45))
print("{0:2s}　{1:>.2f}　{2:>6.2f}　{3:>.2f}".format ("2015",98.00,79.32,102.00))

# 輸入 input

input("")
"""
變數 = input([提示字串])
由input()所接收的值型別是字串
"""


# 課堂練習4
print("B11323222 劉政廷")
y1 = str(input("請輸入年度"))
o1 = float(input("請輸入所得稅"))
p1 = float(input("請輸入營業稅"))
l1 = float(input("請輸入證交稅"))
print("您輸入{}年的年度資料為:所得稅:{},營業稅:{},證交稅:{}".format(y1,o1,p1,l1))
y2 = str(input("請輸入年度"))
o2 = float(input("請輸入所得稅"))
p2 = float(input("請輸入營業稅"))
l2 = float(input("請輸入證交稅"))
print("您輸入{}年的年度資料為:所得稅:{},營業稅:{},證交稅:{}".format(y2,o2,p2,l2))
y3 = str(input("請輸入年度"))
o3 = float(input("請輸入所得稅"))
p3 = float(input("請輸入營業稅"))
l3 = float(input("請輸入證交稅"))
print("您輸入{}年的年度資料為:所得稅:{},營業稅:{},證交稅:{}".format(y3,o3,p3,l3))
print("{0:2s}　{1:3s}　{2:3s}　{3:3s}".format ("年度","所得稅","營業稅","證交稅"))
print("{0:2s}　{1:>.2f}　{2:>6.2f}　{3:>6.2f}".format (y1,o1,p1,l1))
print("{0:2s}　{1:>.2f}　{2:>6.2f}　{3:>6.2f}".format (y2,o2,p2,l2))
print("{0:2s}　{1:>.2f}　{2:>6.2f}　{3:>6.2f}".format (y3,o3,p3,l3))

# 運算子
"""
1.算數運算子
+, -, *, /, %(餘數), //(商), **(指數)
2.比較運算子
==, <=, >=, <, >, !=(不等於)
3.邏輯運算子
not(反閘), and(及閘), or(或閘)
4.複合指定運算子
+=, -=, /=, %=, //=, **=
"""

# 數值運算
a = 5
b = 2

print(a+b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)

#範例1 (梯形面積)
top = float(input("請輸入上底長度為:"))
bottom = float(input("請輸入下底長度為:"))
heigh = float(input("請輸入高的長度為:"))
area = (top+bottom) * heigh / 2
print("梯形面積為:" + str(area))

#範例2 (溫度轉換)

c = float(input("請輸入攝氏溫度:"))
f = c * 9 / 5 + 32
print("華氏溫度:" + str(f))
print(f"攝氏{c}度等於華氏{f}度")
print("攝氏{1}度等於華氏{0}度".format(f,c))

#範例3 (BMI)
h = float(input("請輸入您的身高(cm):"))
w = float(input("請輸入您的體重(kg):"))
bmi = w / (h/100) **2
print("身高{}公分, 體重{}公斤, BMI值為{:.2f}".format(h,w,bmi))

# 比較運算子
x = 5
y = 2
print(x == y)
print(x != y)
print(x >= y)
print(x <= y)
print(x > y)
print(x < y)

# 邏輯運算子
a = 5
b = 2
print(not(a==b))
print((a>=b))
print((a==b) and (a>=b))
print((a==b) or (a>=b))

# 複合指定運算子
i = 20
i += 2 #i = i+2
print(i)

# 字串運算
s = "123456789"
print(s)

print(s * 2) #複製字串
print(s[8]) #取值 []為索引值
print(s[-2])

print(s[1:5]) #切割字串[開始:結束(不包含本身):間隔]
print(s[:]) #全取
print(s[2:]) #從開始印到最後一個
print(s[:3]) #從結束(不包含本身)往前

print(s[:-2])
print(s[-4:-1])
print(s[3:-2])
print(s[2:8:2])
print(s[::-1]) #迴文
print(s[-1::-1]) #會等於[::-1]

#練習1 
t1 = int(input("請輸入第一次期中考成績？"))
t2 = int(input("請輸入第二次期中考成績？"))
t3 = int(input("請輸入期末考成績？"))
total = t1+t2+t3
av = total/3

print("總分為{}平均為{}".format(total,av))

#練習2
r = eval(input("請輸入幾尺？"))
u = eval(input("請輸入幾吋？"))
r1 = r*12
u1 = r1+u
cm = u1*2.54
print("轉換成{}公分".format(cm))

#練習3
num = eval(input("請輸入座號？"))

if num%5 ==0:
    team = num // 5
else:
    team = num // 5 +1

print("組別為{}".format(team))

#練習4
b = eval(input("請輸入購買罐數？"))
a = b // 12
c = b % 12
m1 = a * 200
m2 = c * 20
total = m1+m2
print("需花費{}".format(total))

# 判斷式 control
"""
1.單向判斷式
if 條件式:
    程式區塊
"""

#範例1(成績)
score = int(input("請輸入你的成績？"))
if score>=60:
    print("PASS")

#範例2(PW)
pw =  input("請輸入密碼")
if (pw == "1234"):
    print("歡迎光臨")

#範例3(天氣)
rain = input("明天會下雨嗎？(Y/N)")
if rain =="Y" or rain=="y" or rain=="會":
    print("請你攜帶雨具")

"""
2.雙向判斷
if 條件式:
    程式區塊1
else:
    程式區塊2
"""

#範例1(成績)
score = int(input("請輸入你的成績？"))
if score>=60:
    print("PASS")
else:
    print("未通過")

#範例2(PW)
pw =  input("請輸入密碼")
if (pw == "1234"):
    print("歡迎光臨")
else:
    print("密碼錯誤")

#範例3(判斷奇偶數)
n = int(input("請輸入一個正整數："))
if (n%2==0):
    print(f"數字{n}為偶數")
else:
    print(f"數字{n}為奇數")

#範例4(判斷三邊是否能構成三角形)
a = int(input("第一個邊的長度"))
b = int(input("第二個邊的長度"))
c = int(input("第三個邊的長度"))

if (a+b>c) and (b+c>a) and (c+a>b):
    print("可構成三角形")
    print("周長為：{}".format(a+b+c))
else:
    print("不可構成三角形")
    
    
"""
3.多項判斷式
if 條件式1:
    程式區塊1
elif 條件式2:
    程式區塊2
elif 條件式3:
    程式區塊3
....
else:
    程式區塊N
"""

#範例1(成績等第)
score = int(input("請輸入你的分數:"))
if score >= 90:
    print("甲等")
elif score >= 80:
    print("乙等")
elif score >= 70:
    print("丙等")
elif score >= 60:
    print("丁等")
else:
    print("您的成績未通過")

#範例2(電影等級)
age = int(input("請輸入你的年齡:"))
if (age < 6):
    print("普通級")
elif (age < 12):
    print("普通級、保護級")
elif (age < 18):
    print("限制級以外")
else:
    print("所有級別")

#範例3(成績等第(換方式))
score = float(input("請輸入您的成績(0-100):"))
if score < 0 or score > 100:
    print("輸入成績範圍有誤")
else:
    if 90 <= score:
        print("A")
    elif 80 <= score and score < 90:
        print("B")
    elif 70 <= score and score < 80:
        print("C")
    elif 60 <= score and score < 70:
        print("D")
    else:
        print("E")

#範例4(成績等第)-巢狀
score = float(input("請輸入您的成績(0-100):"))
if score < 0 or score > 100:
    print("輸入成績範圍有誤")
else:
    if 90 <= score:
        print("A")
    else:
        if score >= 80:
            print("B")
        else:
            if 70 <= score:
                print("C")
            else:
                if 60 <= score :
                    print("D")
                else:
                    print("E")

#練習1(國軍計算)
s = str(input("請輸入性別(男or女)："))
w = float(input("請輸入體重(公斤):"))
h = float(input("請輸入身高(公尺):"))
bmi = w / h**2

if s == "男":
    if bmi < 31 :
        print("合格")
    else:
        print("不合格")
else:
    if bmi < 26 :
        print("合格")
    else:
        print("不合格")

#練習2(座標判斷)
x = float(input("請輸入X座標："))
y = float(input("請輸入y座標："))

if x > 0 and y>0:
    print("第I象限")
elif x < 0 and y>0:
    print("第II象限")
elif x < 0 and y <0:
    print("第III象限")
elif x > 0 and y < 0:
    print("第IV象限")
elif x ==0 and y ==0:
    print("在原點")
elif x == 0 and y != 0:
    print("Y軸上")
else:
    print("X軸上")

#練習3(熱量計算)
a = int(input("請輸入每日活動量(1:輕度,2:中度,3:重度)："))
h = float(input("請輸入身高(公尺):"))
w = float(input("請輸入體重(公斤):"))
bmi = w / h**2
hot = 0

if a == 1:
    if 24 <= bmi <27:
        hot = 25*w
    elif 18.5 <= bmi < 24:
        hot = 30*w
    else:
        hot = 35*w
elif a == 2:
    if 24 <= bmi <27:
        hot = 30*w
    elif 18.5 <= bmi < 24:
        hot = 35*w
    else:
        hot = 40*w
else:
    if 24 <= bmi <27:
        hot = 35*w
    elif 18.5 <= bmi < 24:
        hot = 40*w
    else:
        hot = 45*w

print("BMI為{}".format(bmi))
print("所需熱量為{:.2f}".format(hot))