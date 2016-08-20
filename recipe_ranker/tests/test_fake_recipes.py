import unittest

from recipe_ranker.tests import test_util
from recipe_ranker import ranker

class ResultsTest(unittest.TestCase):
    TEST_RECIPES = [
        {"RecipeId": 0, "Title": "chicken teriyaki with snap peas"},
        {"RecipeId": 1, "Title": "simple buttermilk pancakes"},
        {"RecipeId": 2, "Title": "chocolate chip pancakes"},
        {"RecipeId": 3, "Title": "fried chicken and waffles"},
        {"RecipeId": 4, "Title": "buttermilk biscuits"},
        {"RecipeId": 5, "Title": "cheddar and broccolli soup"},
        {"RecipeId": 5, "Title": "fish stew with tomatoes"},
        {"RecipeId": 6, "Title": "garlic bread"},
    ]

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

