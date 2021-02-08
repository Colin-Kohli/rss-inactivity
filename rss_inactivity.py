def get_rss_inactivity(rss_dict, minimum_days_inactive):
    '''
     Identifies companies which have had no rss activity for a given number of days. 

    This function takes a dictionary from company names to company RSS feed, and selects the companies which have not added to their feed in some number of days. 
    As the return type is unspecified by the buisness requirments, the function will return a dictionary. 
    The return dictionary is keyed by companies whose feeds have lapsed for the given amount of days, and valued by the respective URLs of those feeds.

    Parameters:
    rss_dict (dict of str: str): A dictionary keyed from the string of a company's name and valued to some amount of RSS feed URL strings.

    miniumum_days_inactive (int): The number of days a feed must be inactive for to be returned by the function. 

    '''

    inactive_companies = {}

    return inactive_companies
