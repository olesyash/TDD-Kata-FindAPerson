__author__ = 'olesya'

class Crowdmap():
    def __init__(self, l_post):
        self.posts_list = l_post

    def get_all_posts_for(self, name):
        for l in self.posts_list:
            if name in l:
                return True
        return False