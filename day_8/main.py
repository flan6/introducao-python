from csv_wraper import CSV
from db import DB

class main():
    c = CSV()
    banco = DB(__file__.removesuffix("main.py") + "db/chinook.db")

    def main(self):
        file_path = __file__.removesuffix("main.py") + "csv/a.csv"

        artist_csv = self.c.read(file_path)

        self.banco.Update_by_id("albums", ["Title"], ["Monkeys in Pijamas"], 2)

        self.banco.Delete_by_id("albums", 3)

if __name__ == '__main__':
    main().main()
