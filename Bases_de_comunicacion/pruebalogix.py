from pylogix import PLC 

IPAdd = ''  #ESCRIBIR DIRECCION IP DEL PLC
Slot = 0    #ESCRIBIR EL SLOT DEL PROCESADOR (EN CONTROL LOGIX PUEDE SER DISTINTO DE 0)
Tag = 'velocidad'    #EESCRIBIR LA TAG QUE QUIERO LEER 

ControlLogix = PLC()
ControlLogix.IPAddress = IPAdd
ControlLogix.ProcessorSlot = Slot


lectura = ControlLogix.Read(Tag)

if lectura.Status == 'Success' :
    print ('El tag "' + lectura.TagName + '" dice:')
    print (lectura.Value)
else:
    print ('El Tag "' +lectura.TagName + '" no existe!  Verifique el nombre del tag')