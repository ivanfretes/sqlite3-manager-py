from sqlite_manager.manager import Sqlite

'''
Ejemplo de implementacion
@version : 0.0.1
'''

def main():
    sqlite = Sqlite('test-app.db')
    create_table(sqlite)
    insert(sqlite, 'productos')

def insert(sqlite, table):
    sqlite.insert(table) \
        .row(
            ['id', 'apellido'],
            ['1', 'Doe']
        )

def create_table(sqlite):
    ''' Crea una tabla'''

    table = sqlite.create_table('productos')
    table.column('id')
    table.column('nombre', 'TEXT', 20)
    table.column('apellido')
    table.query()

if __name__ == "__main__":
    main()



