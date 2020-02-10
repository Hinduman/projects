# functions used by cipher module
# this functions can be used individually for CLI also
# through function calling
import math


# this function accepts 2 strings and displays an encoded array as output
def encrypt(arg1,arg2):
    var=[arg1[9*x:9*(x+1)] for x in range(math.ceil(len(arg1)/9))]
    var[-1]+='0'*(9-len(var)%9)
    var1=lambda x,i=2:x[:9] if len(x)>9 else var1(x*i,i=i+1)
    ans=[list(map(lambda x,y,z:ord(x)^ord(y)^z,i,var1(arg2),range(1,10))) for i in var]
    return func(ans,[])


# this function accepts 1st argument as array and 2nd argument as string
# displays the decoded as string
def decrypt(arg1,arg2):
    var=[arg1[9*x:9*(x+1)] for x in range(math.ceil(len(arg1)/9))]
    var1=lambda x,i=2:x[:9] if len(x)>9 else var1(x*i,i=i+1)
    ans=[list(map(lambda x,y,z:x^ord(y)^z,i,var1(arg2),range(1,10))) for i in var]
    return ''.join(chr(i) for i in func(ans,[]) if i != 48)


#  this is function converting 2D array to 1D
# by linearly placing the individual elements
# this is called in other two classes
def func(arg,arg1):
    var=lambda arg,arg1:arg1 if not len(arg) else var(arg,arg1+arg.pop(0))
    return var(arg,arg1)
