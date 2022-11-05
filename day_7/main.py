from csv_wraper import CSV
from db import DB

class main():
    c = CSV()
    banco = DB(__file__.removesuffix("main.py") + "db/chinook.db")

    def main(self):
        file_path = __file__.removesuffix("main.py") + "csv/albums.csv"

        # # lista_do_csv = self.c.read(file_path)
        # # print(lista_do_csv)

        # self.c.write(file_path, [['ian', '27', 'estudante'], ['higor', '27', 'auxiliar administrativo']])

        # lista_do_csv = self.c.read(file_path)
        # print(lista_do_csv)

        # print(type(lista_do_csv[1][1]))

        result = self.banco.ler_do_banco("SELECT * FROM albums")
        print(result[1])

        try:
            result[1][1] = "batata"
            print(result[1])
        except TypeError:
            print("nao deixou :(")

        # self.c.write(file_path, result)



if __name__ == '__main__':
    m = main()
    m.main()
