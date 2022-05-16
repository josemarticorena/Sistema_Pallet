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

######## LECTURA INDIVIDUAL #######
print('-------------LECTURA TAGS INDIVIDUALES---------------')
lectura = ControlLogix.Read(Tag)

if lectura.Status == 'Success' :
    print ('El tag "' + lectura.TagName + '" dice:')
    print (lectura.Value)
else:
    print ('El Tag "' +lectura.TagName + '" no existe!  Verifique el nombre del tag')

######## LECTURA INDIVIDUAL #######
def bindigits(n, bits):
    bini = []
    cont =0
    s = bin(n & int("1"*bits, 2))[2:]
    x = ("{0:0>%s}" % (bits)).format(s)
    print(x)
    for i in x:
        bini.append(i)
    bini.reverse()
    #print(bini)
    return bini
    #return ("{0:0>%s}" % (bits)).format(s)

print('-------------LECTURA TAGS INDIVIDUALES---------------')

lectura2 = ControlLogix.Read('Local:3:O.Data')

print('todo bien')
print(lectura2.Value)

binario = bindigits(lectura2.Value,32)
print(len(binario))
print (binario)




######### LECTURA VARIOS TAGS ##########
print('-------------LECTURA LISTA DE TAGS ---------------')
lista_read = ControlLogix.Read(Lista_tags)
for i in lista_read:
    if i.Status == 'Success' :
        print ('El tag "' + i.TagName + '" dice:')
        print (i.Value)
    else:
        print ('El Tag "' + i.TagName + '" no existe!  Verifique el nombre del tag')

reading = False

while reading:
    try:
        lectura = ControlLogix.Read(Tag)
        print ( lectura.Value)
        time.sleep(1)
    except KeyboardInterrupt:
        break


    