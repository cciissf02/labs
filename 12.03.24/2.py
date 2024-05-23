class LeftParagraph:
    def __init__(self, width):
        self.width = width
        self.words = []
    def add_word(self, word):
        if len(' '.join(self.words)) + len(word) <= self.width:
            self.words.append(word)
        else:
            self.end()
            self.words.append(word)
    def end(self):
        print(' '.join(self.words))
        self.words = []

class RightParagraph:
    def __init__ (self, width):
        self.width = width
        self.words = []
    def add_word(self, word):
        if len(' '.join(self.words + [word])) <= self.width:
            self.words.append(word)
        else:
            self.end()
            self.words.append(word)
    def end(self):
        spaces = ' ' * (self.width - len(' '.join(self.words)))
        print(spaces + ' '.join(self.words))
        self.words = []

lp = LeftParagraph(8)
lp.add_word('abc')
lp.add_word('defg')
lp.add_word('hi')
lp.add_word('jklmnopq')
lp.add_word('r')
lp.add_word('stuv')
lp.end()
print()
rp = RightParagraph(8)
rp.add_word('abc')
rp.add_word('defg')
rp.add_word('hi')
rp.add_word('jklmnopq')
rp.add_word('r')
rp.add_word('stuv')
rp.end()
print()