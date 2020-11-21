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
a =[]
a.append(3)
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
c = 1
while c < 7:
    b = random.randrange(1, 46)
    if b in a:
        continue
    else:
        a.append(b)
    c += 1
print(a)
"""
"""
import random
a = []

for i in range(10):
    b = random.randrange(1, 101)
    a.append(b)
big = a[0]

for i in range(1, len(a)):
    if big < a[i]:
        big = a[i]
print(a)
print(big)
"""
"""
import random
a = []
c = 0
while True:
    b = random.randrange(1, 101)
    a.append(b)
    if a[c] == 100:
        break
    c += 1
print(a)
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

a = {'abc': 170, 'age': 100, 'value': 200, 'height': 180, 'height': 190}
print(a['abc'])
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

# 12일 수업---------------------------------------------
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
    if  num == 1:
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
def seven(n):
    a = n % 7
    if a > 3:
        ans = n - a + 7
    else:
        ans = n - a
    return ans


n = int(input())
print(seven(n))
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
        ogar.a ttacked(a)
        if ogar.hp <= 0:
            print("{} 사망".format(og ar.name))
            break
        else:
            print("{}가 {}를 {}의 공격력으로 공격했다.\n{}의 hp:{}\n{}의 hp:{}"
              .format(mc.name, ogar.name, a, mc.name, mc.hp, ogar.name, ogar.hp))
    elif select_skill == 2:
        if mc.mp > 0:
            a = m c.skill()
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
"""
f = open("/Users/cho/Desktop/test_new.txt",'r')
temp = f.readlines()

print(temp)
"""
# 9.26
"""
def plus():
    a = int(input())
    b = int(input())
    return a + b

def minus():
    a = int(input())
    b = int(input())
    return a - b

def mul(x, y):
    return x * y


print(mul(plus(), minus()))
"""
"""
a = int(input())
b = int(input())
temp = a
a = b
b = temp
print(a,b)
"""
"""
for line in lines:
    print(line)
"""
"""
for line in lines:
    print(line.split('\n')[0])
"""
"""
a = "hihihikbyebye"
b = a.split('k')
print(b)
"""
"""
f = open("test.txt", "r")
lines = f.readlines()
id = input("id:")
pwd = input("pwd:")
for line in lines:
    server_id = line.split(',')[0]
    server_pwd = line.split(',')[1].split('\n')[0]
    if id == server_id and pwd == server_pwd:
        print("로그인 완료")
        exit()
print("다시")
"""
"""
f = open("test.txt", "r")
lines = f.readlines()
id = input("id:")
pwd = input("pwd:")
flag = 0
for line in lines:
    server_id = line.split(',')[0]
    server_pwd = line.split(',')[1].split('\n')[0]
    if id == server_id and pwd == server_pwd:
        print("로그인 완료")
        flag=1
        break
if flag==0:
    print("다시")
"""
"""
f = open("test.txt","a")
fr = open("test.txt","r")
id = input("아이디를 입력하세요:")
pwd = input("비밀번호를 입력하세요:")
for line in lines:
    server_id = line.split(',')[0]
    server_pwd = line.split(',')[1].split('\n')[0]
    if id == server_id:
        print("이미 가입되어 있습니다.")
        exit()
f.write(id + ',' + pwd + '\n')
print("가입완료")
"""
"""
# 0 1 2
# 3 4 5
# 6 7 8
import random
def make_board():
    a = []
    for i in range(9):
        a.append("-")
    return a
board = make_board()
def see_board():
    for j in range(0,4,3):
        print(board[j]+"|"+board[j+1]+"|"+board[j+2])
        print("-----")
    print(board[6] + "|" + board[7] + "|" + board[8]+"\n")

x_or_o = input("x or o:")
if x_or_o == 'x':
    p1 = 'x'
    p2 = 'o'
else:
    p1 = 'o'
    p2 = 'x'
def set_p1():
    p1_choice = int(input("choice number 0~8:"))
    if board[p1_choice] == '-':
        board[p1_choice] = p1
    else:
        print("you can't. Choice other number:")
        set_p1()
    see_board()
def set_p2():
    p2_choice = random.randrange(0, 9)
    if board[p2_choice] == '-':
        board[p2_choice] = p2
    else:
        set_p2()
    see_board()
    
if p1 == 'x':
    set_p1()
    set_p2()
else:
    set_p2()
    set_p1()
"""
"""
f = open("test.txt","r")
import random

def make_board():
    b = []
    for i in range(9):
        b.append('-')
    return b

def show_board():
    for j in range(0, 7, 3):
        print(board[j] + '|' + board[j + 1] + '|' + board[j + 2])
    print('-----')


def set_p1():
    choice = int(input("choice number 0~8:"))
    if board[choice] == '-':
        board[choice] = p1
    else:
        print("you can't. Choice other number:")
        set_p1()

def set_p2():
    m = random.randrange(0, 9)
    if board[m] == '-':
        board[m] = p2
    else:
        set_p2()

def check_win(p):
    if board[0] == board[1] and board[1] == board[2] and board[0] == p:
        return True
    elif board[3] == board[4] and board[4] == board[5] and board[3] == p:
        return True
    elif board[6] == board[7] and board[7] == board[8] and board[6] == p:
        return True
    elif board[0] == board[3] and board[3] == board[6] and board[0] == p:
        return True
    elif board[1] == board[4] and board[4] == board[7] and board[1] == p:
        return True
    elif board[2] == board[5] and board[5] == board[8] and board[2] == p:
        return True
    elif board[0] == board[4] and board[4] == board[8] and board[0] == p:
        return True
    elif board[2] == board[4] and board[4] == board[6] and board[2] == p:
        return True

def check_draw():
    for i in board:
        if i != '-':
            continue
        else:
            return
    print("무승부")
    exit()
    
board = make_board()

x_or_o = input('x or o:').lower()
if x_or_o == 'x':
    p1 = 'x'
    p2 = 'O'
    turn = 0
else:
    p1 = 'O'
    p2 = 'X'
    turn = 1

for i in range(5):
    if turn == 0:
        print("player turn")
        set_p1()
        show_board()
        check = check_win(p1)
        if check:
            print("player win")
            break
        check_draw()
        turn = 1
    if turn == 1:
        print("com turn")
        set_p2()
        show_board()
        check = check_win(p2)
        if check:
            print("com win")
            break
        check_draw()
        turn = 0

# 추가 -> 로그인 & 회원가입

# type
# < ~ !=
# and, or
# for, while
# list => for i in list & for i in range(len(list)
"""
"""
from random import randrange
f = open("test.txt","a")
fr = open("test.txt","r")
lines = fr.readlines()
print(lines)
def login():
    id = input("id:")
    pwd = input("pwd:")
    for line in lines:
        server_id = line.split(',')[0]
        server_pwd = line.split(',')[1].split('\n')[0]
        if id == server_id and pwd == server_pwd:
            print("로그인 완료")
            return
    print("다시 로그인")
    login()

def m_id():
    id = input("아이디를 입력하세요:")
    pwd = input("비밀번호를 입력하세요:")
    for line in lines:
        server_id = line.split(',')[0]
        server_pwd = line.split(',')[1].split('\n')[0]
        if id == server_id:
            print("이미 가입되어 있습니다.")
            m_id()
            return
    f.write(id + ',' + pwd + '\n')
    print("가입완료")


def menu():
    choice = int(input("1.make id 2.login"))
    if choice == 1:
        m_id()
    elif choice == 2:
        login()

def m_board():
    a = []
    for i in range(9):
        a.append(' ')
    return a

board = m_board()

def p_board():
    for i in range(0, 7, 3):
        print(board[i] + '|' + board[i + 1] + '|' + board[i + 2])
    print()

menu()

print("game start!")
x_o = input("x or o").lower()
if x_o == 'x':
    p1 = 'x'
    p2 = 'o'
    turn = 0
else:
    p1 = 'o'
    p2 = 'x'
    turn = 1

def set_p1():
    p1_num = int(input("input 1~9:"))
    if board[p1_num - 1] == ' ':
        board[p1_num - 1] = p1
    else:
        print("put again")
        set_p1()

def set_p2():
    p2_num = randrange(1, 10)
    if board[p2_num - 1] == ' ':
        board[p2_num - 1] = p2
    else:
        set_p2()

def win():
    if board[0] == board[1] and board[1] == board[2] and board[0] != ' ':
        return True
    elif board[3] == board[4] and board[4] == board[5] and board[3] != ' ':
        return True
    elif board[6] == board[7] and board[7] == board[8] and board[6] != ' ':
        return True
    elif board[0] == board[3] and board[3] == board[6] and board[0] != ' ':
        return True
    elif board[1] == board[4] and board[4] == board[7] and board[1] != ' ':
        return True
    elif board[2] == board[5] and board[5] == board[8] and board[2] != ' ':
        return True
    elif board[0] == board[4] and board[4] == board[8] and board[0] != ' ':
        return True
    elif board[2] == board[4] and board[4] == board[6] and board[2] != ' ':
        return True

def draw():
    for i in board:
        if i != ' ':
            continue
        else:
            return
    print("draw")
    exit()

for i in range(5):
    if turn == 0:
        print("player turn")
        set_p1()
        p_board()
        if win():
            print("player win")
            break
        draw()
        turn = 1

    if turn == 1:
        print("com turn")
        set_p2()
        p_board()
        if win():
            print("com win")
            break
        draw()
        turn = 0
"""
"""
a = []
a.append(1)
print(a)
del a[0]
print(a)
"""
"""
#자료구조
#stack - FILO
#overflow - 다찼는데 넣으려고 하는 경우
#underflow - 아무것도 없는데 빼려고 할 경우
#cpu ram(프로그램이 돌아감) hd

def push(stack, a):
    #overflow 확인 코드
    #넣어주는 작업
    return stack
def pop(stack):
    #underflow 확인 코드
    #빼주는 작업
    #del stack[0]
    return stack
stack = []
max_v = 5
while True:
    check = int(input("1 is push, 2 is pop, 3 is exit"))
    if check == 1:
        push(stack, a)
        pass
    elif check == 2:
        pass
    elif check == 3:
        break
#pass에 코드 채워넣기
"""
"""
def push(stack, a):
    if len(stack) == max_v:
        print("overflow")
        return
    else:
        stack.append(a)
    #overflow 확인 코드
    #넣어주는 작업
    return stack
def pop(stack):
    if len(stack) == 0:
        print("underflow")
        return
    else:
        print("{} 삭제".format(stack[len(stack)-1]))
        del stack[len(stack)-1]
    #underflow 확인 코드
    #빼주는 작업 -> del stack[0]
    return stack
max_v = 5
list = []
while True:
    check = int(input("1 is push, 2 is pop, 3 is exit"))

    if check == 1:
        a = int(input("input num"))
        push(list, a)
    elif check == 2:
        pop(list)
    elif check == 3:
        print(list)
        break
#pass에 코드 채워넣기
"""
"""
#버블정렬
list = [3,5,1,2,7]
for j in range(len(list)):
    for i in range(len(list)-1):
        if list[i] > list[i + 1]:
            tmp = list[i]
            list[i] = list[i+1]
            list[i+1] = tmp
            #list[i],list[i+1] = list[i+1],list[i]
print(list)

#반복문은 두번정도 쓰는게 좋다
"""
"""
#pygame 설치

import pygame
pygame.init()#게임을 초기화 해주는 작업

def car(carImg, x, y):
    gameDisplay.blit(carImg, (x, y)) #이미지를 그려주는 역할 x, y좌표

display_width = 800 #display 너비선언
display_height = 800 #display 높이선언

gameDisplay = pygame.display.set_mode((display_width, display_height)) #display 설정
pygame.display.set_caption('race') #제목

black = (0, 0, 0)
white = (255, 255, 255)

clock = pygame.time.Clock()
crashed = False 
carImg = pygame.image.load("racecar.png") #자동차 이미지 경로

x = (display_width * 0.45)
y = (display_height * 0.8)

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #게임을 나가기
            crashed = True
    gameDisplay.fill(white) #배경 색
    car(carImg, x, y) #car 이미지를 x, y좌표에 그리기
    pygame.display.update() #바뀐
    clock.tick(60)

"""
"""
#pygame 설치
import pygame

pygame.init()#게임을 초기화 해주는 작업

def car(carImg, x, y):
    gameDisplay.blit(carImg, (x, y)) #이미지를 그려주는 역할 x, y좌표

display_width = 800 #display 너비선언
display_height = 800 #display 높이선언

gameDisplay = pygame.display.set_mode((display_width, display_height)) #display 설정
pygame.display.set_caption('race') #제목

black = (0, 0, 0)
white = (255, 255, 255)

clock = pygame.time.Clock()
crashed = False
carImg = pygame.image.load("racecar.png") #자동차 이미지 경로

x = (display_width * 0.45)
y = (display_height * 0.8)
x_change = 0
car_speed = 0

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #게임을 나가기
            crashed = True
        if event.type == pygame.KEYDOWN: #키를 눌렀을 때
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
                
        #위 아래 추가하기
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
    x += x_change
    gameDisplay.fill(white) #배경 색
    car(carImg, x, y) #car 이미지를 x, y좌표에 그리기

    pygame.display.update() #이미지 업데이트
    clock.tick(60)

"""
"""
#pygame 설치
import pygame

pygame.init()#게임을 초기화 해주는 작업

def car(carImg, x, y):
    gameDisplay.blit(carImg, (x, y)) #이미지를 그려주는 역할 x, y좌표

display_width = 800 #display 너비선언
display_height = 800 #display 높이선언

gameDisplay = pygame.display.set_mode((display_width, display_height)) #display 설정
pygame.display.set_caption('race') #제목

black = (0, 0, 0)
white = (255, 255, 255)

clock = pygame.time.Clock()
crashed = False
carImg = pygame.image.load("racecar.png") #자동차 이미지 경로

x = (display_width * 0.45)
y = (display_height * 0.8)
x_change = 0
y_change = 0
car_speed = 0

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #게임을 나가기
            crashed = True
        if event.type == pygame.KEYDOWN: #키를 눌렀을 때
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
            elif event.key == pygame.K_UP:
                y_change = -5
            elif event.key == pygame.K_DOWN:
                y_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                x_change = 0
                y_change = 0
    x += x_change
    y += y_change
    gameDisplay.fill(white) #배경 색
    car(carImg, x, y) #car 이미지를 x, y좌표에 그리기

    pygame.display.update() #이미지 업데이트
    clock.tick(60)
"""
"""
#queue

def enqueue(queue, a):
    return queue

def dequeue(queue):
    return queue

queue = []
max_v = 5
while True:
    a = int(input("1 is enqueue, 2 is dequeue, 3 is out :"))
    if a == 1:
        a = int(input("input num"))
        enqueue(queue, a)
    elif a == 2:
        dequeue(queue)
    else:
        print("out")
        break

"""
"""
# queue
def enqueue(queue, a):
    if len(queue) == max_v:
        print("overflow")
        return
    else:
        queue.append(a)
    return queue

def dequeue(queue):
    if len(queue) == 0:
        print("underflow")
        return
    else:
        print("{} is delete".format(queue[0]))
        del queue[0]
    return queue

queue = []
max_v = 5
while True:
    a = int(input("1 is enqueue, 2 is dequeue, 3 is out :"))

    if a == 1:
        a = int(input("input num"))
        enqueue(queue, a)
    elif a == 2:
        dequeue(queue)
    else:
        print(queue)
        print("out")
        break

queue = [1,2,3,4,5]
print(a[0])
"""
"""
#선택정렬
#1. 가장 작은 수 출력
import random
a = []

for i in range(10):
    a.append(random.randrange(1, 200))

mini = 0
for i in range(1, len(a)):
    if a[mini] > a[i]:
        mini = i
print(a)
print(mini, a[mini])
"""
"""
import random
a = []
for i in range(10):
    a.append(random.randrange(1, 200))
print(a)
for i in range(len(a)-1):#기준점
    mini = i
    for j in range(i+1, len(a)):#최소값
        if a[j] < a[mini]:
            mini = j
    tmp = a[i]
    a[i] = a[mini]
    a[mini] = tmp
    #a[i], a[mini] = a[mini], a[i]
    print(a)
"""
"""
#pygame 설치
import pygame

pygame.init()#게임을 초기화 해주는 작업

def car(carImg, x, y):
    gameDisplay.blit(carImg, (x, y)) #이미지를 그려주는 역할 x, y좌표

display_width = 800 #display 너비선언
display_height = 800 #display 높이선언

gameDisplay = pygame.display.set_mode((display_width, display_height)) #display 설정
pygame.display.set_caption('race') #제목

black = (0, 0, 0)
white = (255, 255, 255)

clock = pygame.time.Clock()
carImg = pygame.image.load("racecar.png") #자동차 이미지 경로
car_width = 79

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #게임을 나가기
                crashed = True
            if event.type == pygame.KEYDOWN: #키를 눌렀을 때
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        x += x_change
        gameDisplay.fill(white) #배경 색
        car(carImg, x, y) #car 이미지를 x, y좌표에 그리기

        if x > display_width - car_width or x < 0:
            crashed = True

        pygame.display.update() #이미지 업데이트
        clock.tick(60)

game_loop()
"""
"""
#pygame 설치
import pygame

pygame.init()#게임을 초기화 해주는 작업

def car(carImg, x, y):
    gameDisplay.blit(carImg, (x, y)) #이미지를 그려주는 역할 x, y좌표

display_width = 800 #display 너비선언
display_height = 800 #display 높이선언

gameDisplay = pygame.display.set_mode((display_width, display_height)) #display 설정
pygame.display.set_caption('race') #제목

black = (0, 0, 0)
white = (255, 255, 255)

clock = pygame.time.Clock()
carImg = pygame.image.load("racecar.png") #자동차 이미지 경로
car_height = 148
car_width = 79

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    y_change = 0
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #게임을 나가기
                crashed = True
            if event.type == pygame.KEYDOWN: #키를 눌렀을 때
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    x_change = 0
                    y_change = 0
        x += x_change
        y += y_change
        gameDisplay.fill(white) #배경 색
        car(carImg, x, y) #car 이미지를 x, y좌표에 그리기

        if (x > display_width - car_width or x < 0) or (y > display_height - car_height or y < 0):
            crashed = True

        pygame.display.update() #이미지 업데이트
        clock.tick(60)

game_loop()
"""

