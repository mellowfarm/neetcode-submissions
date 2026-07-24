class PrefixTree:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        word = list(word)
        curr = self.root
        for letter in word:
            if letter not in curr:
                curr[letter] = {}
            curr = curr[letter]
        curr["end"] = True

    def search(self, word: str) -> bool:
        word = list(word)
        curr = self.root
        idx = 0
        while idx < len(word):
            if word[idx] not in curr:
                return False
            curr = curr[word[idx]]
            idx += 1
        if curr.get("end", False):
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        prefix = list(prefix)
        curr = self.root
        idx = 0
        while idx < len(prefix):
            if prefix[idx] not in curr:
                return False
            curr = curr[prefix[idx]]
            idx += 1
        return True
        