import unittest

from recipe_ranker import ranker

class ResultsTest(unittest.TestCase):
    TEST_RECIPES = [
        {"id": 0, "name": "chicken teriyaki with snap peas"},
        {"id": 1, "name": "simple buttermilk pancakes"},
        {"id": 2, "name": "chocolate chip pancakes"},
        {"id": 3, "name": "fried chicken and waffles"},
        {"id": 4, "name": "buttermilk biscuits"},
        {"id": 5, "name": "cheddar and broccolli soup"},
        {"id": 5, "name": "fish stew with tomatoes"},
        {"id": 6, "name": "garlic bread"},
    ]

    def test_no_match(self):
        recipes = ranker.search("pancakes", self.TEST_RECIPES)
        self.assertEqual(len(recipes), 2)



