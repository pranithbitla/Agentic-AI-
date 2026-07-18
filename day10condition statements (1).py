#control statements-->these are the statements which control teh flow of execution of the program
#-->conditional statements(if,else,elif)
#-->repetition statements(loops)-->for,while,nested loops(patterns)
#-->jumping statements-->break,continue,pass,assert

'''#ifstatement:
if<condition>:
    statement(s)....
    ......
    .....

#validate the price..
#money=100
money=int(input("enter the billing value:"))
if money <=100:
    print(f'now you are eligible to get your items')#dynamic input
print("check again")
students=['ram','akash','abhi','mani']
name=input("enter the student name:").lower()
if name in students:
    marks=50
    grade='A'
    print(f'{name} has secured {marks} marks and {grade} Grade')'''
#if-else statements:
'''syntax:
if condition:
    statement(s)
    .......
    ....
else:
    statement(s)...
    ....
#vote Eligibility
#user will enter his/her age-->give voter eligibility
age=int(input("enter the age:"))
if age>=18:
    print(f'you are eligible to vote,so use it properly')
    print("your age is{} years,eligible".format(age))
else:
    print("you are not eligible to vote")
    print(f'you need to wait for{18-age}years to get vote right')

if-elif-else statement(s)...
.....

syntax:
if condition1:
    statemnt(s)...
    ...
elif condition2:
    statemnt(s)...
    ...
    ....
else:
    statement(s)...
    ....'''
#for same above vote elibility we rewrite the logic
age=int(input("enter the age:"))
if age>=18:
    print(f'you are eligible to vote,so use it properly')
    print("your age is{} years,eligible".format(age))
elif age==0 or age<0:
    print(f'enter only +ve values')
else:
    print("you are not eligible to vote")
    print(f'you need to wait for{18-age}years to get vote right')
    




































































































































