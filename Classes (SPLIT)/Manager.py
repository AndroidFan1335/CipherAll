class Manager():
    '''This is the Manager class (formerly the UserInput class).  This class is responsible for assigning the data from the GUI
    to variables that can be manipulated by all the subclasses in this program.  This class was renamed as it was deeemd 
    more appropriate as a manager class compared to a UserInput class (which is basically the GUI class).'''
    

    def __init__(self, SharedKey, Option, textFieldCiph, textFieldPlain, finalEncryption):
        '''initialization method'''
        self.SharedKey = entrySharedKey
        self.Option = Option ##like ciphOrPlain option, determined via radio button or other selection
        self.textFieldCiph = entryEncrypt
        self.textFieldPlain = finalPlain


    def isKeyValid(): 
        ##Method that checks if the user input a valid shared key (to determine if a keygen is needed)
        IsKeyEmpty = False
        if (len(self.SharedKey)) == 0:
            IsKeyEmpty = True
        return IsKeyEmpty


    def getSharedKey(userkey):
         ##Method Returns a valid shared key
        SharedKey = userkey
        print (SharedKey)


    def getPlainTxt(userplain): 
        ##Method Returns the PlainText
        usertext = userplain
        finalPlain = usertext
        print (userplain)


    def getCiphTxt(userpw):
         ##Method Returns the CipherText
        newpassword = userpw
        entrySharedKey = userpw
        print(newpassword)


    def encOrDec():
        ##method that checks whether Encrypt or Decrypt was selected
        return self.Option


    def verify(input, inputpw):
        print(input)
        print (inputpw)
