# https://leetcode.com/problems/implement-trie-ii-prefix-tree/

from typing import Dict


# store two counters at every node;
# at the end of word, increment endcount
# when inserting, increment count at every node, i.e. for every letter
# when erasing word, decrement counts at every letter.
class Trie:
    children: Dict[str, "Trie"]
    count: int
    endcount: int

    def __init__(self):
        self.children = {}
        self.count = 0
        self.endcount = 0

    def insert(self, word: str) -> None:
        crtTree = self
        for letter in word:
            if letter not in crtTree.children:
                crtTree.children[letter] = Trie()
            crtTree = crtTree.children[letter]
            crtTree.count += 1
        crtTree.endcount += 1

    def countWordsEqualTo(self, word: str) -> int:
        crtTree = self
        for letter in word:
            if letter not in crtTree.children:
                return 0
            crtTree = crtTree.children[letter]
        return crtTree.endcount

    def countWordsStartingWith(self, prefix: str) -> int:
        crtTree = self
        for letter in prefix:
            if letter not in crtTree.children:
                return 0
            crtTree = crtTree.children[letter]
        return crtTree.count

    def erase(self, word: str) -> None:
        crtTree = self
        for letter in word:
            if letter not in crtTree.children:
                break
            crtTree = crtTree.children[letter]
            crtTree.count -= 1
        crtTree.endcount -= 1


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    trie.insert("banana")
    print(f"Expected: 1 Actual: {trie.countWordsEqualTo('banana')}")
    trie.insert("amaranth")
    trie.insert("april")
    print(f"Expected: 2 Actual: {trie.countWordsStartingWith('ap')}")
    trie.erase("apple")
    print(f"Expected: 0 Actual: {trie.countWordsEqualTo('apple')}")
    print(f"Expected: 1 Actual: {trie.countWordsEqualTo('april')}")
    print(f"Expected: 1 Actual: {trie.countWordsStartingWith('ap')}")
