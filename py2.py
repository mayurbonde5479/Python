# Q no 1

'''def add():
    print(" printing 1")
def modify():
    print(" printing 2")
def delete():
    print(" printing 3")
a = int(input())
match a:
    case 1: add()
    case 2: modify()
    case 3: delete()
    case _: print("nothing")
'''

# Q no 2

'''
def square(num):
    return num*num

a = int(input())

print(square(a))
'''

# Q no 3:

'''
def disply(var1,var2,var3):
    print(var1,var2,var3)

disply(20,"mayur",'M')
'''

# Q no 4:

'''
def myfun1():
    print("printing myfun1")
def myfun2():
    myfun1()
    print("printing myfun2")
myfun2()
'''

# Q no 5:

'''
def define():
    return 1
def define1():
    return 0

a  = int(input())

if a > 0:
    print(define())
elif a < 0:
    print(define1())
else:
    print(define1())
'''

# Q no 6:

'''
a = input()
if a.isalpha():
    if a.isupper():
        print("Uppercase")
    else:
        print("Lowercase")
else:
    print("not alphabet")   
'''

# Q no 7:

'''
a = str(input())
b = a.swapcase()
print(b)
'''

# Q no 8:

'''
a = str(input())
b = a.__len__()
if 3 <= b <= 5 :
    print("yes it is acceptable")
else :
    print("give valid input")
'''

# Q no 9:

'''
print("Enter n")
n = int(input())
def sum():
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    return sum
b = print(sum())
'''
