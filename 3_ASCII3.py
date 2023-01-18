""" /home/cir/ascii3.py
    TNM/ITL
    Diplomado en DevOps
    Por Cirino Silva Tovar
    Viernes 16 de Diciembre 2022

    Agregé esta linea (Lalo)  <------------------------------------
"""

# program to print ASCII table from '0 to 255'
# coding: cp437

import codecs

def meta():
   print ("\nDespliega la tabla ascii para IBM-PC tradicional")
   print ("usando unicode code page 437\n")

def header():
   print("  ", end = "")
   for i in range(0, 16):
      print (hex(i)[2:], end = " ")
   print ()
   for i in range(0,34):
      print ("_", end = "") 
   print ()
   
def control():   
   print  ("0", end = " ")  
   for i in range(0, 33):
      if (i % 16 == 0 and i != 0):
         print ()
         if (i == 32):
            print (i % 16 + 2, end = " ")
         else:
            print (i % 16 + 1, end = " ")   
      if (i < 32):
         print (".", end = " ")

def table():
   j = 2  
   for i in range(33, 256):
      if (i % 16 == 0):
         j = j + 1
         print ()
         print (hex(j)[2:], end =" ")
      h = hex(i) [2:]
      ch = codecs.decode(h, 'hex_codec') 
      print (ch.decode('cp437'), end = " ")
   print ()
   
meta()
header()
control()
table()   
