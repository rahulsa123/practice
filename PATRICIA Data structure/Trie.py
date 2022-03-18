class Trie:
    """
    Create trie node with data, l_child, r_child
    >>> node = Trie("a",None,None)
    """

    root = None

    def __init__(self, data) -> None:
        self.data = data
        self.childs = dict()
        self.is_finished = False

    @classmethod
    def addWord(cls, word: str) -> None:
        """
        addWord("Apple")
        it will add word in trie data structure
        """
        word = word.lower()  # solving duplicate copy issue
        if Trie.root is None:
            Trie.root = Trie("")
        ref = Trie.root
        for latter in word:
            if latter not in ref.childs:
                ref.childs[latter] = Trie(latter)
            ref = ref.childs[latter]
        ref.is_finished = True

    @classmethod
    def search(cls, word: str) -> bool:
        """
        >>>search("Apple")
            True (if Apple or apple )
            False (if word not present)
        """
        word = word.lower()
        if Trie.root is None:
            return False
        temp = Trie.root
        for latter in word:
            if latter not in temp.childs:
                return False
            temp = temp.childs[latter]
        return temp.is_finished

    @classmethod
    def reset(cls):
        Trie.root = None


if __name__ == "__main__":
    Trie.addWord("Applee")
    Trie.addWord("Apple")
    print(Trie.search("apple"))
