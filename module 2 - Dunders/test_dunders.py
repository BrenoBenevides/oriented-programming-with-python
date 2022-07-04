class Book:

    def __init__(self, author, name, pages):
        self.author = author
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Author: {self.author} Name: {self.name} Pages: {self.pages}'

    def __repr__(self):
        return f"Book('{self.author}','{self.name}','{self.pages}')"

    def __format__(self, format_spec):
        if format_spec == 'short':
            return f'Book Name: {self.name}'
        else:
            return f"""Book Name {self.name} 
                       by {self.author}
                       with {self.pages} pages
                    """
    def __eq__(self, other):
        return (self.author == other.author) and (self.name == self.name) and (self.pages) == self.pages

    def __hash__(self):
        return hash((self.author,self.pages,self.name))

instance = Book('Hayek', 'o caminho da servidao',250)
instance2 = Book('Hayek', 'o caminho da servidao',250)

print('instance1',hash(instance),
      'instance2',hash(instance2))


print(instance == instance2)
# print('instance',instance)
# print('new instance',eval(repr(instance)))
# print('instance formated: {:short}'.format(instance))

