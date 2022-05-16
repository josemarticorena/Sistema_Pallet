from encodings import utf_8
from operator import truediv 
import time
from tokenize import Binnumber
from pylogix import PLC 

IPAdd = '192.168.0.70'  #ESCRIBIR DIRECCION IP DEL PLC
Slot = 1    #ESCRIBIR EL SLOT DEL PROCESADOR (EN CONTROL LOGIX PUEDE SER DISTINTO DE 0)
Tag = 'velocidad'    #EESCRIBIR LA TAG QUE QUIERO LEER 
Lista_tags = ['NivelTanque4','errores','sensor1']

ControlLogix = PLC()
ControlLogix.IPAddress = IPAdd
ControlLogix.ProcessorSlot = Slot

######## LECTURA Output Digital #######
print('-------------LECTURA TAGS---------------')
#Funcion que regresa el binario ordenado
def bindigits(n, bits):
    bini = []
    cont =0
    s = bin(n & int("1"*bits, 2))[2:]
    x = ("{0:0>%s}" % (bits)).format(s)
    for i in x:
        bini.append(int(i))
    bini.reverse()
    return bini


lectura2 = ControlLogix.Read('Local:3:O.Data') #Leemos el Tag Local 3 output Data

binario = bindigits(lectura2.Value,32) #MAndamos a convertir el valor entero obtenido por un binario, para ver todas las posiciones

print (binario)     
print(binario[10])
