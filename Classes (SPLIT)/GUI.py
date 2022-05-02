class GUI(Manager):
    '''This is the GUI Class. This class is mostly responsible for facilitating the collection 
of data from the user in a manner that the program as a whole can utilize and manipulate
said data. At the moment, the class currently has the tkinter schematics for the 'Encrypt' portion 
of the program, and will be expanded to also include the 'Decrypt' portion once all classes 
can communicate properly with eachother (which will take some debugging on my end) '''
   

    def __init__(self, master):
        self.master = master
        master.title("Encryption Prototype")


        ###Elements from the Encrypt portion of the GUI###


        self.labelEncrypt = tk.Label(master, text="Enter the Plain Text you want encrypted here")
        self.labelEncrypt.grid(row=0, column=0)

        self.entryEncrypt = tk.Entry(master)
        self.entryEncrypt.grid(row=1, column=0)

        self.doneButton = tk.Button(master, text="Done!", command=self.doneClick)
        self.doneButton.grid(row=2, column=0)

        self.nullSpaceVert = tk.Label(master, text="\n")
        self.nullSpaceVert.grid(row=3, column=0)

        self.labelSharedKey = tk.Label(master, text="Enter a Password Here | Under 8 Characters")
        self.labelSharedKey.grid(row=4, column=0)

        self.entrySharedKey = tk.Entry(master)
        self.entrySharedKey.grid(row=5, column=0)

        self.doneButton2 = tk.Button(master, text="Done!", command=self.doneClick2)
        self.doneButton2.grid(row=6, column=0)

        self.randButton = tk.Button(master, text="Make me One!", command=self.randFunc)
        self.randButton.grid(row=7, column=0)

        self.nullSpaceVert1 = tk.Label(master, text="\n")
        self.nullSpaceVert1.grid(row=8, column=0)

        self.var = tk.StringVar()
        self.var2 = tk.StringVar()
        self.radioLabel = tk.Label(master, text="Choose your Encryption Method")
        self.radioLabel.grid(row=9, column=0)
        self.r1 = tk.Radiobutton(master, text="DES", variable=self.var, value="DES", command=self.radioSelection)
        self.r1.grid(row=10, column=0)
        self.r2 = tk.Radiobutton(master, text="AES", variable=self.var, value="AES", command=self.radioSelection)
        self.r2.grid(row=11, column=0)
        self.r3 = tk.Radiobutton(master, text="BlowFish", variable=self.var, value="BlowFish",
                                 command=self.radioSelection)
        self.r3.grid(row=12, column=0)

        self.enterButton = tk.Button(master, text = "Encrypt my Text!", command = self.scramble)
        self.enterButton.grid(row = 13, column = 0)

        self.op1 = tk.Label(master, bg='white', width=30, text='empty')
        self.op1.grid(row=14, column=0)
        self.op2 = tk.Text(master, bg = 'white', width = 150, height = 2)
        self.op2.grid(row = 17, column = 0)
        self.nullSpaceVert2 = tk.Label(master, text="\n")
        self.nullSpaceVert2.grid(row=15, column=0)
        self.labelOut = tk.Label(master, text='Result: ')
        self.labelOut.grid(row=16, column=0)

        ##Elements of the Decrypt portion of the GUI### 

        self.labelEncryptD = tk.Label(master, text="Enter the CipherText you want Decrypted here")
        self.labelEncryptD.grid(row=0, column=1)

        self.entryEncryptD = tk.Entry(master)
        self.entryEncryptD.grid(row=1, column=1)

        self.doneButtonD = tk.Button(master, text="Done!", command=self.doneClickD)
        self.doneButtonD.grid(row=2, column=1)

        self.nullSpaceVertD = tk.Label(master, text="\n")
        self.nullSpaceVertD.grid(row=3, column=1)

        self.labelSharedKeyD = tk.Label(master, text="Enter the correct Password Here | Under 8 Characters")
        self.labelSharedKeyD.grid(row=4, column=1)

        self.entrySharedKeyD = tk.Entry(master)
        self.entrySharedKeyD.grid(row=5, column=1)

        self.doneButton2D = tk.Button(master, text="Done!", command=self.doneClick2D)
        self.doneButton2D.grid(row=6, column=1)

        #self.randButtonD = tk.Button(master, text="Make me One!", command=self.randFuncD)
        #self.randButtonD.grid(row=7, column=1)

        self.nullSpaceVert1D = tk.Label(master, text="\n")
        self.nullSpaceVert1D.grid(row=8, column=1)

        self.varD = tk.StringVar()
        self.var2D = tk.StringVar()
        self.radioLabelD = tk.Label(master, text="Choose your Encryption Method")
        self.radioLabelD.grid(row=9, column=1)
        self.r1D = tk.Radiobutton(master, text="DES", variable=self.var, value="DES", command=self.radioSelectionD)
        self.r1D.grid(row=10, column=1)
        self.r2D = tk.Radiobutton(master, text="AES", variable=self.var, value="AES", command=self.radioSelectionD)
        self.r2D.grid(row=11, column=1)
        self.r3D = tk.Radiobutton(master, text="BlowFish", variable=self.var, value="BlowFish",
                                 command=self.radioSelectionD)
        self.r3D.grid(row=12, column=1)

        self.enterButtonD = tk.Button(master, text = "Decrypt my Text!", command = self.scrambleD)
        self.enterButtonD.grid(row = 13, column = 1)

        self.op1D = tk.Label(master, bg='white', width=30, text='empty')
        self.op1D.grid(row=14, column=1)
        self.op2D = tk.Text(master, bg = 'white', width = 150, height = 2)
        self.op2D.grid(row = 17, column = 1)
        self.nullSpaceVert2D = tk.Label(master, text="\n")
        self.nullSpaceVert2D.grid(row=15, column=1)
        self.labelOutD = tk.Label(master, text='Result: ')
        self.labelOutD.grid(row=16, column=1)

        ##Encrypt portion functions###


    def doneClick(self):
        """This method is responsible for returning whatever text was placed inside of the "entryEncrypt" 
        text box.  this method also includes a print function that outputs the same content for future debugging purposes"""
        self.finalPlain = self.entryEncrypt.get()
        ##print("|DEBUGGING| Output: \n" + self.finalPlain)
        Manager.getPlainTxt(self.finalPlain)


    def doneClick2(self):
        '''Similar to the method above, this method is responsible for returning the contents of the 'entrySharedKey' text
        box.  It also prints the same data for future debugging.   May combine with the above function to avoid creating
        repetitive methods. '''
        self.finalText = self.entrySharedKey.get()
        ##print("|DEBUGGING| Output: \n" + self.finalText)
        Manager.getSharedKey(self.finalText)
        


    def randFunc(self):
        '''this method is responsible for providing a pseudo-randomly generated shared key for the user 
        to use in encrypting their plaintext.  at the moment it has a pre-defined key as the 'Encrypt' class 
        has a function just for this purpose, but still need to make the classess work with one another.  This method 
        also erases any text inside of the text box and auto fills it with the contents of the auto-gen key'''
        self.key = Encrypt.strGen()
        self.entrySharedKey.delete(0,tk.END)
        self.entrySharedKey.insert(0, self.key)


    def radioSelection(self):
        '''this method is responsible for displaying to the user what encryption algorithm they have selected, 
        and returning that information to the other classes.  Similar to other methods above, a debugging print
        is also included. Mostly a proof of concept as none of the radio buttons affect the encryption/decryption 
        as of yet. '''
        self.op1.config(text="You Have Selected: " + self.var.get())
        print("|DEBUGGING| Reported Algorithm: " + self.var.get())
        return self.var.get()

    def scramble(self):
        self.op2.configure(state = 'normal')
        Manager.verify(self.finalPlain, self.finalText)
        finalEncrypt = Encrypt.DES(self.finalPlain, self.finalText)
        self.op2.insert(1.0, str(finalEncrypt))
        self.op2.configure(state = 'disabled')

        ##print("|DEBUGGING| Reported Algorithm: " + self.var.get())
        #print (finalEncrypt)
        #return finalEncrypt

        ###Decrypt Portion Functions 

    def doneClickD(self):
        """Duplicate method variant for the Decrypt Method and its respective appropriate changes"""
        self.finalPlain = self.entryEncryptD.get()
        ##print("|DEBUGGING| Output: \n" + self.finalPlain)
        Manager.getPlainTxt(self.finalPlain)


    def doneClick2D(self):
        """Duplicate method variant for the Decrypt Method and its respective appropriate changes"""
        self.finalText = self.entrySharedKeyD.get()
        ##print("|DEBUGGING| Output: \n" + self.finalText)
        Manager.getSharedKey(self.finalText)
        


    def randFuncD(self):
        """Duplicate method variant for the Decrypt Method and its respective appropriate changes"""
        self.key = Encrypt.strGen()
        self.entrySharedKey.delete(0,tk.END)
        self.entrySharedKey.insert(0, self.key)


    def radioSelectionD(self):
        """Duplicate method variant for the Decrypt Method and its respective appropriate changes"""
        self.op1D.config(text="You Have Selected: " + self.varD.get())
        print("|DEBUGGING| Reported Algorithm: " + self.varD.get())
        return self.varD.get()

    def scrambleD(self):
        """Duplicate method variant for the Decrypt Method and its respective appropriate changes"""
        self.op2D.configure(state = 'normal')
        Manager.verify(self.finalPlain, self.finalText)
        finalEncrypt = Decrypt.SED(self.finalPlain, self.finalText)
        self.op2D.insert(1.0, str(finalEncrypt))
        self.op2D.configure(state = 'disabled')

        ##print("|DEBUGGING| Reported Algorithm: " + self.var.get())
        #print (finalEncrypt)
        #return finalEncrypt




