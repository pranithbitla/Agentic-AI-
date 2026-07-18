#printMembership operatores
fruits=['apple','orange','banana']
print('apple' in fruits)
print(45 in fruits)
print(45 not in fruits)
print('codegnan' in 'code')

#Identify operations -->id-->is,is not-->boolen value
a=[1,2,3,4]
b=[1,2,3,4]
print(a==b)
print(a is b)
print(id(a))
print(id(b))
c=a
print(c)
print(a is c)
print(c==a)
print(id(a))
print(id(c))
print(c is b)

#logical operators-->and,or,not-->boolen value
a=14;b=23
c=a>b and b>a
print(c)
c=a<b or b<a
print(c)
e=b<c or a in [12,13,14]
print(e)
print(not(true))

#bitwise operations
print(5&4)
print(5^7)
print(4|7)
print(3<<4)
print(4>>5)


