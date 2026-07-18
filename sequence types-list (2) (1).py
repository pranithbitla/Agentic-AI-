#Sequence types-->Mutable,Indexed,Ordered and Heterogenous Collection
#Nested Lists-->list inside another lists
data=['codegnan',35,4.56,['python','java','AAI','DA'],100,65]
print(data)
print(len(data))
#we need to access ineer list as below
print(data[3])
#now i want to get 'python' and 'java' from above list
a=data[3][:2]
print(a)
b=data[3][2:]
print(b)
#get in python only 'pyt'
c=data[3][0][:3]
print(c)
#get in java only 'ava'
d=data[3][1][1:]
print(d)
#get the output as ['python','AAI']
e=data[3][::2]
print(e)
#get the output as[35,['python,'java','AAI','DA'],45]
f=data[1::2]
print(f)

#lists are mutable -->we can insert/remove elements
data=['codegnan',35,4.56,['python','java','AAI','DA'],100,65]
#using indexing and slicing->change
#35-->45
data[1]=45
print(data)
print(len(data))
data[2]=['agents','prompt','rag']
print(data)
print(len(data))
data[3][1]='rag'
print(data)

#indexing will never change the length of collection
#now we will use slicing
data=['codegnan',35,4.56,['python','java','AAI','DA'],100,65]
data[1:3]=['java','DSA']
print(data)
data[1:3]=['RAG','MCP','Agents','Lora','grt','sonet']
print(data)

data=['codegnan',35,4.56,['python','java','AAI','DA'],100,65]
print(data)
data[3][1::2]=['rag','mcp']
print(data)
#indexing,slicing,striding can insert elements but we loose our oringinal data
#append(),extend(),insert()
#append()-->inserts only single object at the end of list/empty list we can start assign
details=['mani',22,'codegnan']
data=['codegnan',35,4.56,['python','java','AAI','DA'],100,65]
print(len(details))
details.append(34)
print(details)
details.append('Agentic AI')
print(details)
details.append(data)
print(details)
print(details.append('mani'))#it returns None a swe need print only list

#extend()-->inserts multiple objects(iterable)to the end of the list
details=['mani',22,'codegnan']
details.extend((34,45))
print(details)
details.extend('codegnan')
print(details)
detalis.extend(['codegnan'])
print(details)

#insert()-->insert object before index
details=['mani',22,'codegnan']
details.insert(1,'python')
print(details)
print(len(details))
details.insert(5,'agents')
print(details)
details.insert(6,['temperature','agents'])
print(details)
details.insert(-1,'mani')
print(details)
details.insert(-2,['python','java'])
print(details)
details[-1].append('mani')
print(details)
details[-1].extend('python')
print(details)
details[-1].insert(1,'claude')
print(details)

#remove(),pop(),clear()
details=['mani',22,'codegnan','agents','MCP']
print(details)
#pop()removes by default last index if not given
details.pop()
print(details)
details.pop(1)
print(details)
#remove()
details=['mani',22,'codegnan','agents','MCP']
details.remove('agents')
print(details)
details.remove()#it returns the error
print(details)
#clear()
details.clear()#removes all objects in the collection and reyurns empty list
print(details)
#to extract group of objects-->del
details=['mani',22,'codegnan','agents','MCP']
del details[2:4]
print(details)

del details#remove complete list

#index(),count(),copy(),sort(),reverse()
detalis.extend(['agents','rag'])
print(details)
print(details.index('agents'))
print(details.index('agents',4))
print(details.count('agents'))
#details.sort()
details.pop(1)
print(details)
details.sort()
print(details)#alphabetical order as we have strings in it
b=[12,-98,23,78,2]
b.sort()
print(b)
b.sort(reverse=True)#this becomes descending order
print(b)
b.reverse()
print(b)
#copy()-->creates a shallow copy of list
c=b.copy()
print(c)
c[2]='codegnan'
print(c)
print(b)
#create nested list and observe copy() in it
data=['mani',22,'agents','MCP',['java','python','RAG'],'AII','manimala']
d=data.copy()
print(d)
print(data)
d[3]='codegnan'
print(d)
d[4][1]='machine learning'
print(d)





































































































































































































