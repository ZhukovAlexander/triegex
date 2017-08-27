import collections

__all__ = ('Triegex',)

OR = r'|'
NOTHING = r'z^'  # well, it matches nothing https://stackoverflow.com/a/940840/2183102
GROUP = r'(?:{0})'
WORD_BOUNDARY = r'\b'


class TriegexNode:

    def __init__(self, char: str, end: bool, *childrens):
        self.char = char if char is not None else ''
        self.end = end
        self.childrens = {children.char: children for children in childrens}

    def __iter__(self):
        return iter(self.childrens.values())

    def __contains__(self, key):
        return key in self.childrens

    def __getitem__(self, key):
        return self.childrens[key]

    def render(self):
        char = self.char
        if not self.childrens:
            return char
        if self.end:
            char = self.char + WORD_BOUNDARY
        return char + GROUP.format(
            OR.join(
                [children.render() for key, children in sorted(self.childrens.items())]
            )
        )


class Triegex(collections.MutableSet):

    _root = None

    def __init__(self, *words):
        """"""

        # make sure we match nothing when no words are added
        self._root = TriegexNode(None, False, TriegexNode(NOTHING, False))

        for word in words:
            self.add(word)

    def add(self, word: str):
        current = self._root
        for letter in word[:-1]:
            current = current.childrens.setdefault(letter, TriegexNode(letter, False))
        # this will ensure that we correctly match the word boundary
        current.childrens[word[-1]] = TriegexNode(word[-1], True)

    def render(self):
        return self._root.render()

    def _traverse(self):
        stack = [self._root]
        current = self._root
        while stack:
            yield current
            current = stack.pop()
            stack.extend(current.childrens.values())

    def __iter__(self):
        paths = {self._root.char: []}
        for node in self._traverse():
            for children in node:
                paths[children.char] = [node.char] + paths[node.char]
                if children.end:
                    yield ''.join(reversed([children.char] + paths[children.char]))

    def __len__(self):
        return sum(1 for _ in self.__iter__())

    def __contains__(self, word):
        current = self._root
        for char in item:
            if char not in current:
                return False
            current = current[char]
        return True

    def discard(self, word):
        return