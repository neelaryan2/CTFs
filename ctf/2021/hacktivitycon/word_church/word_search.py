class WordSearch:
    def __init__(self, grid):
        self.grid = grid
        self.R = len(grid)
        self.C = len(grid[0])
        self.dir = [[-1, 0], [1, 0], [1, 1], [1, -1], [-1, -1], [-1, 1], [0, 1], [0, -1]]

    def mod(self, c, x, m):
        c += x
        if c >= m:
            return c - m
        if c < -m:
            return c + m
        return c

    def search2D(self, row, col, word):
        if self.grid[row][col] != word[0]:
            return None

        for x, y in self.dir:
            path = [(row, col)]
            rd = self.mod(row, x, self.R)
            cd = self.mod(col, y, self.C)
            found = True

            for k in range(1, len(word)):
                if (word[k] == self.grid[rd][cd]):
                    path.append((rd, cd))
                    rd = self.mod(rd, x, self.R)
                    cd = self.mod(cd, y, self.C)
                else:
                    found = False
                    break

            if found:
                return path
        return None

    def patternSearch(self, word):
        for row in range(self.R):
            for col in range(self.C):
                f = self.search2D(row, col, word)
                if f is not None:
                    return f
        return []


def transpose_grid(grid):
    r = len(grid)
    c = len(grid[0])
    g = ['' for i in range(c)]
    for row in grid:
        assert len(row) == c
        for i, ch in enumerate(row):
            g[i] += ch
    return g


if __name__ == '__main__':
    grid = """
    YIDPMBLGBZPIRGVW
    IXJHNNNKYXLHNGTI
    PWYOZSPAUKNYEYTR
    GOQTLVUNUWRUURXI
    AOQLJPPGSXKWWADB
    GNBUZEGDCDEDITWM
    FHOQNFBHLFNHXIKA
    INBHLDXOFFSOGOXE
    VEBYOVENBYSJMNNN
    MQIPLFSRXQWJZSDD
    IWEKYVRDWLSFZBYT
    AYSBWGEIDEYNOWCG
    ALCIJEXLMZAEGJGF
    MNJKCJNLAMORDSHO
    UWJVSNXLXSVVSZDG
    PQZVSZXKUJYJDFYX
     """
    grid = transpose_grid(grid.split())
    word = 'FENS'

    G = WordSearch(grid)
    print(G.patternSearch(word))
