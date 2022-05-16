from pylogix import PLC 

IPAdd = '192.168.0.70'  #ESCRIBIR DIRECCION IP DEL PLC
Slot = 1    #ESCRIBIR EL SLOT DEL PROCESADOR (EN CONTROL LOGIX PUEDE SER DISTINTO DE 0)
Tag = 'velocidad'    #EESCRIBIR LA TAG QUE QUIERO LEER 
Lista_tags = [('tiempo',10),('errores', 4),('sensor1',1)]  #matriz para  una lista de tags 

ControlLogix = PLC()
ControlLogix.IPAddress = IPAdd
ControlLogix.ProcessorSlot = Slot

######## ESCRITURA INDIVIDUAL #######
ControlLogix.Write(Tag, 10)

######## ESCRITURA MULTIPLE #######
ControlLogix.Write(Lista_tags)
verificacion = ControlLogix.Write(Lista_tags)

for i in verificacion:
    print(i.TagName, i.Status)