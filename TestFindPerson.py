import unittest
from crowdmap import Crowdmap

class FindPersonTests(unittest.TestCase):
    def setUp(self):
        self.crowdmap = Crowdmap()

    def test_getAllPostsForName(self):
       posts = self.crowdmap.get_all_postsfor("Or")
       self.assertIn("Or", posts)


