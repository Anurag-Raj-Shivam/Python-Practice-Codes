a=10*10
b=11+19
c=10/3
d=100-20
print(a)
print(b)
print(c)
print(d)


#it will straight answer if you run
x=100
y=10
print(x+y)


#it will show the process how its going on

x=50
y=50
print("{}*{}={}".format(x,y,x*y))


#it will show the process how its going on

x=50
y=50
print("{0}*{1}={2}".format(x,y,x*y))

#type of spaces
print("Hello"," ","world")     #" " this we use to create space

print("Hello","World", sep="....-----")    #sep= (seprater)


#use of %

name="Raj"
print("Hello %s" % name)       #%s we used to replcae %name
age=20
print("hello %s ! how are you and are you %d years old" %(name,age))

print("hello %.2s ! how are you and are you %d years old" %(name,age))  #. with number before to represent how much letters i want from the value

#use of % with . and all 3 are same
name = "Raj"
x = 120
y = 100

print(f"Hello {name}, how are you? One day you borrowed Rs {x} and 2nd day you took Rs {y}, so now you have to return me {x}+{y}={x + y}")

name = "Raj"
x = 120
y = 100

print("Hello {}, how are you? One day you borrowed Rs {} and 2nd day you took Rs {}, so now you have to return me {}+{}={}".format(name, x, y, x, y, x + y))

#this is the oldest format using %
name="Raj"
x=120
y=100

print("Hello %s, How are you? One day you borrowed Rs %d and 2nd day you took Rs %d, so now you have to return me" " {}+{}={}".format(x,y,x+y) %(name,x,y))

#another

x=50
y=10
print("{0}*{1}={2}".format(x,y,x*y))


#just for try

name1= "Santa"
name2="Banta"
name3="Ghanta"
x=15
y=25
z=35

print(f"Hello my name is {name1} and my brother's name is {name2}. My age is {x} years old and my brother's age is {y} years old. combining me and my brother our father named {name3}'s age is {z}years old ")

name1= "Santa"
name2="Banta"
name3="Ghanta"
x=15
y=25
z=35

print(f"Hello my name is %s and my brother's name is %s. My age is %d years old and my brother's age is %d years old. combining me and my brother our father named %s's age is %d years old " %(name1, name2,x,y,name3,z))