"""
#데이터 타입
# int, float, str, bool, list, dict

#짝수 구하기
#for문 별찍기, 역으로 찍기
#while문으로 별찍기
#리스트를 이용해서 최대값 찾기

"""
"""
a = int(input("input num:"))
if a % 2 == 0:
    print("짝수")
else:
    print("홀수")
"""
"""
for i in range(1, 6):
    print("{}".format('*' * i))
for j in range(5, -1, -1):
    print("{}".format('*' * j))
"""
"""
i = 1
while i < 6:
    print("{}".format('*' * i))
    i += 1
"""
"""
a = [1, 6, 2, 8, 3, 7]
big = 0
for i in range(len(a)):
    if a[big] < a[i]:
        big = i
print(big, a[big])
"""
"""
import random
def make_list(a):
    for i in range(10):
        a.append(random.randrange(1, 200))
    return a

def action_find_max_value(a):
    b = a[0]
    for i in range(len(a)):
        if a[i] > b:
            b = a[i]
    return b

def output_value(b):
    print("Max value {}".format(b))

a = []
not_sort_list = make_list(a)
max_value = action_find_max_value(not_sort_list)
output_value(max_value)
"""
"""
import random
a = []

for i in range(10):
    a.append(random.randrange(1,100))
print(a)

for i in range(1,len(a)):
    for j in range(i,0,-1):
        if a[j-1] > a[j]:
            a[j], a[j-1] = a[j-1], a[j]
print(a)
"""
"""
import random
def make_list(a):
    for i in range(10):
        a.append(random.randrange(1, 100))
    return a

def insertsort(a):
    for i in range(1, len(a)):
        for j in range(i, 0, -1):
            if a[j - 1] > a[j]:
                a[j], a[j - 1] = a[j - 1], a[j]

def output_list(b):
    print("{}".format(b))

a = []
make_list(a)
output_list(a)
insertsort(a)
output_list(a)
"""
#pygame 설치
import pygame

