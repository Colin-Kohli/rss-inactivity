import unittest
import rss_inactivity as rss


class TestRSS(unittest.TestCase):

    def test_ReturnDictIsBlank_False(self):
        self.assertNotEqual(rss.get_rss_inactivity({'a': ['1']}, 1), {})

    # def test_BadInput_AssertionErrorThrown(self):
    #     self.assertRaises(
    #         AssertionError, rss.get_rss_inactivity({'a': ["6"]}, 1))
    #     self.assertRaises(AssertionError, rss.get_rss_inactivity({[]: 5}, 1))


    # TODO
    # Test if urls and companies are paired correctly
    # Test multiple feeds per company, some lapsed some not
    # assert url regex
if __name__ == '__main__':
    unittest.main()
