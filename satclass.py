"""
#day1
a = 1
b = 3.1
c = "abc"

print(a)
print(type(a))

a = "3"
print(a, type(a))

a = int(a)
print(a, type(a))

a = float(a)
print(a, type(a))
"""

"""
a = int(input())
b = int(input())

print(a + b)
print(a - b)
print(a * b)
print(a ** b)
print(a / b)
print(a // b)
print(a % b)
"""

"""
a = 1
if a == 1:
    print("hi")
print("kkk")
"""

"""
a = int(input())

if a % 2 == 0:
    print("even")
else:
    print("odd")

"""
"""
a = int(input())

if a == 0:
    print("zero")
elif a == 1:
    print("one")
elif a == 2:
    print("two")
else:
    print("etc")
"""
"""
a = 5
b = 3
c = int(input())

if c == 1:
    print(a+b)
elif c == 2:
    print(a - b)
elif c == 3:
    print(a * b)
elif c == 4:
    print(a / b)
elif c == 5:
    print(a % b)
"""
"""
# 1.초기값 2. 조건식 3. 증가/감소
a = 0
while a < 100:
    print("10")
    a += 1 # a = a + 1

for i in range(101):
    print("10")
"""
"""
for i in range(1,10,3):
    print("hi",i)
"""
"""
for i in range(1, 11):
    print("*" * i)
"""
"""
for i in range(10, 0, -1):
    print("*" * i)
"""

"""
for i in range(1,100):
    one = i % 10
    if one % 3 == 0 and one != 0:
        print("*")
    else:
        print(i)
"""
"""
for i in range(1, 100):
    one = i % 10
    ten = i // 10
    one_con = one % 3 == 0 and one != 0
    ten_con = ten % 3 == 0 and ten != 0

    if one_con and ten_con:
        print("**")
    elif one_con or ten_con:
        print("*")
    else:
        print(i)
"""
"""
for a in range(2,10):
    for i in range(1,10):
        print("{} * {} = {}".format(a, i, a*i))
    print()
#------------------------------------------------
"""
"""
for i in range(2,10):
    for j in range(1,10):
        print("{} * {} = {}".format(i, j, i*j))
    print()
"""
"""
cnt=0
a = int(input())
for i in range(2,a // 2 + 1):
    if a % i == 0:
        cnt = 1
        break
if cnt == 0:
    print("소수")
else:
    print("소수 아님")
"""

"""
a = 0
while a < 5:
    print("hi", a)
    # a = a + 1 or a += 1 출력 값이 5번 나오게 하기.
"""
"""
a = 2
while a < 10:
    b = 1
    while b < 10:
        print("{} * {} = {}".format(a, b, a * b))
        b += 1
    a += 1
    print()
"""
"""
a = []
a.append(3)
a.append(4)
a.append(5)
print(a)
print(a[1])

b = [3, 4, 5]
print(len(b))
"""
"""
a = [2, 3, 4, 5]
for i in range(len(a)):
    print(a[i])
"""
"""
import random
b = random.randrange(1, 100)
print(b)

a = []
for i in range(10):
    b = random.randrange(1, 100)
    a.append(b)
print(a)
"""
"""
import random
a = []

for i in range(10):
    b = random.randrange(1, 100)
    a.append(b)
big = a[0]

for i in range(1, len(a)):
    if big < a[i]:
        big = a[i]
print(a)
print(big)
"""
"""
x = int(input())
a = []
while x != 0:
    a.append(x % 2)
    x //= 2
for i in range(len(a)-1, -1, -1):
    print(a[i], end=" ")
"""
"""
b = int(input())
a = []
for i in range(1, 101):
    a.append(i)
low = a[0]
high = a[99]
cnt = 1
while low <= high:
    mid = (low + high)//2
    if b == mid:
        print("{}를 찾는데 {}번 탐색하였습니다.".format(a[b-1], cnt))
        break
    elif b < mid:
        high = mid - 1
        cnt += 1
    else:
        low = mid + 1
        cnt += 1
"""
"""
a = [1, 2, 3, 4]
b = []
for i in range(len(a)):
    if i == 1:
        continue
    b.append(a[i])
"""
"""
#슬라이싱
a = [1, 2, 3, 4, 5, 6, 7]

print(a[2:5])
"""

