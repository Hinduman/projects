'''
Cipher double codec
this code is most optimised
This simple GUI displays both encoder,decoder in notebook format
1st page has encoder region and 2nd page,decoder
To cross-verify, copy the results from encoder page to 1st Entry block of decoder page
you can change passcode entry to get different results from same message
Python>=3.1 interpreter
'''
from tkinter import ttk,StringVar,font,CENTER
import resource


# Formation of object in GUI form
class CipherApp(ttk.Notebook):
    def __init__(self):
        # inheriting super class using __init__ method
        super().__init__()
        # initializing variables for future usage
        self.var=font.Font(family=font.families()[6],size=16)
        self.var1=StringVar(),StringVar(),StringVar(),StringVar()
        self.var2=ttk.Frame(),ttk.Frame()
        self.ans=StringVar(),StringVar()
        [x.set('passcode') for x in self.var1[1::2]]
        # placing widgets in main class using grid layout
        [ttk.Label(x,text=y,font=self.var).grid(row=0,column=0) for x,y in zip(self.var2,['Message to be coded','Array to be decoded'])]
        [ttk.Entry(x,textvariable=y,font=self.var,width=30).grid(row=0,column=1) for x,y in zip(self.var2,self.var1[::2])]
        [ttk.Label(x,text='Pass key',font=self.var).grid(row=1,column=0) for x in self.var2]
        [ttk.Entry(x,textvariable=y,font=self.var,width=20).grid(row=1,column=1) for x,y in zip(self.var2,self.var1[1::2])]
        [ttk.Button(x,text=y,command=z).grid(columnspan=2) for x,y,z in zip(self.var2,['Encrypt','Decrypt'],[self.func,self.func1])]
        [ttk.Entry(x,textvariable=y,width=80,justify=CENTER).grid(columnspan=2) for x,y in zip(self.var2,self.ans)]
        [self.add(x,text=y) for x,y in zip(self.var2,['Encryption','Decryption'])]
        # placing notebook class in Application using packing layout
        self.pack()

    # functions to display the results on Button press
    def func(self):
        self.ans[0].set(resource.encrypt(self.var1[0].get(),self.var1[1].get()))

    def func1(self):
        var=[int(x) for x in self.var1[2].get().strip('[]()').split(',')] if ',' in self.var1[2].get() else \
                            [int(x) for x in self.var1[2].get().strip('[]()').split()]
        self.ans[1].set(resource.decrypt(var,self.var1[3].get()))


# entering main loop
if __name__ == '__main__':
    # creating application using object calling(instantiation)
    app=CipherApp()
    app.master.title('Cipher Codec')
    # application dispatching using mainloop method
    app.mainloop()
