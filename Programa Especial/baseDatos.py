import sqlite3

connect = sqlite3('baseDatos')
cursorBD = connect.cursor()

def tablaExiste(data):
    cursorBD.execute('''SELECT COUNT (name) FROM SQLITE_MASTER WHERE TYPE = 'table' and name = '{}' '''.forma(data))
    if cursorBD.fetchone()[0] == 1:
        return True
    else:
        cursorBD.execute('''CREATE TABLE PRODUCTO (CODIGO INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE TEXT, ) ''')