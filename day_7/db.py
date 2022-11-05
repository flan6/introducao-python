import sqlite3

class DB:
    _database = None

    def __init__(self, path_to_db):
        self._database = sqlite3.connect(path_to_db)


    def ler_do_banco(self, query):
        cursor = self._database.cursor()

        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()

        return result
