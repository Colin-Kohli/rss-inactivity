# rss-inactivity
RSS-inactivity is a tool for identifying RSS feeds from a dictionary with inactivity greater than a given number of days.

The function get_rss_inactivity(rss_dict, minimum_days_inactive, today=datetime.datetime.today()) accepts a dictionary mapping company names to RSS feeds, and returns those companys which have not updated their feeds in minimuin_days_inactive days. 

The inactive companies are returned in a dictionary of their own, keyed to a list their respective inactive URLs. A single company may have multiple URLs as values, and multiple companies may have the same URLs as a value. A single company may not have the same URL as a value multiple times. 

test_rss_inacivity.py contains various unit tests for rss_inactivity.py.

My next steps would be to refactor the RSS calls to be asychronous, as a slow XML retreival could bottleneck this single-threaded program. I will also need to add a timeout for the RSS calls, as the parser I used does not have a native timeout functionaity. 
