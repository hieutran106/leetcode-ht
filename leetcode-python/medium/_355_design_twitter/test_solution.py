import unittest
from .solution import Twitter

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_case_1(self):
        twitter = Twitter()
        # user 1 posts a new tweet
        twitter.postTweet(1, 5)
        # User 1's news feed should return a list with 1 tweet id -> [5]. return [5
        tweets = twitter.getNewsFeed(1)
        self.assertEqual([5], tweets)

        twitter.follow(1, 2)
        twitter.postTweet(2, 6)
        tweets = twitter.getNewsFeed(1)
        self.assertEqual([6, 5], tweets)

        twitter.unfollow(1, 2);
        tweets = twitter.getNewsFeed(1)
        self.assertEqual([5], tweets)

    def test_case_2(self):
        twitter = Twitter()
        # user 1 posts a new tweet
        twitter.postTweet(1, 5)
        twitter.postTweet(1, 6)

        # user 2 posts a new tweet
        twitter.postTweet(2, 7)

        # user 3 posts a new tweet
        twitter.postTweet(3, 8)
        twitter.postTweet(3, 9)

        twitter.follow(1, 3)

        tweets = twitter.getNewsFeed(1)
        self.assertEqual([9, 8, 6, 5], tweets)

        twitter.unfollow(1, 3)
        tweets = twitter.getNewsFeed(1)
        self.assertEqual([6, 5], tweets)



if __name__ == '__main__':
    unittest.main()

