import psycopg2
import psqlConfig_web


class BestSellersAPI:
    
    def __init__(self):
        try:
            self.conn = psycopg2.connect(database = psqlConfig_web.database, user = psqlConfig_web.username, password = psqlConfig_web.password, host="localhost")
            print("database opened successfully")
        except(Exception, psycopg2.Error) as error:
            print("Error connecting to PostgreSQL", error)
    
    def cursor_init(self):
        try:
            curr = self.conn.cursor()
            return curr
        except(Exception, psycopg2.Error) as error:
            print("Error connecting to PostgreSQL", error)
            return(error)

    def formatTuples(self, tupList):
        formattedList = []
        for i in tupList:
            formattedList.append(i[0])
        return formattedList
    
    def numIsGreaterThanZero(self, number):
        if int(number) <= 0:
            return False
        return True
   
    def isValidYearRange(self, yearStart, yearEnd):
        if(yearStart > yearEnd):
            return False
        elif(yearStart < 1931 or yearStart > 2020):
            return False
        elif(yearEnd < 1931 or yearEnd > 2020):
            return False
        return True
        
    def getBestsellersGivenYearRange(self, yearStart, yearEnd):
        """Gets list of books on the bestseller list during a given year range.
        Args:
            yearStart (int): The first year of interest
            yearLast (int): The last year of interest

        Returns:
            bestSellers (list): a list of the best selling books
        """
        
        if not self.isValidYearRange(yearStart, yearEnd):
            return "invalid year range"
        
        curr = self.cursor_init()
        
        curr.execute("SELECT DISTINCT title FROM weekRankings WHERE EXTRACT(year FROM week) BETWEEN %s AND %s ORDER BY title;", (yearStart, yearEnd))

        result = curr.fetchall()
        curr.close()
        formattedBestsellers = self.formatTuples(result)
        return formattedBestsellers
   
    def getNumberOneBestsellersGivenYearRange(self, yearStart, yearEnd):
        """Gets list of books that are ranked number one on the bestseller list.
        Args:
            yearStart (int): The first year of interest
            yearLast (int): The last year of interest

        Returns:
            NumberOneBestSellers (list): a list of the number one best selling books in the range
        """
        
        if not self.isValidYearRange(yearStart, yearEnd):
            return "invalid year range"
            
        curr = self.cursor_init()

        
        curr.execute("SELECT DISTINCT title FROM weekRankings WHERE EXTRACT(year FROM week) BETWEEN %s AND %s AND ranking = 1;", (yearStart, yearEnd))
        result = curr.fetchall()
        curr.close()
        formattedNumberOneBestsellers = self.formatTuples(result)
        return formattedNumberOneBestsellers       

    def getBooksByAuthor(self, author):
        """Gets all the books written by a specific author
        Args:
            author(str): The name of the author to search for
        Returns:
            list: a list of books on the bestseller list written by the given author
        """

        curr = self.cursor_init()
        author = author.upper()
        authorWildcard = "".join(["%", author, "%"])
        curr.execute("SELECT author, title FROM bestsellersInfo WHERE author LIKE %s ORDER BY author;", (authorWildcard,))
        result = curr.fetchall()
        curr.close()
        if not result:
            return "None"
        return (result)


    def getNumAuthorsWithMostBooks(self, numAuthors):
        """Returns a list of authors with more than the input number of books on the bestseller list
         Args:
        numBooks(int): the number of books to limit by

        Returns:
        list: authors with more than numBooks books on the bestseller list
        """

        if not self.numIsGreaterThanZero(numAuthors):
            return "invalid value"
            
        curr = self.cursor_init()
    
        curr.execute("SELECT DISTINCT author, numBestsellers FROM bestsellersperauthor ORDER BY numBestsellers DESC LIMIT %s ;", (numAuthors, ))
        result = curr.fetchall()
        curr.close()
        
        if not result:
            return "no authors have more than {} books on the bestseller list".format(numAuthors)
            
        
        return result

    def getLongestRunningBooks(self, topNum):
        """Returns given number of books that ran for longest number of weeks.

        Returns:
            List of topNum books that ran for the longest number of weeks e.g. top ten longest running books
        """
        
        if not self.numIsGreaterThanZero(topNum):
            return "invalid value"
            
        curr = self.cursor_init()

        curr.execute("SELECT title, total_weeks FROM bestsellersInfo ORDER BY total_weeks DESC LIMIT %s ;", (topNum, ))
        result = curr.fetchall()
        curr.close()

        if not result:
            return "No books have been running for that long"

        return result
        
    def isBestseller(self, bookName):
        """Prints true if the given book is a bestseller
        Args:
            bookName (str): The fname of the book to search for

        Returns:
            bool: either true if the given book is a bestseller or false if the given book is not a bestseller
        """
        curr = self.cursor_init()
        bookName = bookName.upper()

        curr.execute("SELECT * FROM bestsellersInfo WHERE title LIKE %s;", (bookName,))
        result = curr.fetchall()
        curr.close()
        if not result:
            return False
        return True

    def getBookInfo(self, bookName):
        """Gets the information for a given book
        Args:
            bookName (str) : The name of a book

        Returns:
            dictionary: fields: author, rank, weeks, date.
            The rank is the highest rank reached, weeks is the number of weeks it was on the list,
            the date is the first time it appeared on the list
        """
        bookName = bookName.upper()
        bookNameWildcard = "".join(["%", bookName, "%"])

        if not self.isBestseller(bookNameWildcard):
            return "None"

        curr = self.cursor_init()
        curr.execute("SELECT title, author, bestRank, total_weeks, first_week FROM bestsellersInfo WHERE title=%s;", (bookName,))
        result = curr.fetchall()
        if not result:
            curr.execute("SELECT title, author, bestRank, total_weeks, first_week FROM bestsellersInfo WHERE title LIKE %s;", (bookNameWildcard,))
            result = curr.fetchall()
        curr.close()
        return result

if __name__ == "__main__":
    bestsellers = BestSellersAPI()
    bestsellers.conn.close()