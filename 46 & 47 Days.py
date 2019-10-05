 # ________________ 46 & 47 Days ______________ #
 
class library:
    def __init__(self, book, shelf):
        self.book = book
        self.shelf = shelf

    def printinfo(self):
        print(self.book, self.shelf)


class scienceSection(library):
    def __init__(self,book,shelf, name):
        super().__init__(book,shelf)
        self.name = name

    def printinfo(self):
        print("number of book is ", self.book,
              "numbers of shelf is ", self.shelf ,
              "the name of book is", self.name)


x = scienceSection(20,4,"phsics")
x.printinfo()
