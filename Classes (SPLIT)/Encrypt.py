class Encrypt(Manager):

    """This is the Encrypt Class. This class will be responsible for encrypting any given plaintext and spitting out 
a cipher text along with a shared key, if one is needed. Much of its output will be dependant on the information
provided from the UserInput class, so it will inherit much of its methods and data.  Currently having issues with 
implementing PyDes as this implementation encrypts strings as bytes (which makes sense from a security standpoint) which makes
it difficult to implement a definite encrypt function.  Currently replaced with encryption functions used in a previous assignment 
as a placeholder in order to make progress on the GUI. Blocks of code that utilized the PyDes implementation blocked out pending
further review. """
    

    def __init__(self, SharedKey, textFieldPlain):
        '''Initialization method'''
        self.SharedKey = self.entrySharedKey
        self.textFieldPlain = self.finalPlain


    def DES(plainText, key):    

        '''this method is responsible for creating a DES standard ciphertext from a given plaintext and shared key
        combination.  Most of the work should be done via the PyDes library, but pending revision of the DES and SED methods, 
        placeholder algorithm is being utilzed, sourced from Bradley N. Miller, David L. Ranum, Julie Anderson. 2021. Python programming in
        context (3rd. ed.). Jones & Bartlett Learning, Burlington, MA. 166-253.'''

        alphabet ="abcdefghijklmnopqrstuvwxyz " 
        plainText = plainText.lower()
        cipherText = ""
        for ch in plainText:
            idx = alphabet.find(ch) 
            cipherText = cipherText + key[idx]
        return cipherText 

            ##previous PyDes implementaion. Errors produced: processed as BYTE instead of STR
        '''charset = "utf-8"
        k = pyDes.des(str(inputpw), pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
        r = k.encrypt(input.encode(charset))
        return r'''


    def strGen():
        ''' This is a temporary pseudo-random shared key generator.  This method should responsible for creating a fairly secure
            shared key that can be used with any given plaintext in an encryption algorithm.  Will be updated with a more hardened generator
            as the PyDes implementaion is figured out. Sourced from sourced from Bradley N. Miller, David L. Ranum, Julie Anderson. 2021. Python programming in
        context (3rd. ed.). Jones & Bartlett Learning, Burlington, MA. 166-253 .'''
        def rmChar (string, idx):
            return string[:idx] + string[idx+1:] #
        alphabet = "abcdefghijklmnopqrstuvwxyz "
        key = ""
        for i in range (len(alphabet)- 1, -1, -1):
            idx = random.randint(0,i)
            key = key + alphabet[idx]
            alphabet = rmChar(alphabet, idx)
        return key

