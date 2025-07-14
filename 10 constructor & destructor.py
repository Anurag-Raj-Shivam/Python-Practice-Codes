class honda:

    def type(self, owner, name, speed):
        self.owner = owner
        self.name = name
        self.speed = speed

    def sentence(self):
        print('Hello Team!')
        print("My name is", self.owner,
              'I have a', self.name, "and i can go for", self.speed, 'in just 10 mins.')


line = honda()
line.type('Raj', 'bike', '150km/hr')
line.sentence()


print('------------------------------------------------------------------------------')


class Pokemon:
    def __init__(self,name):
        self.name=name
        print(self.name, "I choose you")
    def __del__(self):
        print(self.name,"come back to ball")
    def Names(self,power,week):
        self.power=power
        self.week=week
    def fullline(self):
        print("his", self.power," and his weekness is" , self.week)


Fullla= Pokemon ("Charmender")
Fullla.Names("Fire","Ice")
Fullla.fullline()
Fullla.__del__()
        
        
        
print('------------------------------------------------------------------------------')


class Pokemon:
    def __init__(self,name):
        self.name=name
        print(self.name, "I choose you")
    def __del__(self):
        print(self.name, "come back to ball")
    def Power(self,Type,weekness):
        self.Type = Type
        self.weekness = weekness
    def fullline(self):
        print ("He is" ,self.Type, "pokemon and he can't fight in", self.weekness)

Line=Pokemon("Pikachu")
Line.Power("Electric", "water")
Line.fullline()
Line.__del__()


print('------------------------------------------------------------------------------')


class Chinri:
    def __init__(self,ids):
        self.ids=ids
        print("Our work started")
    def __del__(self,ids):
        print(self.ids,"Our work done")
    def Behaviour(self,name,action):
        self.name=name
        self.action=action
    def Wholesentence (self):
        print("when she is", self.name,"she start", self.action, "me")

Sim2=Chinri(7)
Sim2.Behaviour("mad on me","souting")
Sim2.Wholesentence()
Sim2.__del__(id)



print('------------------------------------------------------------------------------')


class Dog:
    
    def __init__(self):                                        #__del__
        print("our class is created")

    def __del__(self):
        print("our work is closed")
    def nameaction(self, name, action):
        self.name = name
        self.action = action

    def Wholeline(self):
        print("My dog named", self.name, "is", self.action, "while we are out walking.")

sum8 = Dog()
sum8.nameaction("Drogo", "licking")
sum8.Wholeline()
sum8.__del__()



print('------------------------------------------------------------------------------')



class Dog:
    
    def __init__(self):                                        #__del__
        print("our class is created")

    def __del__(self):
        print("our work is closed")
    def nameaction(self, name, action):
        self.name = name
        self.action = action

    def Wholeline(self):
        print("My dog named", self.name, "is", self.action, "while we are out walking.")

sum1 = Dog()
sum1.nameaction("Drogo", "licking")
sum1.Wholeline()

sum2 = Dog()
sum2.nameaction("Bruno", "barking")
sum2.Wholeline()

sum3 = Dog()
sum3.nameaction("Munna", "watching")
sum3.Wholeline()
sum3.__del__()




print('------------------------------------------------------------------------------')



class Dog:
    
    def __init__(self):                                        #__init__
        print("our class is created")
        
    def nameaction(self, name, action):
        self.name = name
        self.action = action

    def Wholeline(self,):
        print("My dog named", self.name, "is", self.action, "while we are out walking.")

sum4 = Dog()
sum4.nameaction("Drogo", "licking")
sum4.Wholeline()

sum5 = Dog()
sum5.nameaction("Bruno", "barking")
sum5.Wholeline()

sum6 = Dog()
sum6.nameaction("Munna", "watching")
sum6.Wholeline()


print('------------------------------------------------------------------------------')



class Actors:
    def __init__(self):
        print('Welcome to Award Show')
    def __del__(self):
        print('Thanks for coming')
    def Name(self,name,movie,hitorflop):
        self.name=name
        self.movie=movie
        self.hitorflop=hitorflop
    def lineis(self):
        print('And this award goes to',self.name,'for the film',self.movie,'and this is',self.hitorflop,'on box office')

Award=Actors()
Award.Name('SRK','Don','Superhit')
Award.lineis()

print('------------------------------------------------------------------------------')

class Mall:
    def __init__(self):
        print('Best mall in noida')
    def __del__(self):
        print('Thanks for coming')
    def namakran(self,name,location,open_time):
        self.name=name
        self.location=location
        self.open_time=open_time
    def line(self):
        print('Here we are presenting',self.name,'mall which is located in',self.location,'and you can visit till',self.open_time)

lelo=Mall()
lelo.namakran('DLF','Sector 18','23:30')
lelo.line()
lelo.__del__()


print('------------------------------------------------------------------------------')

class zoo:
    def __init__(self):
        print('Welcome to jungle')
    def __del__(self):
        print('Thanks for not being eaten')
    def animals(self,name,name1,nature):
        self.name=name
        self.name1=name1
        self.nature=nature
    def linewa(self,nametype):
        if nametype==self.name:
            print('Hello meet this little cutie named',self.name,'And he is',self.nature)
        elif nametype==self.name1:
            print('Hello meet this dangerous guy which we call',self.name1,'and he is so',self.nature)
        else:
            print('Animals are out of cage bhaggggggooooooo')

jumani=zoo()
jumani.animals('','Tiger','khunkhar')
jumani.linewa('Tiger')    #you have to write name1 element so it can run that line
jumani. __del__()


jorawar=zoo()
jorawar.animals('Rabbit','','naughty')
jorawar.linewa('Rabbit')  #you have to write name element so it can run that line
jorawar.__del__()

jinda=zoo()
jinda.animals('','','ooooooo')
jinda.linewa('you have to write other than name and name1 so else can run')
