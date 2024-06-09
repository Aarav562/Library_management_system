class Patron:
    all =[]
    def __init__(self,name:str,reg_no:str,branch:str,section=0):
        assert section>0 , f"The Given Section {section} is not valid"
        self.__name = name
        self.__reg_no = reg_no
        self.__branch = branch
        self.__section = section
        self.books_borrowed = []
        Patron.all.append(self)

    @property 
    def name(self):
        return self.__name

    @property
    def reg_no(self):
        return self.__reg_no
    
    @property
    def branch(self):
        return self.__branch
    
    @property
    def section(self):
        return self.__section

    
    def borrow_books(self,book):
        if book not in self.books_borrowed:
            self.books_borrowed.append(book)
            book.check_out(self)



    def return_books(self,book):
        self.books_borrowed.remove(book)
        book.check_in()
               
    def __repr__(self):
        val = len(self.books_borrowed)
        return f"{self.__class__.__name__}({self.__name},{self.__reg_no},{self.__branch},{self.__section},Books_borrowed = {val}"

class Book:
    id_counter = 1
    all = []
    def __init__(self,name:str,author:str,id = 0):
        self.__name = name
        self.__author = author
        self.__id = Book.id_counter
        self.books_present = []
        self.books_lent = []
        Book.id_counter +=1
        Book.all.append(self)

    @property
    def name(self):
        return self.__name
    
    @property
    def author(self):
        return self.__author
    
    @property
    def id(self):
        return self.__id
    
    
    def check_in(self):
        self.books_present.append(self)
        if self in self.books_lent:
            self.books_lent.remove(self)

    def check_out(self, paetron):
        if self in self.books_present:
            self.books_present.remove(self)
            self.books_lent.append(self)
            paetron.borrow_books(self)



    def __repr__(self):
        is_present = self in self.books_present
        return f"{self.__class__.__name__}({self.name},{self.author},{self.id},Status: {'Present' if is_present else 'Lent Out'}"
    

