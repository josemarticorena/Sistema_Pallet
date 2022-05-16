from pylogix import PLC 
#hola
PLCs = PLC()
dispositivos = PLCs.Discover()
for i in dispositivos.Value:
    print(i.IPAddress)
    print('  Product Code: ' + i.ProductName + ' ' + str(i.ProductCode))
    print('  Vendor/Device ID:' + i.Vendor + ' ' + str(i.DeviceID))
    print('  Revision/Serial:' +  i.Revision + ' '  + i.SerialNumber)
    print('')
    print (i.State)