class Pokemon:
    value1="his name is Squaduck and"
    value2="his name is bulabsor and"

class Power:
    value3="his power is watergun"
    value4="his power is leafgrass"

class Mix (Pokemon, Power):
    pass

pokemon_=Pokemon
power_=Power
mix_=Mix

print (pokemon_.value1)
print (power_.value3)
print (pokemon_.value2)
print (power_.value4)



class Pokemon:
    value1="his name is Squaduck and"
    value2="his name is bulabsor and"

class Power:
    value3="his power is watergun"
    value4="his power is leafgrass"

class Mix (Pokemon , Power):
      pass

pokemon_=Pokemon
power_=Power
mix_=Mix

print(pokemon_.value1,power_.value3)
print(pokemon_.value2,power_.value4)



class Pokemon:                                        #superclass 
    Value1='he is Pikachu with electric power'
    Value2='he is charlizard with fire power'


class Pokemon1:                                        #superclass 
    Value11='he is Pikachu with electric power'
    Value22='he is charlizard with fire power'

class Power(Pokemon, Pokemon1):                                   #subclass 
    pass

pokemon_=Pokemon()
pokemon1_=Pokemon1
power_=Power()

print(pokemon_.Value1,pokemon1_.Value11)
print(pokemon_.Value2,pokemon1_.Value22)







class Pokemon:                                        #superclass 
    Value1='he is Pikachu with electric power'
    Value2='he is charlizard with fire power'

class Power(Pokemon):                                   #subclass 
    pass

pokemon_=Pokemon()
power_=Power()
print(pokemon_.Value1)
print(pokemon_.Value2)

