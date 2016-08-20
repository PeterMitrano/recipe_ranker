from fuzzywuzzy import fuzz

GOOD_ENOUGH_RATIO = 75

def search(keywords, recipes):
    """ recipes is an array of recipe dicts, returns a list of recipes that match """
    matching_items = []
    for item in recipes:
        recipe_name = item['Title']
        ratio = fuzz.partial_token_set_ratio(keywords, recipe_name)
        if ratio > GOOD_ENOUGH_RATIO:
            matching_items.append(item)

    return matching_items
