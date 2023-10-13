import unittest
import datetime
from api import *

class APITester(unittest.TestCase):
    
    def setUp(self):
        self.bst = BestSellersAPI()

    def test_bestsellers_given_year_range(self):
        self.assertEqual(len(self.bst.getBestsellersGivenYearRange(1932, 1932)), 48)
        self.assertEqual(len(self.bst.getBestsellersGivenYearRange(2001, 2002)), 292)
        self.assertEqual(self.bst.getBestsellersGivenYearRange(1932, 2021), "invalid year range")
        self.assertEqual(self.bst.getBestsellersGivenYearRange(1700, 2020), "invalid year range")
        self.assertEqual(self.bst.getBestsellersGivenYearRange(1935, 1932), "invalid year range")
    
    def test_get_number_one_bestsellers_given_year_range(self):
        self.assertEqual(len(self.bst.getNumberOneBestsellersGivenYearRange(1932, 1932)), 18)
        self.assertEqual(len(self.bst.getNumberOneBestsellersGivenYearRange(2001, 2002)), 45)
        self.assertEqual(self.bst.getNumberOneBestsellersGivenYearRange(1932, 2021), "invalid year range")
        self.assertEqual(self.bst.getNumberOneBestsellersGivenYearRange(1700, 2020), "invalid year range")
        self.assertEqual(self.bst.getNumberOneBestsellersGivenYearRange(1935, 1932), "invalid year range")
         
    def test_get_books_by_author(self):
        self.assertEqual(self.bst.getBooksByAuthor('SELMA VANGSTEIN'), "This author has no books on the list")
        self.assertEqual(len(self.bst.getBooksByAuthor('Hervey Allen')), 5)
        self.assertEqual(len(self.bst.getBooksByAuthor('HERVEY ALLEN')), 5)

    def test_get_authors_with_more_than_num_books(self):
        self.assertEqual(len(self.bst.getAuthorsWithMoreThanNumBooks(115)), 1)
        self.assertEqual(self.bst.getAuthorsWithMoreThanNumBooks(-5), "invalid value")
        self.assertEqual(self.bst.getAuthorsWithMoreThanNumBooks(1150), "no authors have more than 1150 books on the bestseller list")
    
    def test_get_longest_running_books(self):
        self.assertEqual(len(self.bst.getLongestRunningBooks(3)), 3)
        self.assertEqual(self.bst.getLongestRunningBooks(0), "invalid value")
        self.assertEqual(self.bst.getLongestRunningBooks(-1), "invalid value")
        self.assertEqual(len(self.bst.getLongestRunningBooks(1000000000)), 7431)
        
    def test_is_bestseller(self):
        self.assertTrue(self.bst.isBestseller('THE TEN COMMANDMENTS'))
        self.assertTrue(self.bst.isBestseller('Inside, Outside'))
        self.assertFalse(self.bst.isBestseller('FANTASTIC FISH'))
    
    def test_get_book_info(self):
        self.assertEqual(self.bst.getBookInfo('CHAOS'), ('PATRICIA CORNWELL', 7, 3, datetime.date(2016, 12, 4)))
        self.assertEqual(self.bst.getBookInfo('FANTASTIC FISH'), "This book is not on the bestseller list")

        
if __name__ == "__main__":
    unittest.main()