import pyodbc

server = 'PANCHO-PC\SQLEXPRESS'
bd = 'DBPAncho'
usuario = 'Pancho2'
contrasena = '3126'



try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server}; SERVER='+ server+
    '; DATABASE='+bd+'; UID='+ usuario+'; PWD='+contrasena)
    print('conexion exitosa')

except:
    print ('error')


cursorInsert = conexion.cursor()

ver_tabla = "Select * from dbo.PanchoTabla"

cursorInsert.execute(ver_tabla)



Datos = cursorInsert.fetchall()
for dato in Datos:
    print(dato)


cursorInsert.commit() #confirma el cambio a base de datos
cursorInsert.close()
conexion.close()