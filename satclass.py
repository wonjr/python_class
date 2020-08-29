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
a = input()
flag = 0
for i in range(len(a)):
    if a[i] != a[len(a)-1-i]:
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

#한번 값을 한단하면 바꿀 수 없다. list와 비슷하지만 메모리 측면에서 더 효율적으로 사용할 수도 있다.
"""

"""
a = [1,"a",[1,"a"]]
a = [[1,2,3],[4,5,6]]
print(a[0])
print(a[0][2])
"""
""" = {}
a = dict()

a = {'kkk': 170, 'age':100, 'value': 200, 'height' : 180, 'height': 190}
print(a['kkk'])
a.keys()
print(a['height'])
"""

def add_test(x, y):
    #print(x + y)
    return x + y
#add_test(1,3)
print(add_test(1,3))
c = add_test(1,3)
print(c)