"""
start = 0
end = 100
mid = (start + end) // 2
val = int(input())
for i in range(100):
    if val == mid:
        break
    elif val > mid:
        start = mid
    else:
        end = mid
    mid = (start + end) // 2
if i > 50:
    print("not find value")
else:
    print("find",i)
"""
"""
a = input()
for i in range(0, len(a)//2):
    if a[i] != a[len(a)-1-i]:
        print("NO")
        exit()
print("YES")
"""
"""
a = input()
flag = 0
for i in range(len(a)//2):
    if a[i] != a[len(a)-1-i]:
        flag = 1
        break
if flag == 1:
    print("NO")
else:
    print("YES")
"""
"""
a = input()
reverse = []
not_reverse = []
for i in range(len(a)):
    reverse.append(a[i])
    not_reverse.append(a[len(a)-1-i])
flag=0
for i in range(len(reverse)):
    if reverse[i] != not_reverse[i]:
        flag = 1
        break
if flag == 1:
    print("not same")
else:
    print("same")
"""


"""
#튜플
a = (1,2,3)

#한번 값을 할당하면 바꿀 수 없다. list와 비슷하지만 메모리 측면에서 더 효율적으로 사용할 수도 있다.
"""

"""
a = [1,"a",[1,"a"]]
a = [[1,2,3],[4,5,6]]
print(a[0])
print(a[0][2])
"""
"""
a = dict()

a = {'kkk': 170, 'age':100, 'value': 200, 'height' : 180, 'height': 190}
print(a['kkk'])
print(a.keys())
print(a.values())
print(a['height'])
"""
"""
def add_test(x, y):
    #print(x + y)
    return x + y
#add_test(1,3)
print(add_test(1,3))

c = add_test(1,3)
print(c)
"""
"""
def add1(x, y):
    print(x+y)

def add2(x, y):
    z = x + y
    return z

a = int(input())
b = int(input())
add1(a, b)

c = add2(a, b)
print(c)
"""
"""
def test_hi(b,c):
    a = b + c
    print(a)
test_hi(3,5)
"""
"""
dan = int(input())
for i in range(1,10):
    print("{}*{}={}".format(dan,i,dan*i))

def gugu(x):
    for i in range(1,10):
        print("{}*{}={}".format(x, i, x*i))

dan = int(input())
gugu(dan)
"""
"""
def clock(s):
    h = s // 3600
    m = s % 3600 // 60
    s = s % 3600 % 60
    print("{}시간{}분{}초".format(h, m, s))
s = int(input("초 입력:"))
clock(s)
"""
"""
def gcd(a, b):
    for i in range(1,a+1):
        if a % i == 0 and b % i == 0:
            cnt = i
            print(cnt)

a = int(input())
b = int(input())
gcd(a,b)
"""
"""
#5 n을 입력받으면 끝자리가 n의 배수인 애들만 *출력
def star(x,y):
    for i in range(1,101):
        one = i % 10
        ten = i // 10
        one_con = one % x == 0 and one != 0
        ten_con = ten % y == 0 and ten != 0
        if one_con and ten_con:
            print("**")
        elif one_con or ten_con:
            print("*")
        else:
            print(i)
a = int(input())
b = int(input())
star(a, b)
"""

#12일 수업---------------------------------------------
"""
def gcd(x, y):
    for i in range(1, x+1):
        if x % i == 0 and y % i == 0:
            num = i
    return num
    
x = int(input("숫자 x입력:"))
y = int(input("숫자 y입력:"))
if gcd(x, y)==1:
    print("서로소")
else:
    print("최대공약수는 {}".format(gcd(x, y)))
    """
"""
#서로소 판별하기
def gcd2(x, y):
    for i in range(1, x+1):
        if x % i == 0 and y % i == 0:
            num = i
    if num == 1:
        print("서로소")
    else:
        print("최대공약수는 {}".format(num))
        print("서로소가 아니다.")
        
x = int(input("숫자 x입력:"))
y = int(input("숫자 y입력:"))
gcd2(x, y)
"""
"""
x = int(input("숫자 x 입력:"))
y = int(input("숫자 y 입력:"))
a = 0
flag=0
if x>y:
    a=y
else:
    a=x
for i in range(2,a+1):
    if x%i==0 and y%i==0:
        flag=1
        break
if flag==1:
    print("서로소가 아니다.")
else:
    print("서로소이다.")
"""
"""
def people(a):
    if(len(a)!=14):
        print("잘못 입력하셨습니다.")
        exit()
        a="941021-1111111"#=>a[0]~a[13]
    else:
        if a[7] == '1' or a[7] == '3':
            gen = 'M'
        else:
            gen = 'W'
        if a[7] == '1' or a[7] == '2':
            age = 2020-(1900 + 10 * int(a[0]) + int(a[1]))+1
        else:
            age = 2020 - (2000 + 10 * int(a[0]) + int(a[1]))+1
    print("나이는 {}살 성별은 {}입니다.".format(age,gen))
a = input()
people(a)
"""

