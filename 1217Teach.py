#迴圈(Loop)
"""

range()整數串列
range(終止值)
range(起始值,終止值,間隔值)


"""

list1 = range(5)
print(list(list1))
# [0, 1, 2, 3, 4]

list2 = range(3,8)
print(list(list2))
# [3, 4, 5, 6, 7]

list3 = range(3,8,2)
print(list(list3))
# [3, 5, 7]

list4 = range(8,3,-1)
print(list(list4))
# [8, 7, 6, 5, 4]

list5 = range(-2,4) #起始值為負值
print(list(list5))
# [-2, -1, 0, 1, 2, 3]

list6 = range(6,-2,-3)
print(list(list6))
# [6, 3, 0]

"""
for 迴圈

for 變數 in 串列:
    程式區塊
"""

list7 = ["燕巢校區","第一校區","旗津校區","建工校區","楠梓校區"]
for s in list7:
    print(s)

#1+....10
total = 0
for i in range(1,11):
    total += i
print(total)
#print(sum)

print(f'v2：{sum([i for i in range(1,11)])}')

total2 = 0
n = int(input("請輸入一個正整數n"))
for i in range(1,n+1):
    total2 += i
#print("1到{}的整數和為{}".format(n,total2))
print("1到%d的整數和為%d"% (n,total2))

#加總(起始、終值、及遞增/遞減值由使用者輸入)
b = int(input("請輸入加總起始值："))
e = int(input("請輸入加總終止值："))
s = int(input("請輸入加總遞增/遞減值："))
sum = 0
for a in range(b,e+1,s):
    sum += a
    print("i為",a,"加總結果為:",sum)

#99乘法表
for i in range (1,10):
    for j in range(1,10):
        product = i * j
        print("%d*%d = %2d  " % (i,j,product), end="")
    print()

#計算1*1+2*2+.....+n*n

sum =0
n = int(input("請輸入n的值:"))

if n>=1 and n<=1000:
    for i in range(1,n+1):
        product = i*i
        sum += product
    print(sum)
else:
    print("題目超過題目要求")

#求階層1!+2!+3!....+n!
sum = 1
total = 0
n = int(input("請輸入n的值:"))
for i in range(1,n+1):
    sum *= i
    total += sum
print(total)

#break(跳出) & continue(跳過)

#break
for i in range(1,11):
    if(i==4):
        break
    print(i,end=" ")
print("break")

#continue
for i in range(1,11):
    if(i==4):
        continue
    print(i,end=" ")
print("continue")


n = int(input("請輸入一個數值："))
b = int(input("排除何數的倍數："))

for i in range(1,n+1):
    if(i%b==0):
        continue
    print(i,end=" ")
    

"""
while 迴圈

while 條件式:
    程式區塊
"""

#範例1 1+2+....10
n = sum = 0
while (n<10):
    n += 1
    sum += n
print(sum)

#範例2 1~10偶數總和
n = 1
sum = 0
while n <=10:
    if n%2==0:
        sum = sum+n
    n = n+1
print(sum)

"""
利用While迴圈計算1~1000之間3的倍數，並且是奇數的總和
"""

n = 1
sum = 0
while n<=1000:
    if n%2 !=  0 and n%3 ==0:
        sum = sum+n
    n = n+1
print(sum)

#利用while寫出n!

n = int(input("請輸入n"))
sum = 1
while n>1:
    sum = sum*n
    n = n-1
print(sum)

# n! > M
pro = i =1
m = int(input("請輸入M?"))
while (pro<m):
    i = i+1
    pro = pro*i
print(i,"階層為",pro,"大於",m)

#輸入帳密，判斷正確與否。While

ac = str(123)
pd = str(456)
wac = str(input("請輸入帳號"))
wpd = str(input("請輸入密碼"))
while (ac != wac or pd != wpd) or (ac != wac and pd != wpd) or (ac == wac and pd == wpd) or (ac == wac and pd != wpd) or (ac != wac and pd == wpd):
    if ac == wac and pd != wpd:
        print("帳號正確，密碼錯誤")
    elif ac != wac and pd == wpd:
        print("帳號錯誤，密碼正確")
    elif ac != wac or pd != wpd:
        print("帳號密碼皆錯誤")
    else:
        print("帳號密碼正確")
    break




#輸入一整數，判斷其因數有哪些?並判斷是否為質數。while
n = int(input("請輸入整數"))
j = 2
i = 0
prime = True
while j<n:
    if(n%j==0):
        prime = False
        break
    j+=1
if prime:
    print(n,'是質數')
else :
    print(n,'不是質數')
    while i <= n:
        i += 1    
        if n%i ==0:
            print("有因數:",i,end = "\n")
            n = n/i
            i = 1
            pass
        else:
            pass


#輸入一整數，判斷其因數有哪些?並判斷是否為質數。while
n = int(input("請輸入整數"))
sum = 0
i = 1
print("因數有",end=" ")
while i<=n:
    if n%i == 0:
        sum += 1
        print(i,end=" ")
    i +=1
if sum>2:
    print("\n",n,"不是質數")
else:
    print("\n",n,"是質數")
    
    
#for & while
#1.break

for i in range(1,6):
    print(i)
    if i == 4:
        break

i = 1
while (i<6):
    print(i)
    if i == 4:
        break
    i = i+1

#2.continue

for i in range(1,6):
    if i == 4:
        continue
    print(i)

i = 0
while (i<6):
    i = i+1
    if i == 4:
        continue
    print(i)