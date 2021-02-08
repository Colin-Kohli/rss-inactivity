from re import split
import unittest
import pip
import feedparser
import datetime
import logging


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

    # A blank dictionary which will eventually hold company names paired with URLs which have not been updated in 'minimium_days_inactive' days
    inactive_companies = {}

    # Will will capture the date just once and pass it to other functions rather than calling it every time we need to do a date calculation
    today = datetime.datetime.today()

    for company in rss_dict:
        feed_urls = rss_dict[company]
        for url in feed_urls:
            feedFound = False
            try:
                feed = feedparser.parse(url)
                feedFound = True
            except:
                logging.warn(
                    "Exception while parsing feed. If the root certificates of your default python installation have not been updated, please install new certificates")

            # Dont love the structure here, will try to find a way to reorder this exception block

            if(feedFound):
                days_inactive = days_since_last_update(feed, today)
                if days_inactive >= minimum_days_inactive:
                    if company in inactive_companies:
                        inactive_companies[company].append(url)
                    else:
                        inactive_companies[company] = [url]

    return inactive_companies


def days_since_last_update(feed, today):

    # NEED TO CATCH IF DATE ITEM DOESNT EXIST LIKE WITH THAT ONE PODCAST

    # dates have a strange format, with items seperated by spaces. split the items by spaces, then build a datetime object so we can do date arithmetic
    split_date = feed["feed"]["published"].split(" ")
    day = split_date[1]
    if len(day) == 1:
        day = "0" + day  # the number of digits on the day of the month is irregular, so add a leading zero if just one digit
    month = split_date[2]
    year = split_date[3]
    hour_minute_second = split_date[4]

    last_post_date = datetime.datetime.strptime(
        day + month + year + hour_minute_second, "%d%b%Y%H:%M:%S")  # build datetime object

    # return day difference between most recent date and today
    return (today - last_post_date).days


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


print(get_rss_inactivity(
    {'Unraveled': ['https://rss.acast.com/unraveled']}, 10))
