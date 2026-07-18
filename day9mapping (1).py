'''datatypes-->numeric,boolean,sequence datatypes(str,lists,tuples),aet datatype(sets frozen sets),mapping(dictionary)'''
#dictionary-->collection of key-value pairs,mutable,ordered..-->{},dict()
'''details={}
print(details)
print(type(details))
details={'Name':'codegnan','place':'hyd','age':7}
print(details)
print(len(details))

#accessing keys
print(details['Name'])
print(details['age'])
#keys must be uniqe in adictionary
data={'age':25,'name':'codegnan','age':26}
print(data)#here recent update value of age will be taken
#in dictionary we index by using keys'''

#create dictionaries using other datatypes
students_data={'ids':[22,32,45,34],
               'names':['mani','vasanthi','prassana','akshitha'],
               'place':['hyd','vjwda'],
               'gender':['male','female']}
'''print(len(students_data))
print(students_data.keys())#return key from dictionary
print(students_data['names'])
print(students_data['ids'])
print(students_data.values())
students_data['coures']=['PFS','JFS','AAA','DA']
print(students_data)
print(type(students_data))
print(type(students_data['ids']))
#now if we want to insert 3 more uniqe ids
students_data['ids'].extend([56,47,89])
print(students_data)
students_data['names'].insert(1,'ashok')
print(students_data['names'])
#we want to insert new place
students_data['place'].append('vizag')
print(students_data)
#print(students_data['coures'][1::2])
#students_data['ids'].delete[2:3]
#print(students_data)
(students_data['names'].sort())
print(students_data)
#keys(),values(),items()
print(students_data.items())#returns key value pairs as tupls'''
print(students_data)
#get method will return value if key is existing,else default-->none
print(students_data.get('branch'))
print(students_data.get('branch','CSE'))
#print(students_data['branch'])#raiser keyerror as we dont have branch
#setdefault->update the dictionary if key is no exsting with in default none
print(students_data.setdefault('ids'))
#students_data.setdefault('branch')
students_data.setdefault('branch',['CSE','CSD','ECE','EEE'])
print(students_data)
#update(),pop(),popitem(),clear()
students_data.update({'fees':[456,234],'marks':[25,45,65]})
print(students_data)
print(students_data.pop('marks'))#we need to metion the key which we want to remove
print(students_data)
print(students_data.popitem())#comes from the last
print(students_data)
print(students_data.copy())
print(students_data)
#print(students_data.clear())
#print(students_data)
#fromkeys()will create a new dictionary by accpecting each object in the given iterable as key whereas value is set to none
#key where as value is set to none
ids=[23,47,65]
#to convert above list to dictionary
d=dict.fromkeys(ids)#each value will be assigned as none we can modify accordingly
print(d)
d[23]='random'
print(d)
#print(d+d)#not possible for sets and dicts
#membership-->in,not in (keys)
print(23 in d)#returns True as we have 23 as key


#nestend dictionaries
#take-->creat a nestend dictionary with own scenario




































































































































