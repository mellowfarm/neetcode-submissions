class Twitter:

    def __init__(self):
        self.users = {}
        self.following = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users[userId] = []
            self.following[userId] = set([userId])
        self.users[userId].append((-1*self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        res = []
        following_list = self.following.get(userId, set())
        for account in following_list:
            posts = self.users.get(account, [])
            if not posts:
                continue
            i = len(posts) - 1
            time, tweet = posts[i]
            heapq.heappush(feed, (time, tweet, account, i-1))
        while feed and len(res) < 10:
            next_post = heapq.heappop(feed)
            ntime, ntweet, naccount, nidx = next_post
            res.append(ntweet)
            if nidx >= 0:
                ntime, ntweet = self.users[naccount][nidx]
                heapq.heappush(feed, (ntime, ntweet, naccount, nidx-1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            if followerId not in self.following:
                self.following[followerId] = set([])
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            self.following.get(followerId, set()).discard(followeeId)
                
