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
        following_list = self.following[userId]
        for account in following_list:
            posts = self.users[account]
            for post in posts:
                heapq.heappush(feed, post)
        for _ in range(10):
            if not feed:
                break
            next_post = heapq.heappop(feed)
            res.append(next_post[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            if followerId not in self.following:
                self.following[followerId] = set([])
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            following_list = self.following[followerId]
            new_list = following_list - set([followeeId])
            self.following[followerId] = new_list
                
