import flask
from flask import render_template, request
import json
import sys
import api_web

app = flask.Flask(__name__)

# This line tells the web browser to *not* cache any of the files.
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('aboutTheData.html')

@app.route('/search')
def search():
    api = api_web.BestSellersAPI()
    return render_template('searchTheData.html')


@app.route('/longest-running', methods=['POST'])
def searchResult():
    formResults = request.form
    numberBooksWantToSee = formResults['numBooks']
    api = api_web.BestSellersAPI()
    databaseResult = api.getLongestRunningBooks(numberBooksWantToSee)
    result = [databaseResult, formResults]
    return render_template('longestRunning.html', results=result)

@app.route('/book-info', methods=['POST'])
def bookInfoResult():
    formResults = request.form
    bookTitle = formResults['title']
    api = api_web.BestSellersAPI()
    databaseResult = api.getBookInfo(bookTitle)
    result = [databaseResult, formResults]
    if(result[0] == "None"):
        return render_template('badTitleRequest.html')
    if len(result[0]) == 1:
        return render_template('bookInfo.html', results=result[0][0])
    else:
        return render_template('matchBookTitles.html', results=result)

@app.route('/bestsellers-year', methods=['POST'])
def searchResult2():
    formResults = request.form
    yearStart = int(formResults['yearStart'])
    yearEnd = int(formResults['yearEnd'])
    api = api_web.BestSellersAPI()
    databaseResult = api.getBestsellersGivenYearRange(yearStart, yearEnd)
    result = [databaseResult, formResults]
    return render_template('bestsellersGivenYearRange.html', results=result)

@app.route('/number-one-bestsellers-given-year', methods=['POST'])
def searchResult3():
    formResults = request.form
    yearStart = int(formResults['yearStart'])
    yearEnd = int(formResults['yearEnd'])
    api = api_web.BestSellersAPI()
    databaseResult = api.getNumberOneBestsellersGivenYearRange(yearStart, yearEnd)
    result = [databaseResult, formResults]
    return render_template('numOneBestsellersGivenYearRange.html', results=result)

@app.route('/top-authors', methods=['POST'])
def searchResult4():
    formResults = request.form
    numberBooksWantToSee = formResults['numAuthors']
    api = api_web.BestSellersAPI()
    databaseResult = api.getNumAuthorsWithMostBooks(numberBooksWantToSee)
    result = [databaseResult, formResults]
    return render_template('authorsWithMostBooks.html', results=result)


@app.route('/books-by-author', methods=['POST'])
def searchResult5():
    formResults = request.form
    authorToDisplay = formResults['author']
    api = api_web.BestSellersAPI()
    databaseResult = api.getBooksByAuthor(authorToDisplay)
    if(databaseResult == "None"):
        return render_template('badAuthorRequest.html')
    result = [databaseResult, formResults]
    return render_template('booksByAuthor.html', results=result)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=port)
