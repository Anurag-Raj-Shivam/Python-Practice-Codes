#1st code only class & self

class Heath:
    def name(self, name, movie):
        self.name=name
        self.movie=movie
    def fullline (self):
        print("The charectar named" , self.name, "was in" , self.movie )

Pin = Heath()
Pin.name("Joker","The Batman")
Pin.fullline()


Pin = Heath()
Pin.name("Grey","lover boy")
Pin.fullline()


Pin = Heath()
Pin.name("Hilas","Hello Kitty")
Pin.fullline()

#2nd code Class self and construct

class Atom:
    def __init__(self, name):
        self.name=name
        print("Show name is", self.name)
    def charcter(self,hero):
        self.hero=hero
        print(self.hero)

A=Atom("DC Legends")
A.charcter("Captain")


A.charcter("Black")


A.charcter("Firstrom")


A.charcter("atom")

A=Atom("DC Legends")
A.charcter("Hawk")


#3rd Code Class self and construct and destruction

class Nikita:
    def __init__(self,value1):
        self.value1=value1
        print("I am sick so i want", self.value1)
    def __del__(self, value2):
        self.value2=value2
        print("else i will", value2)
    def action(self,acti, damki):
        self.acti=acti
        self.damki=damki
    def line(self):
        print(self.acti, "and", self.damki)

Niks=Nikita("a kiss")
Niks.action("hug"," agree on whatever i say")
Niks.line()
Niks.__del__("slap you hit you and cut you in pieces and put you in fridge")




class Chinri:
    def Behaviour(self,name,action):
        self.name=name
        self.action=action
    def Wholesentence (self):
        print("when she is", self.name,"she start", self.action, "me")

Sim2=Chinri()
Sim2.Behaviour("mad on me","souting")
Sim2.Wholesentence()

Sim2=Chinri()
Sim2.Behaviour("horny","cumming")
Sim2.Wholesentence()



print('------------------------------------------------------------------------------')

class dog1:
    def Name(self,name):
        self.name = name
    def Sentence(self):
        print("whhf", self.name, "barking on street")

sum5=dog1()
sum5.Name("Bruno")
sum5.Sentence()





class dog:
    def nameaction(self,name, action):
        self.name =name
        self.action = action
    def Wholeline (self):
        print("My dog named" , self.name, "is" ,self.action, "while we are having sex")

sum1=dog()
sum1.nameaction("Drogo","licking")
sum1.Wholeline ()


sum2=dog()
sum2.nameaction("bruno","barking")
sum2.Wholeline()

sum3=dog()
sum3.nameaction("munna","watching")
sum3.Wholeline()




print('------------------------------------------------------------------------------')



class Person:
    def Girlsexmark(self, girlname, girlthing):
        self.girlname= girlname
        self.girlthing = girlthing
    def printgirlsexyness(self):
        print(self.girlname," one part i like is", self.girlthing)

Sum1 = Person()
Sum1.Girlsexmark("Taneesha","Boobs")
Sum1.printgirlsexyness()



class Person:
    def printname(self, firstname, lastname):
        self.firstname=firstname
        self.lastname=lastname
    def printname1(self):
        print(self.firstname," ",self.lastname)     #"  " this we use to make space

personname = Person()
personname.printname("Raj","killa")
personname.printname1()


print('------------------------------------------------------------------------------')


class Person:
    def setFullName(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def printFullName(self):
        print(self.firstName, self.lastName)

personName = Person()        #we call this instance
personName.setFullName("Programming", "Knowledge")
personName.printFullName()





class Gender:
    def name(self, name, gender):
        self.name= name
        self.gender = gender
    def sex(self):
        print ("the girl named", self.name, "is", self.gender)

Sum1 = Gender ()
Sum1.name("Taneesha", 5.10)
Sum1.sex ()

print('------------------------------------------------------------------------------')


class plant:

    def type(self,name,type1,type2,eatable):
        self.name=name
        self.type1=type1
        self.type2=type2
        self.eatable=eatable
    def fulll(self,Category):
        if Category==self.type1:
            print('This is ',self.name,'and this a',self.type1,'and we can',self.eatable,'it')
        elif Category==self.type2:
            print('This is ',self.name,'and this a',self.type2,'and we can',self.eatable,'it')
        else:
            print('You are meat eater')

Patta=plant()
Patta.type('Rose','flower','plant','not eat')
Patta.fulll('flower')

Patta=plant()
Patta.type('Chick','flower','plant','not eat')
Patta.fulll('you can wright what ever you want')


print('----------------------------------------------')

#use of PASS in class

class Model:
    pass

Disha = Model()
Mia = Model()
Lilith = Model()

Disha.body= 'slim'
Mia.body= 'clevage'
Lilith.body='boobs'

Disha.age= 30
Mia.age= 25
Lilith.age= 35

Disha.best= 'belly'
Mia.best= 'moan'
Lilith.best= 'bulky'

print(Disha.body)
print(Mia.best)


print('----------------------------------------------')

class Rectangle:
    pass                  #this we use so we don't have to define the class at same time

rect1=Rectangle()
rect2=Rectangle()

rect1.height= 20
rect2.height= 30

rect1.width= 40
rect2.width= 10

print(rect1.height*rect1.width)
print(rect2.height * rect2.width)