import unittest
import datetime
import rss_inactivity as rss


link_dict = {
    'Unraveled': ['https://rss.acast.com/unraveled'],
    'Bible': ['https://feeds.fireside.fm/bibleinayear/rss'],
    'Dateline': ['https://podcastfeeds.nbcnews.com/dateline-nbc']
}


class TestRSS(unittest.TestCase):

    # Test sanity check of bad parameter values and types
    def test_BadInput_AssertionErrorThrown(self):
        with self.assertRaises(AssertionError):
            # bad type arg1 key
            rss.get_rss_inactivity({4: ["6"]}, 1)
            # bad type arg1 value (no list)
            rss.get_rss_inactivity({'a': "6"}, 1)
            # bad type arg1 value(within list)
            rss.get_rss_inactivity({'a': [9]}, 1)
            # bad type arg1 value(empty list)
            rss.get_rss_inactivity({'a': [9]}, 1)
            # bad value arg2
            rss.get_rss_inactivity({'a': ["6"]}, -1)
            # bad type arg2
            rss.get_rss_inactivity({'a': ["6"]}, "hello")

    def test_ActiveFeed_TitleInReturnDict(self):
        self.assertIn("Unraveled", rss.get_rss_inactivity(link_dict, 0))

    def test_InactiveFeed_TitleNotInReturnDict(self):
        self.assertNotIn(
            "Unraveled", rss.get_rss_inactivity(link_dict, 1000000))

    def test_ReturnDictIsBlank_False(self):
        self.assertNotEqual(rss.get_rss_inactivity(link_dict, 0), {})

    def test_ThreeDifferentLinksOneCompany(self):

        _link_dict = {
            'Unraveled': ['https://rss.acast.com/unraveled', 'https://feeds.fireside.fm/bibleinayear/rss', 'https://podcastfeeds.nbcnews.com/dateline-nbc'],
            'Dateline': ['https://podcastfeeds.nbcnews.com/dateline-nbc']
        }

        today = datetime.datetime.strptime(
            "08Feb202117:57:34", "%d%b%Y%H:%M:%S")  # manually set date so this test doesn't fail tomorrow :)

        result = rss.get_rss_inactivity(_link_dict, 0, today=today)
        self.assertEqual(len(result["Unraveled"]), 3)

    def test_OneLinkTwoCompanies(self):

        _link_dict = {
            'Unraveled': ['https://podcastfeeds.nbcnews.com/dateline-nbc'],
            'Dateline': ['https://podcastfeeds.nbcnews.com/dateline-nbc']
        }
        today = datetime.datetime.strptime(
            "08Feb202117:57:34", "%d%b%Y%H:%M:%S")  # manually set date so this test doesn't fail tomorrow :)

        result = rss.get_rss_inactivity(_link_dict, 0, today=today)
        self.assertEqual(result["Unraveled"], result["Dateline"])


if __name__ == '__main__':
    unittest.main(buffer=True)
