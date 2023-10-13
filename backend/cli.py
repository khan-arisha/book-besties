import api

def printContext():
    print("Welcome!")
    print("Our database contains info about the New York Times besteller lists from 1931 to 2020.")
    print("Each week we noted down the top ranked books.")
    print("For each title, we have recorded the author, the best rank it achieved, the first rank it ever achieved, ")
    print("and the total number of weeks it has been on the list.")
    print("Now, let's have some fun with this data!")
    print("What do you want to find out?")

def printOptions():
    print("These are your choices: ")
    print("1. Get the bestsellers in a given year range")
    print("2. Get the number one bestsellers in a given year range")
    print("3. Get all books on the bestseller list by a given author")
    print("4. Get a list of authors with more than a certain number of books on the bestseller list")
    print("5. Get a list of given length of the longest-running books")
    print("6. Check if a book is on the bestseller list")
    print("7. Get information about a given book")

def goAgain():
    print("Now you get to choose again. YAY \n")

def getChoice():
    choice = input("Make a new choice (1-7) or enter STOP to quit: ")
    choice = choice.upper()
    return choice
        

api = api.BestSellersAPI()

printContext()
printOptions()
functionToTest = getChoice()
while functionToTest != "STOP":
    if(functionToTest == "1"):
        yearStart = int(input("Enter a starting year "))
        yearEnd = int(input("Enter an end year "))
        print("The best selling books between ", yearStart, " and ", yearEnd, " are ", api.getBestsellersGivenYearRange(yearStart, yearEnd), "\n")
        
    elif(functionToTest == "2"):
        yearStart = int(input("Enter a starting year "))
        yearEnd = int(input("Enter an end year "))
        print("The number one best selling books between ", yearStart, " and ", yearEnd, " are ", api.getNumberOneBestsellersGivenYearRange(yearStart, yearEnd), "\n")

    elif(functionToTest == "3"):
        author = input("Enter the name of an author ")
        print("These are all the books written by " + author +": ", api.getBooksByAuthor(author) , "\n")

    elif(functionToTest == "4"):
        numBooks = int(input("Enter a number of books "))
        print("Authors with more than ", numBooks, " books on the bestseller list are ", api.getAuthorsWithMoreThanNumBooks(numBooks), "\n")

    elif(functionToTest == "5"):
        topNum = int(input("Enter the number of longest running books you want to see "))
        print("The top ", topNum, " books of all time are: ", api.getLongestRunningBooks(topNum), "\n")

    elif(functionToTest == "6"):
        bookName = input("Enter a book title ")
        if(api.isBestseller(bookName)):
            print("This book is a bestseller\n")
        else:
            print("This book is not a bestseller\n")

    elif(functionToTest == "7"):
        bookName = input("Enter a book title ")
        bookInfo = api.getBookInfo(bookName)
        if type(bookInfo) != str:
            print("The author is {}".format(bookInfo[0]))
            print("The highest rank it reached was {}".format(bookInfo[1]))
            print("The total weeks it was on the list is {}".format(bookInfo[2]))   
            print("The date the book was first on the list is {}\n".format(bookInfo[3]))   
        else:
            print(bookInfo)
            
    goAgain()
    printOptions()
    functionToTest = getChoice()


    

