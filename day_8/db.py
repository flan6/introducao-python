import sqlite3

class DB:
    _database = None

    def __init__(self, path_to_db):
        self._database = sqlite3.connect(path_to_db)


    def Select(self, table: str, columns: str, condition: str) -> list:
        query = f"SELECT {columns} FROM {table} WHERE {condition}"

        cursor = self._database.cursor()

        try:
            cursor.execute(query)
            result = cursor.fetchall()

        except Exception as e:
            print(f"an error occured in the SELECT: {e}")
            return

        finally:
            cursor.close()

        return result

    def Insert(self, table: str, columns: str, obj):
        values = ""
        for _ in columns:
             values += "?, "

        query = f"INSERT INTO {table}({columns}) VALUES({values})"

        cursor = self._database.cursor()

        try:
            cursor.executemany(query, obj)
            self._database.commit()

        except Exception as e:
            print(f"an error occured {e}")
            self._database.rollback()
            return

        finally:
            cursor.close()

        return cursor.lastrowid

    def Delete_by_id(self, table: str, id: int):
        query = f"DELETE FROM {table} WHERE id = (?)"
        cursor = self._database.cursor()

        try:
            cursor.execute(query, str(id))
            self._database.commit()

        except Exception as e:
            print(f"an error occured {e}")
            self._database.rollback()

        finally:
            cursor.close()

    def Update_by_id(self, table: str, columns: list, values: list, id: int):
        set_values = ""
        for column in columns:
            set_values += f"`{column}` = (?)"

        query = f"UPDATE {table} SET {set_values} WHERE id = {id}"
        cursor = self._database.cursor()

        try:
            cursor.execute(query, values)
            self._database.commit()

        except Exception as e:
            print(f"an error occured {e}")
            self._database.rollback()

        finally:
            cursor.close()
