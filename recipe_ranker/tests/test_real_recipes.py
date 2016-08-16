
import unittest

from recipe_ranker import ranker

class ResultsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.TEST_RECIPES = ""

    def test_no_match(self):
        recipes = ranker.search("southwest bean burritos", self.TEST_RECIPES)
        self.assertEqual(len(recipes), 0)

    def test_few_match(self):
        recipes = ranker.search("pancakes", self.TEST_RECIPES)
        self.assertEqual(len(recipes), 2)

        recipes = ranker.search("chicken", self.TEST_RECIPES)
        self.assertEqual(len(recipes), 2)

    def test_one_match(self):
        recipes = ranker.search("biscuits", self.TEST_RECIPES)
        self.assertEqual(len(recipes), 1)
