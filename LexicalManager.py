import json

class LexicalManager :
    def __init__(self):
        self.lexicalFileName = "lexical.json"
        self.jsonFile = open(self.lexicalFileName, "r")
        print("Opening Lexical")
        self.lexicalData = json.load(self.jsonFile)

    def parse_categories(self):
        return self.lexicalData.keys()

    def is_part_of_category(self, category, description):
        for i in self.lexicalData[category]:
            if (description.lower().find(i.lower()) != -1):
                return True
        return False

    def add_category(self, category):
        for i in self.parse_categories():
            if (category.lower() == i.lower()):
                print("this category already exist")
                return
        self.lexicalData[category.lower()] = {}
        self.dump_data()

    def add_word(self, category, word):
        isCategoryFound = False;
        for i in self.parse_categories():
            if (category.lower() == i.lower()):
                print("this category already exist")
                isCategoryFound = True
        if not isCategoryFound:
            print("Category is not found")
            return;
            
        self.lexicalData

    def dump_data(self):
        self.jsonFile.close()
        self.jsonFile = open(self.lexicalFileName, "w")
        newJson = json.dump(self.lexicalData, self.jsonFile)
        self.jsonFile.close()
        self.jsonFile = open(self.lexicalFileName, "r")

    def exit(self):
        self.jsonFile.close()

if __name__ == "__main__":
    lex = LexicalManager()
    lex.parse_categories()
    lex.add_category("Resto")
    if lex.is_part_of_category("Groceries", "tim"): 
        print("test successfull")

