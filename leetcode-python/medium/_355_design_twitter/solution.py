from typing import List, Dict, Set
from collections import defaultdict


class Twitter:
    # list of tweet (count, tweet_id)
    tweets_map: Dict[int, List]
    followees_map: Dict[int, Set]
    count: int

    def __init__(self):
        self.tweets_map = defaultdict(list)
        self.followees_map = defaultdict(set)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets_map:
            self.tweets_map[userId] = []

        tweet = (self.count, tweetId)  # (cnt, tweetId)
        self.tweets_map[userId].append(tweet)
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """Merge K sorted list"""
        res = []
        followee_ids = list(self.followees_map[userId])
        # current user follow themselves
        followee_ids.append(userId)
        print(f"List of followee of {userId=}: {followee_ids=}")
        user_to_mrt_index = {user_id: len(self.tweets_map[user_id]) - 1 for user_id in followee_ids}
        print(f"{user_to_mrt_index=}")

        while len(res) < 10 and any(mrt_index >= 0 for mrt_index in user_to_mrt_index.values()):
            max_count = -1
            max_user_id = None
            # find index of max count
            for k, v in user_to_mrt_index.items():
                if v == -1:
                    continue
                tweet = self.tweets_map[k][v]
                if tweet[0] > max_count:
                    max_count = tweet[0]
                    max_user_id = k

            # MRT will be from max_user_id
            print(f"Found {max_user_id=}")
            mrt_id = user_to_mrt_index[max_user_id]
            mrt = self.tweets_map[max_user_id][mrt_id]
            print(f"User {max_user_id} has the most recent tweet")
            print(f"The tweet is {mrt}")
            res.append(mrt[1])

            user_to_mrt_index[max_user_id] = user_to_mrt_index[max_user_id] - 1
            print("=========")

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followees_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followees_map:
            if followeeId in self.followees_map[followerId]:
                self.followees_map[followerId].remove(followeeId)
