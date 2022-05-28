
'''enumerate gives index and list in sequence'''
# a=['milk','bread','water'] # it is a list
# print(type(a),a)
'''to make it into enumerate data type'''
# b=enumerate(a)
# print(type(b),b)#'enumerate'> <enumerate object at 0x000001F084623580>
'''try to priint b it ging address of b
to print exact value use'''

# print(dict(b)) #{0: 'milk', 1: 'bread', 2: 'water'}

# print(list(b))#[(0, 'milk'), (1, 'bread'), (2, 'water')]

# print(tuple(b))#((0, 'milk'), (1, 'bread'), (2, 'water'))

'''set unorder list it will not give in order list items'''

# print(set(b))#{(2, 'water'), (1, 'bread'), (0, 'milk')}

'''to change the order'''

# a=['milk','bread','water']
# c=enumerate(a,-1)
''' in this start from -1,0,1,2,_,_,_'''
# print(list(c))#[(-1, 'milk'), (0, 'bread'), (1, 'water')]

# a=['milk','bread','water','ghee','curd','butter','honey']
# c=enumerate(a,8)
# c=enumerate(a,-5)
# print(list(c))
# print(set(c))
 

'''print the fuction available in directory'''
# print(dir(__builtins__))

'''complex data type'''
a=1+2j
# print(type(a)) #<class 'complex'>
print(a)#(1+2j)
'''real, imag gives the answer in float value'''
print(a.real)#1.0
print(a.imag)#2.0