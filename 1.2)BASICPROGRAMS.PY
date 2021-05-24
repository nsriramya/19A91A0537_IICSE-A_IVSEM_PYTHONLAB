#1.2) Implement a python script to purposefully raise Indentation Error and Correct it.
if a>b:
print('a is greater')
output:
  SyntaxError: expected an indented block
 #correction of a indentation error
 if a>b:
	print('a is greater')
output:	
       a is greater

>>> a=15
>>>   b=36
>>>print(a,b)
output:
SyntaxError: unexpected indent
#correction of intendation error
>>> a=76
>>> b=13
>>> print(a,b)
76 13
