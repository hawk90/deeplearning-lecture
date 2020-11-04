class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def getTitle(self):
        return self.title

    def getAuthor(self):
        return self.author


book1 = Book('Convex', 'Boyd')
book2 = Book('Deep Learning', 'Ian')

print(book1.getTitle(), book1.getAuthor())
print(book2.getTitle(), book2.getAuthor())