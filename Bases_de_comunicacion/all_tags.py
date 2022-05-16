from calendar import formatstring
from pylogix import PLC 

IPAdd = '192.168.0.70'  #ESCRIBIR DIRECCION IP DEL PLC
Slot = 1    #ESCRIBIR EL SLOT DEL PROCESADOR (EN CONTROL LOGIX PUEDE SER DISTINTO DE 0)


ControlLogix = PLC()
ControlLogix.IPAddress = IPAdd
ControlLogix.ProcessorSlot = Slot

Alltags = ControlLogix.GetTagList(False)

#Al no estar conectada a un PLC no funciona
with open('tag_list.txt', 'w') as f:
    for t in Alltags.Value:
        f.write('\n' + t.TagName )
print(Alltags.Value)
for t in Alltags.Value:
    print(t.TagName)