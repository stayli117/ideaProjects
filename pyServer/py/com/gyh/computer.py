# -*- coding: UTF-8 -*

# 运算符

a=10
b=20
c=0

print a+b

print "1 - c 的值为：", c

c = a - b
print "2 - c 的值为：", c

c= a*0.1/b

print 'a/b 的值为：',c

c= a/float(b)
print 'a/float(b)',c

if (a<b):
    a=a-b
    print(a)



print '-----------逻辑运算符-----------'
a = 10
b = 20

if ( a and b ):
    print "1 - 变量 a 和 b 都为 true"
else:
    print "1 - 变量 a 和 b 有一个不为 true"

if ( a or b ):
    print "2 - 变量 a 和 b 都为 true，或其中一个变量为 true"
else:
    print "2 - 变量 a 和 b 都不为 true"

# 修改变量 a 的值
a = 0
if(a):
    print('a 为 true')
else:
    print('a 不为 true')

if ( a and b ):
    print "3 - 变量 a 和 b 都为 true"
else:
    print "3 - 变量 a 和 b 有一个不为 true"

if ( a or b ):
    print "4 - 变量 a 和 b 都为 true，或其中一个变量为 true"
else:
    print "4 - 变量 a 和 b 都不为 true"

if not( a and b ):
    print "5 - 变量 a 和 b 都为 false，或其中一个变量为 false"
else:
    print "5 - 变量 a 和 b 都为 true"


print '-----------成员运算符-----------'

a = 10
b = 20
list = [1, 2, 3, 4, 5 ];

if ( a in list ):
    print "1 - 变量 a 在给定的列表中 list 中"
else:
    print "1 - 变量 a 不在给定的列表中 list 中"

if ( b not in list ):
    print "2 - 变量 b 不在给定的列表中 list 中"
else:
    print "2 - 变量 b 在给定的列表中 list 中"

# 修改变量 a 的值
a = 2
if ( a in list ):
    print "3 - 变量 a 在给定的列表中 list 中"
else:
    print "3 - 变量 a 不在给定的列表中 list 中"


print '-----------身份运算符-----------'

print 'is 与 == 区别：is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。'
a = 20
b = 20

if ( a is b ):
    print "1 - a 和 b 有相同的标识"
else:
    print "1 - a 和 b 没有相同的标识"

if ( a is not b ):
    print "2 - a 和 b 没有相同的标识"
else:
    print "2 - a 和 b 有相同的标识"

# 修改变量 b 的值
b = 30
if ( a is b ):
    print "3 - a 和 b 有相同的标识"
else:
    print "3 - a 和 b 没有相同的标识"

if ( a is not b ):
    print "4 - a 和 b 没有相同的标识"
else:
    print "4 - a 和 b 有相同的标识"