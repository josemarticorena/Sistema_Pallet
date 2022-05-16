import pyodbc

#server = 'PANCHO-PC\SQLEXPRESS'
#bd = 'DBPAncho'
#usuario = 'Pancho2'
#contrasena = '3126'

server = 'bde.com.gt'
bd = 'bde_Python'
usuario = 'bde_Python'
contrasena = 'DhO1Yx4BUfyN'


try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server}; SERVER='+ server+
    '; DATABASE='+bd+'; UID='+ usuario+'; PWD='+contrasena)
    print('conexion exitosa')

except:
    print ('error')


cursorInsert = conexion.cursor()
T = 30
Sensor = 0
Encendido = 1
Conveyor = 0

consulta = "Insert into PanchoTabla(Tiempo, Sensor1, Encendido, Conveyor) values ('30','1','0','1');"

cursorInsert.execute(consulta)

cursorInsert.commit() #confirma el cambio a base de datos
cursorInsert.close()