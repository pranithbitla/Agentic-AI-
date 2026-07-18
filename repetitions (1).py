#repetitions -->we use * operator
data='agent'
print(data*3)
#membreship-->in,not in
print('code' in 'codegnan')
print('agent' not in 'generatiive AI')

#indexing-->we can access position of an object in a string,we use[]to get the index of an object,it starts with 0 and endsat len(obj)-1
name='codegnan'#-->start with 0 count
print(len(name))#--> return 8# when there is len the count start with 1
print(name[0])#return first character
print(name[6])
print(name[23])#index error
print('agent'[2])
#negative indexing-->start from last--> -1
name="codegnan"
print(name[-1])# return last character
print(name[-4])
print(name[4])

name='agentic ai course'
print(name[10])
print(name[-5])
print(name[7])
print(name[25])

#stirng are immutable
name="codegnan"
name[5]='p' #item assignment is not possible
print(name)

#slicing-->Accessing group of characters-->[started:end] start will be incleded,end will be excluded
name="codegnan"
print(name[:])
print(name[1:])#includins starting
print(name[1:5])#both start and end
print(name[:5])#only end
print(name[4:])
print(name[4:25])#even though end is out of range it return till end of string 
print(name[5:1])#not at all possible,as in positive slicing we can access only from lower index to higher index
name='codegnan'
print(name[-5])
print(name[-5:])
print(name[-5:-1])#reminder lower to higher
print(name[-1:-5])#return empty string
print(name[:-8])#return empty string
print(name[-8:])#return complete string
print(name[:-7])

#[::]-->[start:end:step]
name='codegnan'
print(name)
b=name[::]
print(b)
print(b[::1])
print(b[::2])
print(b[1:7:3])
print(b[2:9:5])
print(b[1::4])
print(b[:4:5])

#negitive
name='codegana'
print(name)
print(name[::-1])#prints in reverse order
print(name[::-2])
print(name[::-6])
print(name[-8:-1:])#return complete excluding last character
print(name[-8:-1:-2])#return empty string as no possibilites
print(name[-8:-1:2])
print(name[1:7:-1])#return empty string

#build-in functions-->len(),type(),min(),max(),ord(),chr()
place='hyderbad'
print(len(place))
print(type(place))
print(min(place))#return 'H' as per ASCII values
print(max(place))
print(ord('A'))#return ASCII value of given character
print(chr(97))#return specific character as per ASCII value

#methods(functions) on strings
#lower(),upper(),title(),capitalize(),swapcase()
#case conversions-->converting from one case to another
course="Agenti ai"
print(course)
print(course.lower())#convert to lower case
print(course.upper())#convert to upper case
print(course.swapcase())
print(course.title())#first letter of every word will be capitalized
print(course.capitalize())#first letter will be capitalized

































