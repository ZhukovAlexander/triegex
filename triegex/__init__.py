__all__ = ('Triegex',)

OR = r'|'
NOTHING = r'z^'  # well, it matches nothing https://stackoverflow.com/a/940840/2183102
GROUP = r'(?:{0})'
WORD_BOUNDARY = '\b'


class TriegexNode:

    def __init__(self, char: str, *childrens):
        self.char = char if char is not None else ''
        self.childrens = {children.char: children for children in childrens}

    def render(self):
        if not self.childrens:
            return self.char
        return self.char + GROUP.format(
            OR.join(
                [children.render() for key, children in sorted(self.childrens.items())]
            )
        )


class Triegex:

    _root = None

    def __init__(self, *words):
        self._root = TriegexNode(None, TriegexNode(NOTHING))
        for word in words:
            self.add(word)

    def add(self, word: str):
        current = self._root
        for letter in word[:-1]:
            current = current.childrens.setdefault(letter, TriegexNode(letter))
        current.childrens[word[-1]] = TriegexNode(word[-1] + WORD_BOUNDARY)

    def render(self):
        return self._root.render()

    def __iter__(self):
        return self
