import sqlite3

class SQLiteConnect():

    @staticmethod
    def _conn(pathName = './sqlite-app.db'):
        '''
        @:return Retorna apuntador a la conexion
        '''
        return sqlite3.connect(pathName)