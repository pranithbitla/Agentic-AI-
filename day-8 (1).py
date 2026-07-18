#tuples--> tuples are an immutable,ordered,indexed sequence type,we use()for delaration
#indexed sequence type,we use()for delaration
data=1,24,5
print(data)
print(type(data))

#nested tuples and also have lists inside it
details=('codegan',32,(2,4,5),'mani',[12,45,'agents','rag'])
print(details)
print(len(details))
print(details[2])
print(details[4][2])
print(details[:1])
print(details[0])
details[0]=details[0].replace('n','f')#tuples are immutable we cant modify it
print(details)
details[4][2]=details[4][2].replace('a','A')#here we are using lists so its mutable
print(details)
print(details[1::4])
print(details[::3])
#practics indexing,slicing,striding

details[4].pop(2)
print(details)
print(type(details[4]))
details[4].remove('agents')
print(details)

#operations on tuples-->indexing,slicing,membership,concatenation,repetition
age=22,21,32,25
ids=231,342,213
print(age+ids)#merging
print(age*2)
print(22 in age)#membership

#len(),type(),min(),max()
age=(25,34,22,67)
print(max(age))
print(min(age))
print(tuple(sorted(age)))#Typecasting
#index(),count()
details=('mani','python','java',32,45,65.8)
print(details)
print(details.index(32))
print(details.count(32))

#tuples-->list..(typecasting)
details=list(details)
print(details)
print(tuple(details))

data='codegnan'
print(tuple(data))
print(list(data))

#set datatypes-->sets,frozen sets
#sets-->a set is a unique,mutable collection-->set()
a={}#by dfault it is empty dictionary
b=set()
print(type(a))
print(type(b))
ids={123,124,122,164,345,122,124}
print(ids)
print(len(ids))

#as set is mutable we can insert,remove elements into a set
data={23,4.5,'codegnan',{12,34,5}}#a set cannot contain a ilst and a set inside it
print(data)
#as set is mutable we can insert,remove elements into a set

ids={123,124,122,164,345,122,124}
print(ids)
ids.add(234)
print(ids)
ids.add('agents')
ids.update(('python','java',164))
print(ids)

#remove elements from a set-->discard(),remove(),clear(),pop()
ids={123,124,122,164,345,122,124}
print(ids)
ids.discard(124)
print(ids)
ids.remove(164)
print(ids)
#ids.remove(124)#return keyerror
#print(ids.discard(164))#discard will avoid error
print(ids.pop())#remove an dreturn an ability elemt from a set
print(ids.pop())
print(ids.pop())
#print(ids.pop())#empty set
#clear() removes all elements and returns an empty collection
print(ids.clear())
print(ids)#return empty set

#union,intersection,difference,symmetric difference,subset,supersets

ids={123,124,122,164,345,122,124}
ages={22,35,45,76,123}
print(ages)
d=ids.union(ages)
print(d)
g=ids.update(ages)
print(g)
e=ids.intersection(ages)
print(e)
f=ids.intersection_update(ages)
print(f)#picks common elements from both sets and updates the first set 
h=ids.difference(ages)
print(h)#it removes common elements and returns remaining elements from first set
#|(union),&(intersection),-(difference),^(symmetric difference)
g=ages-ids
print(g)
h=ages|ids
print(h)
i=ages^ids
print(i)#removes common elements and return elements from all
a={1,2,3}
b={1,2,3,4,5}
print(a.issubset(a))
print(b.issuperset(b))
print(a.isdisjoint(b))

#frozenset-->immutable set
ids={123,124,122,164,345,122,124}
data=frozenset(ids)
print(data)
print(type(data))
#we cannot insert/remove elements but mathematical operations are possible
details=frozenset([34,54,67,56,87])
print(details)
print(min(details))
print(max(details))
print(sorted(details))












































































































































