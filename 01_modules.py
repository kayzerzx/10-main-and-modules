"""
modules are an exremely useful tool for organizing and reusing code.
simply put, a module is a python file that contains code, variables, functions, classes 
that you can include in another program:
so just like functions modules help make your code:
-reusable
-organized
-easier to maintain

DRY Principle - "dont repeat yourself"

examples of built in modules:
time, random, os, math........

eg.
import math #include the module 
print(math.pi) $using code from the imported module
"""
#import math
#lets see the built in modules:
#help("modules")
#help(math)

#import a module with an alias
import math as m
print(m.pi)

#import just one function from a module
from random import randint
print(randint(1,10))
