name = input('Enter your 1st name=')

while name == '':
    print('This cred is not valid')
    print('Please try again')
    name = input('Enter your 1st name=')

else:
    print('First Name=',name)

lname = input('Enter your last name=')

while lname=='':
    print('This cred is invalid')
    print('try again')
    lname = input('Enter your last name=')

else:
    print("Last name",lname)
    print('Full name:',name,lname)


#Another code

name = input('Enter your 1st name=')

if name == '':
    print('This cred is not valid')
    print('Please try again')
    name = input('Enter your 1st name=')

else:
    print('First Name=',name)

lname = input('Enter your last name=')

if lname=='':
    print('This cred is invalid')
    print('try again')
    lname = input('Enter your last name=')

else:
    print("Last name",lname)
    print('Full name:',name,lname)

#Another code

i=0

while i<5:
    print("the value of i is:",i)
    i+=1 #this plus means add 1 in every next code
print("Finished while loop")

#Another code

i=0

while i>5:
    print("the value of i is:",i)
    i-=1 #this - means subt 1 in every next code
print("Finished while loop")


#Another code


num = 1
sum = 0
print("Enter a Number. Please enter (0) to exit")
while num !=0:
    num = float(input("Number?"))
    sum=sum+num
    print(sum)



