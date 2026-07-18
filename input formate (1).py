#input formating
#String input
name=input()
print(name)
name=input('Enter the name:')
print(name)
print(type(name))
#Integer input-->int()-->age,value,quantity
age=int(input("enter the age:"))
print(age)
print(type(age))
#float
price=float(input("enter the price:"))
print(price)
print(type(price))
#costprice and sellingprice-->profit and loss
costprice=float(input("enter the costprice:"))
sellingprice=float(input("enter the sellingprice:")) 
print(costprice-sellingprice)
#multiple string inputs
name,place=input("Enter the details:").split()
print(name)
print(place)
name,place=input("Enter the details:").split(',')
print(name)
print(place)
#multiple intger values
a,b=map(int,input("enter the values:").split(','))
print(a)
print(b)
#float
discount,weight=map(float,input("enter the values:").split(','))
print(discount)
print(weight)
#list of strings
data=input("enter the details:").split(',')
print(data)
#list of integers
marks=list(map(int,input("enter the marks:").split(',')))
print(marks)
#float
marks=list(map(float,input("enter the marks:").split(',')))
print(marks)
#tuple
marks=list(map(tuple,input("enter the marks:").split(',')))
print(marks)
#output formating
print(25)
print(15,23.4,'mani')
#sepatator --> for separating the value
print(2026,7,9)
print(25,3.2,2,sep='/')
#above case we want as date format
print(2026,7,9,sep=',')
print(2026,7,9,sep='/')
#end argument in print()-->\n-->new line
name='mani'
place='hyd'
course='AAA'
print(name,course)
print(name,place,course)
print(name,place,end=' ')
print(course)
print(place,name,end='\t')#\t-->tab space
print(course)
#using commas
name='mani'
place='hyd'
print("name :",name,"place :",place)
print("name :",name,"place :",place,sep=',')
#old style formatting-->%d,%s,%f
age=22;place='hyd'
print("age is %d and place is %s"%(age,place))
price=458.34
print("item price is %f"%(price))
print("item price is %.f"%(price))
print("item price is %.1f"%(price))
print("item price is %.2f"%(price))
#using str().format()method
name,course='mani','python'
print("{} is enrolled in {} course".format(name,course))
#f-string notation-->most recommended
name,course='mani','python'
print(f'{name} is enrolled in {course}')


































