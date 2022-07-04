# Dunders
Dunders are used to perform "magical" operations within our classes.

### 1) Dunder repr

It's used to modify the way the class is returned. Instead of showing the class
type and position in memory,it shows something different.

```python

class Book:
    def __repr__(self):
        return 'Instance of type book}'
```

In a print operation,for example,this will return 'instance of type book'

### 2) Dunder str
It's modifies the class return when a print operation is called.

```python

class Book:
    
    def __init__(self,author,name,pages):
        self.author = author
        self.name = name
        self.pages = pages
        
    def __str__(self):
        return f'Author: {self.author} Name: {self.name} Pages: {self.pages}'
```

In a print operation,this will return ``author``, ``book name`` and ``amount of pages``.

The difference between __str__ and __repr__ is very smoothly. Repr is recommended to use to create a new class with the same parameters as shown below.

```python

class Book:
    
    def __init__(self,author,name,pages):
        self.author = author
        self.name = name
        self.pages = pages
        
    def __str__(self):
        return f'Author: {self.author} Name: {self.name} Pages: {self.pages}'
    
    def __repr__(self):
        return f'Book({self.author},{self.name},{self.pages})'

```
### 3) Dunder format
It's used when the class instance is called in a format operation

```python

class Book:
    
    def __init__(self,author,name,pages):
        self.author = author
        self.name = name
        self.pages = pages
        
    def __str__(self):
        return f'Author: {self.author} Name: {self.name} Pages: {self.pages}'
    
    def __repr__(self):
        return f'Book({self.author},{self.name},{self.pages})'
    
    def __format__(self, format_spec):
        if format_spec == 'short':
            return f'Book Name: {self.book}'
        else:
            return f"""Book Name {self.book} 
                       by {self.author}
                       with {self.pages} pages
                    
                    """

instance = Book('Hayek', 'o caminho da servidao',250)
print(f'book info\n {instance}')
```

### 4) Dunder hash
It's used to avoid different hash values when a class instance has the same attributes than another.

For example:

````python
instance1 = Book('Hayek', 'o caminho da servidao',250)
instance2 = Book('Hayek', 'o caminho da servidao',250)
````

Authougth both instances has the same attributes if we compare the hashes,the values will be different.

But if we do the following the comparasion will be True.

````python
class Book:
    
    def __init__(self,author,name,pages):
        self.author = author
        self.name = name
        self.pages = pages
        
    def __str__(self):
        return f'Author: {self.author} Name: {self.name} Pages: {self.pages}'
    
    def __repr__(self):
        return f'Book({self.author},{self.name},{self.pages})'
    
    def __format__(self, format_spec):
        if format_spec == 'short':
            return f'Book Name: {self.book}'
        else:
            return f"""Book Name {self.book} 
                       by {self.author}
                       with {self.pages} pages
                    
                    """
        
    def __hash__(self):
        return hash((self.author,self.name,self.pages,self))

instance1 = Book('Hayek', 'o caminho da servidao',250)
instance2 = Book('Hayek', 'o caminho da servidao',250)

hash(instance1) == hash(instance2) -> True
````
