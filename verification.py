'''
This is 'an idea' of alternate captcha service for bot verification
An GUI window will open if you run this file in computers
comprising python interpreter(Python>=3.1)
'''

from tkinter import Frame,Entry,Button,Label,font,StringVar
import random,string


class CaptchaApp(Frame):
    def __init__(self):
        #inheriting main class Frame below
        super().__init__()
        #initializing variables for further usage
        self.var=font.Font(size=20)
        self.var1=StringVar(self),StringVar(self)
        self.var1[0].set(random.choices(string.ascii_letters+string.digits,k=8))
        #packing the widgets in main frame
        Label(self,text='Security Pin:').grid(row=0,column=0)
        Label(self,textvariable=self.var1[0],font=self.var).grid(row=0,column=1)
        Label(self,text='Enter the reverse of Security Pin\nconsidering only alphabets:').grid(row=1,column=0)
        Entry(self,textvariable=self.var1[1],width=30).grid(row=1,column=1)
        Button(self,text='Check!',command=self.func).grid(columnspan=2)
        self.var2=Label(self)
        #placing main frame in application
        self.pack()

    #method for performing verification of security pin
    #called only when Button('Check!') is pressed
    def func(self):
        #enters if block when contents in entry block follows protocol
        if ''.join(filter(lambda x:True if x in string.ascii_letters else False,self.var1[0].get()))==self.var1[1].get()[::-1]:
            self.var2['text']='Done'
        else:
            #this block resets the entry contents entered and should try again
            self.var2['text']='Try again!'
            self.var1[0].set(random.choices(string.ascii_letters+string.digits,k=8))
            self.var1[1].set('')
        self.var2.grid(columnspan=2)


#main block of program
if __name__ == '__main__':
    #Instantiating the class below
    app=CaptchaApp()
    app.master.title('Captcha verification')
    app.master.resizable(0,0)
    #Application window is created by mainloop() function
    app.mainloop()
