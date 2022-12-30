import time


class WordHuntSolverNaive:

    def __init__(self, board_letters: str, words: dict[str, int]) -> None:
        self.matrix = []
        self.comb = {}
        self.words = words
        for i in range(0, 13, 4):
            self.matrix.append([j for j in board_letters[i:i + 4]])

    def all_comb(self) -> None:
        for i in range(4):
            for j in range(4):
                self.all_comb_helper(j, i, "", [])

    def all_comb_helper(self, x: int, y: int, curr: str, visited: list[tuple[int, int]]) -> None:
        if 0 <= x <= 3 and 0 <= y <= 3 and (x, y) not in visited:
            curr += self.matrix[y][x]
            new_visited = visited + [(x, y)]
            if curr in self.words and curr not in self.comb and len(curr) >= 3:
                self.comb[curr] = visited
            self.all_comb_helper(x, y - 1, curr, new_visited)
            self.all_comb_helper(x, y + 1, curr, new_visited)
            self.all_comb_helper(x - 1, y, curr, new_visited)
            self.all_comb_helper(x + 1, y, curr, new_visited)
            self.all_comb_helper(x - 1, y - 1, curr, new_visited)
            self.all_comb_helper(x - 1, y + 1, curr, new_visited)
            self.all_comb_helper(x + 1, y + 1, curr, new_visited)
            self.all_comb_helper(x + 1, y - 1, curr, new_visited)


with open('words.txt', 'r') as file:
    all_words = {}
    for line in file:
        all_words[line.strip()] = 1

letters = "cfmukwneskwoanse"
s = WordHuntSolverNaive(letters, all_words)
start = time.time()
s.all_comb()
for word in sorted(s.comb.items(), key=lambda x: len(x[0])):
    print(word)
end = time.time()
print(end - start)
