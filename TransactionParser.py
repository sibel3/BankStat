import LexicalManager
import csv

class TransactionParser : 
    def __init__(self):
        print("Creating parser")
        self.lexicalManager = LexicalManager.LexicalManager()
        self.categories = self.lexicalManager.parse_categories()

    def analyse_transaction(self, filename):
        with open(filename, encoding="utf-8", errors='ignore') as csvFile:
            csvReader = csv.reader(csvFile, delimiter=",")
            for category in self.categories:
                sum = 0
                for row in csvReader:
                    if (self.lexicalManager.is_part_of_category(category,row[3])):
                        sum = sum + float(row[2])
                        print(row[3])
                print("sum of {} is {}".format(category, sum))

    def exit():
        self.lexicalManager.exit()

if __name__ == "__main__":
    transac = TransactionParser()
    transac.analyse_transaction("06252021_Transactions.csv")