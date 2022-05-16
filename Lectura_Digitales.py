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

lectura2 = ControlLogix.Read('Local:4:O[2]',1) #Leemos el Tag Local 3 output Data