pygame.init()#게임을 초기화 해주는 작업

display_width = 800 #display 너비선언
display_height = 800 #display 높이선언

gameDisplay = pygame.display.set_mode((display_width, display_height)) #display 설정
pygame.display.set_caption('race') #제목

black = (0, 0, 0)
white = (255, 255, 255)

clock = pygame.time.Clock()
carImg = pygame.image.load("racecar.png") #자동차 이미지 경로
car_height = 148
car_width = 79

def car(carImg, x, y):
    gameDisplay.blit(carImg, (x, y)) #이미지를 그려주는 역할 x, y좌표

def text_object(text, font): #폰트를 render(그리는)하는 역할
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)#폰트 정해주기
    TextSurf, TextRect = text_object(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2)) #중앙에 위치
    gameDisplay.blit(TextSurf, TextRect) #화면에 그려주기

    pygame.display.update()

def crash():
    message_display('You Crashed')

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    y_change = 0
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #게임을 나가기
                crashed = True
            if event.type == pygame.KEYDOWN: #키를 눌렀을 때
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    x_change = 0
                    y_change = 0
        x += x_change
        y += y_change
        gameDisplay.fill(white) #배경 색
        car(carImg, x, y) #car 이미지를 x, y좌표에 그리기

        if (x > display_width - car_width or x < 0) or (y > display_height - car_height or y < 0):
            crashed = True
            crash()

        pygame.display.update() #이미지 업데이트
        clock.tick(60)

game_loop()
pygame.quit()
quit()
