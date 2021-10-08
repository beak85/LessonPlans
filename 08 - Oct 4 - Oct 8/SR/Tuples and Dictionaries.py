##  Sequence Type:
##  a sequence is data which can be scanned by the for loop.

##  Mutability - whether it can be freely modified or not, once created
##      lists are mutable e.g. list.append()
##
##      In situ is a Latin phrase that translates as literally “in position”.
##      For example, the following instruction modifies the data in situ
##      list.append(1)
##
##      Immutable data can only be assigned and read

##      Tupples are immutable

## Creating a tuple

tuple1 = (1, 2, 4, 8) #parenthsis are the prefered way!!
tuple2 = 1., .5, .25
tuple3 = ()
tuple4 = (7,)

## - Try printing each of those

## You can access elements just as in lists, including slices, len(), in, not in
##  DON"T TRY TO MODIFY IT THOUGH

## Concatenate using the +


## Circulate example

v1 = 1
v2 = 2
v3 = 3
v1, v2, v3 = v2, v3, v1 #remember swapping?
print (v1, v2, v3)


######################

## Dictionary
##  -Not a squence typ, but can be adapted
##  -mutable
##  -made of KEYS and VALUE pairs

mascots={'Ayersville':'Pilots', 'Bryan':'Golden Bears', 'Tinora':'Rams'}
print(mascots)

# Order is not preserved!
### CHANGE DEF ABOVE TO VERITCALLY ALIGNED ###

print(mascots['Bryan'])
##print(mascots['Archbold'])

schools = ['Ayersville', 'Archbold', 'Bryan', 'Tinora']
for school in schools:
        if school in mascots:
            print (school,'->',mascots[school])
        else:
            print('Not in dictionary:', school)

#### COMPARE TO:
            
for school in mascots:
        if school in mascots:
            print (school,'->',mascots[school])
        else:
            print('Not in dictionary:', school)


            
for sch,mas in mascots.items():
    print(sch,"->",mas)

for mas in mascots.values():
    print(mas)

mascots['Ayersville'] = 'Losers'
print (mascots)

mascots['Edon'] = 'Bombers'
del mascots['Ayersville']

print(mascots)



