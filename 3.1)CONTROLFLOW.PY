#Implement a python script for checking whether the citizen is eligible for vote or not.
age=int(input('enter the age : '))
if age>=18:
        print('eligible for voting')
else:
    print('not eligible for voting')

"""output:
        enter the age : 12
        not eligible for voting
        
        enter age : 24
        eligible for voting
