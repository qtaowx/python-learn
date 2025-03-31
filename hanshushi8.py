# 8.1 高阶函数
#变量可以指向函数
f = abs
print(f) #<built-in function abs>
print(f(-19))

#函数名也是变量
abs = 10
#abs(-10) #TypeError: 'int' object is not callable

# 传入函数
def add(x,y,f):
    return f(x)+f(y)

print(add(-5,6,hex))

# map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
def f(x):
    return x*x
r = map(f,[1,2,3,4,5,6,7,8,9])
print(list(r))

# 把list所有数字转为字符串
print(list(map(str,[1,2,3,4,5,6,7,8])))

# reduce():这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
from functools import reduce
# 对一个序列求和
def add(x, y):
    return x + y
print(reduce(add,[1,3,5,7,9]))

def fn(x,y):
    return x * 10 + y
print(reduce(fn,[1,3,5,7,9]))

# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
def normalize(name):
    return name[0].upper()+name[1:].lower()
    # return name.capitalize()
    
print(list(map(normalize,['adam', 'LISA', 'barT'])))

# 请编写一个prod()函数，可以接受一个list并利用reduce()求积
def fn2(x,y):
    return x * y
def prod(L):
    return reduce(fn2,L)
print(prod([3, 5, 7, 9]))

# filter()
def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

# 把一个序列中的空字符串删掉
def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty,['A', '', 'B', None, 'C', '  '])))

# 回数是指从左向右读和从右向左读都是一样的数, 请利用filter()筛选出回数
def fn3(n):
    return str(n) == str(n)[::-1] # 直接转换成字符串与之倒序排列进行比较

print(list(filter(fn3, ['abc', '123', 'hello', '12321', 'aa', '1111'])))
print(list(filter(fn3, range(1,200))))

# sorted()
print(sorted([35,5,-12,9,-21]))
# 给sorted传入key函数，即可实现忽略大小写的排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))

# 用一组tuple表示学生名字和成绩
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 请用sorted()对上述列表分别按名字排序
def by_name(value):
    return value[0].lower()
print(sorted(L,key=by_name))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 再按成绩从高到低排序
def by_score(value):
    return value[1]

print(sorted(L, key=by_score, reverse=True))

# 8.2 返回函数
