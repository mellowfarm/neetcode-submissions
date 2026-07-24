class PrefixTree:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        curr = self.root
        for letter in word:
            if letter not in curr:
                curr[letter] = {}
            curr = curr[letter]
        curr[None] = True

    def search(self, word: str) -> bool:
        curr = self.root
        idx = 0
        while idx < len(word):
            if word[idx] not in curr:
                return False
            curr = curr[word[idx]]
            idx += 1
        return curr.get(None, False)

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        idx = 0
        while idx < len(prefix):
            if prefix[idx] not in curr:
                return False
            curr = curr[prefix[idx]]
            idx += 1
        return True
        