__author__ = 'olesya'

class Crowdmap():
    def __init__(self, l_post):
        self.posts_list = l_post

    def get_all_posts_for(self, name):
        list_of_posts = list()
        for l in self.posts_list:
            if name in l:
                list_of_posts.append(l)
        return list_of_posts


    def is_location(self, name):
        return True
