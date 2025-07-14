#you cannot start with ELIF, it will always start with IF

name = input ("Enter Name:")  #: by use of this you can enter value

if name == "Chu":
    print("She is in China:",name) #: by use of this you can enter value
elif name=="Puh":
    print("She is in USA:",name)
elif name=="ghu":
    print("She is in India:",name)
else:
    print("She is dead")

#if you got 2 same value in if and elif, only IF value is going to RUN

name = input ("Enter Name:")  #: by use of this you can enter value

if name == "Chu":
    print("She is in China:",name) #: by use of this you can enter value
elif name=="Chu":
    print("She is in USA:",name)
elif name=="ghu":
    print("She is in India:",name)
else:
    print("She is dead")

#if you got 2 same value in if, then both IF value is going to RUN

name = input ("Enter Name:")  #: by use of this you can enter value

if name == "Chu":
    print("She is in China:",name) #: by use of this you can enter value
if name=="Chu":
    print("She is in USA:",name)
elif name=="ghu":
    print("She is in India:",name)
else:
    print("She is dead")

#NESDTED IF it means use if else statement inside of if else statement

x=10
if x >=0:
    print("x is positive")
    if (x%2)==0:
        print("x is even")
    else:
        print("x is odd")
else:
     print("x is negetive")