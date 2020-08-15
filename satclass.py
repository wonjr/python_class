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
if a % 2 == 1:
    print("odd")
"""
"""
a = int(input())

if a == 0:
    print("zero")
elif a == 1:
    print("one")
else:
    print("etc")
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

b = int(input())
a = []
for i in range(1, 101):
    a.append(i)
low = a[0]
high = a[99]
cnt = 0
while low < high:
    mid = (low + high)//2
    if b == mid:
        print(a[b-1], cnt)
        break
    elif b < mid:
        high = mid - 1
        cnt += 1
    else:
        low = mid + 1
        cnt += 1


