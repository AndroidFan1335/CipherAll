import random, string, pyDes
from tkinter import *
import tkinter as tk
'''Import statments that import the libraries necessary for program classes to function.
Random: used for a good portion of the Encrypt class (such as strGen())
string: used for user input manipulation and also used in the strGen() method.
pyDes: Python library that does most of the heavy lifting regarding implementing a secure
DES encryption algoritm.  Used in the Encrypt and Decrypt Classes and its respective methods
tkinter: main driving force behind the GUI class.  '''


'''This section can be considered alike to the int main() portion of the program.  Very little is expected
to occur outside the main classes. '''
window = tk.Tk()
gui = GUI(window)
window.mainloop()
