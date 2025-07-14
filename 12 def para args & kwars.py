def student (name, age, marks):
    print('name:',name)
    print('age:',age)
    print('mark:',marks)

student('hero',20,98)

#In this we will learn the use of * this in argument

def student1 (name,age,*marks):
    print('name:',name)
    print('age:',age)
    print('mark:',marks)

student1('Nazab',12, 50,60,88,50,40)


#In this we will learn the use of ** this in argument

def student2(name,age,**marks):
    print('name:', name)
    print('age:', age)
    print('mark:',marks)

student2("Halwa",1, Pysics=100,Maths=100,Chemistry=100)



print('FOR practice')

def justiceleague(name,position,weekness,nemesis,*powers):
    print('Name:',name)
    print('Position:',position)
    print('Weekness:',weekness)
    print('Nemesis:',nemesis)
    print('powers:',powers)

justiceleague('Superman','Hero','Kryponite','Lex Luthor','Superstrength','speed','can fly','x-ray & heat vision', )
justiceleague('Batman','Vigilante','Bullet','Joker','Rich','kunfu')
justiceleague('Wonderwomen','Greek god','Love','Cheetah girl','God power','truth rope','hand sheild')
justiceleague('Aquaman','Hero','Dirt','Blackmanta','Water breathe','Superstrength')
justiceleague('Flash','Hero','slow','Reverse Flash','Speed')


#In this we will learn the use of ** this in argument also the value of these will be mark under the line but only key will print

def student3(name,age,**marks):
    print('Name:', name)
    print('Age:', age)
    for x in marks:
        print(x)

student3("Halwa",1, Pysics=100,Maths=100,Chemistry=100)

#same code it's just it will print both like 1 1 niche or 1 line mai bhi

def student4(name,age,**marks):
    print('Name:', name)
    print('Age:', age)
    print('Mark:',marks)
    for x in marks:
        print(x)

student4("Halwa",1, Pysics=100,Maths=100,Chemistry=100)

#for all value 1 k 1 niche

def student5(name,age,**marks):
    print("Name:",name)
    print('Age:',age)
    print('Marks:', marks)
    for key,value in marks.items():
        print(key,'',value)
student5("Rishab",40,Chemistry=80,Biology=99,Maths=80)