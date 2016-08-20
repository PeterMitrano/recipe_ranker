import boto3
import unittest

from recipe_ranker.tests import test_util
from recipe_ranker import ranker

@test_util.wip
class ResultsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        dynamodb = boto3.resource('dynamodb') # the real thing
        table = dynamodb.Table('my_cookbook_recipes')
        cls.response = table.scan()
        cls.TEST_RECIPES = cls.response['Items']

    def test_setup(self):
        self.assertEqual(self.response['ResponseMetadata']['HTTPStatusCode'], 200)
        self.assertGreater(len(self.TEST_RECIPES), 1)

    def test_no_match(self):
        recipes = ranker.search("llamas not a recipe", self.TEST_RECIPES)
        self.assertEqual(len(recipes), 0)

    def test_at_least_one_exists(self):
        recipes = ranker.search("pancakes", self.TEST_RECIPES)
        self.assertGreaterEqual(len(recipes), 1)

        recipes = ranker.search("chicken", self.TEST_RECIPES)
        self.assertGreaterEqual(len(recipes), 1)
