class Decrypt(Encrypt):

    """This is the Decrypt Class.  This class will be resposible for decrypting ciphertext if given the correct decryption key. 
Similar to the Encrypt Class, much of its functionaliy will be inherited from the Manageer Class. """

    def __init__(self, SharedKey, textFieldCipher):
        '''initalization method'''
        super().__init__(SharedKey,textFieldCipher)
        plainText = ""


    def SED(cipherText, key):
        '''Similar to the Encrypt.DES Method, this method is responsible for decrypting a DES standard ciphertext from a given plaintext and shared key
        combination.  Most of the work should be done via the PyDes library, but pending revision of the DES and SED methods, 
        placeholder algorithm is being utilzed, sourced from Bradley N. Miller, David L. Ranum, Julie Anderson. 2021. Python programming in
        context (3rd. ed.). Jones & Bartlett Learning, Burlington, MA. 166-253.'''
        alphabet ="abcdefghijklmnopqrstuvwxyz "
        cipherText = cipherText.lower()
        plainText = ""
        for ch in cipherText:
            idx = key.find(ch)#alphabet replaced with key
            plainText = plainText + alphabet[idx]#key replaced with alphabet
        return plainText
        '''PyDes Implementation of SED: ERROR: utilizes BYTES instead of STR for security purpouses. 
        charset = "utf-8"
        ###k = pyDes.des(str(inputpw), pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
        ###r = k.decrypt(input).decode(charset)

        return input'''