"""
def fact2(a):
    if a <= 0:
        return 1
    else:
        return a * fact2(a-1) #재귀함수

a = int(input("숫자를 입력하시오:"))
print("{}! = {}".format(a,fact2(a)))
"""

"""
def fact1(a):
    tot = 1
    for i in range(1, a+1):
        tot *= i#tot = tot * i
    print("{}! = {}".format(a,tot))

a = int(input())
fact1(a)
"""

"""
#09.19
클래스 - 붕어빵 틀
게임 캐릭터 - hp,mp
1. 캐릭터 만들기
2. 캐릭터 id생성해서 만들기
3. 서로 공격해보기
4. hp가 없어질때까지 공격해보기
5. 스킬 만들어보기
"""
"""
import random

class makeCharacter:

    def __init__(self,id):
        self.name = id
        self.hp = random.randrange(1, 20)
        self.mp = random.randrange(1, 40)
        self.q = random.randrange(1, 4)
        print("{}가 생성되었습니다.\nhp:{}\nmp:{}\n공격력:{}".format(self.name, self.hp, self.mp, self.q))

    def attack(self):
        return self.q

    def attacked(self, atk):
        self.hp = self.hp - atk
    def skill(self):
        self.mp -= 5
        return self.q*2



id = input("Enter character id:")
ogar = makeCharacter(id)
id = input("Enter character id:")
mc = makeCharacter(id)

while True:
    select_skill = int(input("1.attack 2.skill"))
    if select_skill == 1:
        a = mc.attack()
        ogar.attacked(a)
        if ogar.hp <= 0:
            print("{} 사망".format(ogar.name))
            break
        else:
            print("{}가 {}를 {}의 공격력으로 공격했다.\n{}의 hp:{}\n{}의 hp:{}"
              .format(mc.name, ogar.name, a, mc.name, mc.hp, ogar.name, ogar.hp))
    elif select_skill == 2:
        if mc.mp > 0:
            a = mc.skill()
            ogar.attacked(a)
            if ogar.hp <= 0:
                print("{} 사망".format(ogar.name))
                break
            else:
                print("{}가 {}를 스킬로 공격했다.\n{}의 hp:{} mp:{}\n{}의 hp:{}"
                      .format(mc.name, ogar.name, mc.name, mc.hp, mc.mp, ogar.name, ogar.hp))
        else:
            print("마나부족")
            continue
    ogar_rand = random.randrange(1,3)
    if ogar_rand == 1:
        a = ogar.attack()
        mc.attacked(a)
        if mc.hp <= 0:
            print("{} 사망".format(mc.name))
            break
        else:
            print("{}가 {}를 {}의 공격력으로 공격했다.\n{}의 hp:{}\n{}의 hp:{}"
                  .format(ogar.name, mc.name, a, mc.name, mc.hp, ogar.name, ogar.hp))
    elif ogar_rand == 2:
        if ogar.mp > 0:
            a = ogar.skill()
            mc.attacked(a)
            if mc.hp <= 0:
                print("{} 사망".format(mc.name))
                break
            else:
                print("{}가 {}를 스킬로 공격했다.\n{}의 hp:{} mp:{}\n{}의 hp:{}"
                      .format(ogar.name, mc.name, ogar.name, ogar.hp, ogar.mp, mc.name, mc.hp))
        else:
            print("마나부족")
            continue
"""

"""
절대경로 - /home 위에서 부터 내려옴
상대경로 - ./(내 현재 위치에서) ../(현재위치에서 더 상위폴더)
"""

f = open("/Users/cho/Desktop/test_new.txt",'r')
temp = f.readlines()

print(temp)
