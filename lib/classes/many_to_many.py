class Article:
    all = [] 

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise Exception("Invalid author instance.")
        if not isinstance(magazine, Magazine):
            raise Exception("Invalid magazine instance.")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise Exception("Title must be a string between 5 and 50 characters.")
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)  

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        raise AttributeError("Article title is immutable.")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Invalid author instance.")
        self._author = value

    @property
    def magazine(self):
        # retrives the magazine the article is published in
        return self._magazine

    @magazine.setter
    #  ensures the new value is an instance of the magazine
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise Exception("Invalid magazine instance.")
        self._magazine = value


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Name must be a non-empty string.")
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("Author name is immutable.")

    def articles(self):
        # retrives all articles written by this author
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        # retrives all magazines the author has contributed to
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        # add a new article authored by the author
        if not isinstance(magazine, Magazine):
            raise Exception("Invalid magazine instance.")
        return Article(self, magazine, title)

    def topic_areas(self):
        # retrives unique topic areas covered by articles written by this author
        return list({magazine.category for magazine in self.magazines()}) or None


class Magazine:
    all = []  

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise Exception("Name must be a string and between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise Exception("Category must be a string and more than 0 characters.")
        self._name = name
        self._category = category
        Magazine.all.append(self)  
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise Exception("Name must be a string between 2 and 16 characters.")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise Exception("Category must be a string amd more than 0 characters.")
        self._category = value

    def articles(self):
        # retrives all articles associated with this magazine
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        # retrives all authors associated with this magazine
        return list({article.author for article in self.articles()})

    def article_titles(self):
        # retrives titles of all articles associated with this magazine
        return [article.title for article in self.articles()] or None

    def contributing_authors(self):
        # retrives authors who contributed more than 2 articles for this magazine
        authors = [article.author for article in self.articles()]
        return [author for author in set(authors) if authors.count(author) > 2] or None

    @classmethod
    def top_publisher(cls):
        # finds the magazine with the most articles
        if not cls.all:
            return None
        return max(cls.all, key=lambda magazine: len(magazine.articles()))