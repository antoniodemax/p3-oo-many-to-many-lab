class Author:
    pass
    authors = []

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise Exception("name is invalid")

    def contracts(self):
        pass
        return [contract for contract in Contract.contracts if contract.author == self]

    def books(self):
        pass
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        pass
        contract = Contract(self, book, date, royalties)
        return contract

    def total_royalties(self):
        pass
        sum = 0
        for contract in self.contracts():
            sum += contract.royalties
        return sum


class Book:
    pass
    books = []

    def __init__(self, title):
        self.title = title
        Book.books.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str):
            self._title = title
        else:
            raise Exception("title is invalid")

    def contracts(self):
        pass
        return [contract for contract in Contract.contracts if contract.book == self]

    def authors(self):
        pass
        return [contract.author for contract in self.contracts()]


class Contract:
    pass
    contracts = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        pass
        return [contract for contract in cls.contracts if contract.date == date]

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if isinstance(author, (Author)):
            self._author = author
        else:
            raise Exception("author is invalid")

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, book):
        if isinstance(book, (Book)):
            self._book = book
        else:
            raise Exception("book is invalid")

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if isinstance(date, str):
            self._date = date
        else:
            raise Exception("date is invalid")

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, royalties):
        if isinstance(royalties, int):
            self._royalties = royalties
        else:
            raise Exception("royalties is invalid")