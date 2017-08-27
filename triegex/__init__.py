__all__ = ('Triegex',)


class TriegexNode:

    def __init__(self, char: str, childrens=()):
        self.char = char
        self.childrens = {children.char: children for children in childrens}

    def render(self):
        if not self.childrens:
            return self.char
        return self.char + r'(?:{0})'.format(
            r'|'.join(
                [children.render() for key, children in sorted(self.childrens.items())]
            )
        )


class Triegex:

    def __init__(self, *words):
        self._root = TriegexNode('')
        for word in words:
            self.add(word)

    def add(self, word: str):
        current = self._root
        for letter in word[:-1]:
            current = current.childrens.setdefault(letter, TriegexNode(letter))
        current.childrens[word[-1]] = TriegexNode(word[-1] + r'\b')

    def render(self):
        return self._root.render()

    def __iter__(self):
        return self





if __name__ == '__main__':
    triegex = Triegex('spam', 'eggs')
    triegex.add('foo')
    triegex.add('bar')
    triegex.add('baz')
    print(triegex.render())
    import re
    print(re.findall(triegex.render(), 'baz spam eggsggg eggs'))