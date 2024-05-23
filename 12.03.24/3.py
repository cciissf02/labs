class SeaMap:
    def __init__(self):
        self.map = [['.' for _ in range(10)] for _ in range (10)]
        self.kill = []

    def shoot(self, row, col, result):
        if result == 'hit':
            self.map[row][col] = 'x'
        if result == 'sink':
            self.kill.append((row,col))

    def cell(self, row, col):
        if (row,col) in self.kill:
            return 'x'
        if self.map[row][col] =='x':
            return 'x'
        for r, c in self.kill:
            if (self.map[row][col] != 'x') and (abs(r-row) <=1 and abs(c-col) <= 1):
                return '*'
        return '.'

sm = SeaMap()
sm.shoot(2, 0, 'sink')
sm.shoot(6, 9, 'hit')
for row in range(10):
    for col in range(10):
        print(sm.cell(row, col), end = '')
    print()