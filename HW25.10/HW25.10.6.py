class book:
    def __init__(self, pages):
        self.pages = pages
    def __str__(self):
        return  self.pages
    def __len__(self):
        return self.pages

book1 = book(213)
length1 = len(book1)
book2 = book(98)
length2 = len(book2)
print (length1, length2)