#Dictionary the value you save in a Variable

a= {"name": "Seeta", 'age':'16','year':'2006','True':'true','(2,3)':'5', '1:20':'20'} #: this we use to give value of something
print(a)
print(a['name'])   #by this we'll get value of specified value
print(a['age'])
print(a["True"])

print(len(a))

a.get('name')  #this will run in console = print(a['name'])

a['surname']='Sundari' #this will run in console and by this the value will be add in a

a.update({"name":"Sweta"})     #this will run in console

a.values() #this will run in console

