def func(arg,arg1,arg2):
    temp=lambda x,y:x//y+1 if x%y else x//y
    if arg2:
        arg=[int(x) for x in arg.split()]
    mat1=(list(range(1,17))*temp(len(arg),16))[:len(arg)]
    arg1=((arg1*temp(16,len(arg1)))[:16]*temp(len(arg),16))[:len(arg)]
    if arg2:
        return ''.join(map(lambda x,y,z:chr(x^y^ord(z)),arg,mat1,arg1))
    else:
        return ' '.join(map(lambda x,y,z:str(ord(x)^y^ord(z)),arg,mat1,arg1))

print('''Hello User, Welcome to Cipher Double key encryption
The program asks for the message, secret key and
Converts your message to encrypted number array,
which can be decoded only by using same secret key\n\n''')
print('''First enter your choice, based on it answer the relevant question
Choice 0:Encrypt the message
Choice 1:Decrypt the number array\n''')
choice=int(input('Choice 0/1??(Just enter the number):'))
if choice:
    print(func(input('Enter the number array leaving space between each digits:'),input('Your secret Key??:'),choice))
else:
    print(func(input('What is the message??:'),input('Your secret key??:'),choice))
