from encodings import utf_8
from operator import truediv
from sqlite3 import Time 
import time
from tokenize import Binnumber
from pylogix import PLC 
import time

IPAdd = '192.168.11.1'  #ESCRIBIR DIRECCION IP DEL PLC
Slot = 2    #ESCRIBIR EL SLOT DEL PROCESADOR (EN CONTROL LOGIX PUEDE SER DISTINTO DE 0)


ControlLogix = PLC()
ControlLogix.IPAddress = IPAdd
ControlLogix.ProcessorSlot = Slot

######## LECTURA INDIVIDUAL #######
Tag = 'EnMarcha'   
Lista_tags = ['NivelTanque4','errores','sensor1']
print('-------------LECTURA TAGS INDIVIDUALES---------------')
fin = 0
inicio = 0
reading = True
while reading:
    try:
        lectura = ControlLogix.Read(Tag)
        if lectura.Status == 'Success' :
            #print (lectura.Value)
            time.sleep(1)
            Marcha = lectura.Value
            if Marcha == True:
                print ('Marcha')
                fin = time.time()
                
            else:
                print ('Paro')
                inicio = time.time()

            tiempo_transcurrido = inicio - fin
            print(tiempo_transcurrido)


        else:
            print ('El Tag "' +lectura.TagName + '" no existe!  Verifique el nombre del tag')
    except KeyboardInterrupt:
        break

