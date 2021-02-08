import unittest
import pip


def import_or_install_packages():
    try:
        __import__('feedparser')
    except ImportError:
        pip.main(['install', 'feedparser'])


def get_rss_inactivity(rss_dict, minimum_days_inactive):
    '''
     Identifies companies which have had no rss activity for a given number of days. 

    This function takes a dictionary from company names to company RSS feed, and selects the companies which have not added to their feed in some number of days. 
    As the return type is unspecified by the buisness requirments, the function will return a dictionary. 
    The return dictionary is keyed by companies whose feeds have lapsed for the given amount of days, and valued by the respective URLs of those feeds.

    Parameters:
    rss_dict (dict of str: list[str]): A dictionary keyed from the string of a company's name and valued to a list of some amount of RSS feed URL strings.

    miniumum_days_inactive (int): The number of days a feed must be inactive for to be returned by the function. 

    '''

    # Assert all function arguments to be passed in as expected
    sanity_check(rss_dict, minimum_days_inactive)

    # Import packages needed for this program, and install them if they are not present
    import_or_install_packages()

    # A blank dictionary which will eventually hold company names paired with URLs which have not been updated in 'minimium_days_inactive' days
    inactive_companies = {}

    for company in rss_dict:
        feed_urls = rss_dict[company]

    return inactive_companies


def sanity_check(rss_dict, minimum_days_inactive):
    assert isinstance(
        rss_dict, dict), "Argument of wrong type! Type 'dictionary' required as first argument for fuction get_rss_inactivity"

    assert rss_dict != {}, "First argument 'rss_dict' should not be empty"

    assert isinstance(
        rss_dict, dict), "Argument of wrong type! Type 'dictionary' required as first argument for fuction get_rss_inactivity"

    assert isinstance(rss_dict[list(rss_dict.keys())[
        0]], list), "Argument of wrong type! Type 'List' required as value argument for dictionary 'rss_dict'"

    assert rss_dict[list(rss_dict.keys())[0]] != [
    ], "Value list in 'rss_dict' should not be empty"

    assert isinstance(rss_dict[list(rss_dict.keys())[
        0]][0], str), "Argument of wrong type! Type 'String' required as item in value list for dictionary 'rss_dict'"

    assert isinstance(minimum_days_inactive,
                      int), "Argument of wrong type! Type 'int' required as second argument for fuction get_rss_inactivity"

    assert minimum_days_inactive >= 0, "Minimum days inactaive must be a non-negative integer"


get_rss_inactivity({'a': ['1']}, 1)
