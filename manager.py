from sqlite_manager.conn import SQLiteConnect
from abc import ABCMeta


class AbstractSQLite(metaclass=ABCMeta):

    def query(self):
        pass

    def columns(self):
        pass


class SQLiteManager(AbstractSQLite):

    def __init__(self, conn):
        self._cursor = conn.cursor()

    def create_table(self, table_name):
        return CreateTableSQLite(table_name, self._cursor)

    def select(self, *columns, table_name):
        pass

    def insert(self, table_name):
        return InsertSqlite(table_name, self._cursor)

    def update(self, table_name):
        pass



class RowEntity():
    ''' Conjunto de atributos de una entidad '''

    def __init__(self):
        pass

    def _columns(self, **columns):
        for column_name in columns:
            self[column_name] = columns[column_name]



class CreateTableSQLite():

    def __init__(self, table_name, cursor):
        self._query =  '''CREATE TABLE {} ( '''.format(table_name)
        self._cursor = cursor

    def _primary_key(self, column):
        pass

    def column(self, column, column_type = '', column_len = None):
        self._query += "{} {}".format(column,column_type)
        if column_len is not None:
            self._query += "({})".format(column_len)
        self._query += ", "

    def query(self):
        try:
            self._query = self._query[:-2]+")"
            self._cursor.execute(self._query)
        except Exception:
            print("{}".format('''
                La tabla fue generada con anterioridad 
                o no cuenta con los permisos sobre 
                el directorio
            '''))






class InsertSqlite():


    def __init__(self, table_name, cursor):
        self.cursor = cursor
        self._query = '''INSERT INTO {} ('''.format(table_name)

    def row(self, columns = [], column_value = []):
        q_column= '('
        q_val = '('
        try:
            for c,v in zip(columns, column_value):
                q_column += c+','

        except Exception:
            print(''' La Logitud de Datos no coincide ''')

    def data_type(self, val):


        pass

    def rows(self, *rows):
        pass

    def query(self):
        #self.cursor
        pass




def Sqlite(sql_file):
    return SQLiteManager(
        SQLiteConnect()._conn(sql_file)
    )