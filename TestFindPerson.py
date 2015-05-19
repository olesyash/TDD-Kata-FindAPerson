import unittest
from crowdmap import Crowdmap

class FindPersonTests(unittest.TestCase):
    def setUp(self):
        self.crowdmap = Crowdmap(["I met Or A. at Chabad house Bangkok", "We found Or A. R.I.P at Langtang valley"])

    def test_getAllPostsForName(self):
        name = "Or"
        flag = True
        posts = self.crowdmap.get_all_posts_for(name)
        for l in posts:
           if name not in l:
               flag = False
        self.assertTrue(flag)

    def test_get_all_posts_for_missing_name(self):
        name = "Or2"
        flag = True
        posts = self.crowdmap.get_all_posts_for(name)
        for l in posts:
            if name not in l:
               flag = False
            self.assertFalse(flag)

    def test_includes_location_information(self):
        name = "Or"
        self.assertTrue(self.crowdmap.is_location(name))

    def test_includes_location_information_for_misssing_name(self):
        name = "Or2"
        self.assertFalse(self.crowdmap.is_location(name))