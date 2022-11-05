import csv

class CSV:
    def read(self, file_path):
        with open(file_path, 'r') as f:
            reader = csv.reader(f, delimiter=',')
            return [row for row in reader]


    def write(self, file_path, data):
        with open(file_path, 'a') as f:
            writer = csv.writer(f)
            writer.writerows(data)
