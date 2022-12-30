import time


class WordHuntSolverDict:

    def __init__(self, board_letters: str, words: dict[str, int]) -> None:
        self.matrix = []
        self.comb = {}
        self.words = words
        for i in range(0, 13, 4):
            self.matrix.append([j for j in board_letters[i:i + 4]])

    def all_comb(self) -> None:
        for i in range(4):
            for j in range(4):
                self.all_comb_helper(j, i, "", [], [])

    def all_comb_helper(self, x: int, y: int, curr: str, visited: list[tuple[int, int]], directions: list[str]) -> None:
        if 0 <= x <= 3 and 0 <= y <= 3 and (x, y) not in visited:
            curr += self.matrix[y][x]
            if curr in self.words:
                new_visited = visited + [(x, y)]
                if self.words[curr] == 1 and curr not in self.comb and len(curr) >= 3:
                    self.comb[curr] = [new_visited, directions]
                self.all_comb_helper(x, y - 1, curr,
                                     new_visited, directions + ['up'])
                self.all_comb_helper(x, y + 1, curr,
                                     new_visited, directions + ['down'])
                self.all_comb_helper(x - 1, y, curr,
                                     new_visited, directions + ['left'])
                self.all_comb_helper(x + 1, y, curr,
                                     new_visited, directions + ['right'])
                self.all_comb_helper(x - 1, y - 1, curr,
                                     new_visited, directions + ['left_up'])
                self.all_comb_helper(x - 1, y + 1, curr,
                                     new_visited, directions + ['left_down'])
                self.all_comb_helper(x + 1, y + 1, curr,
                                     new_visited, directions + ['right_down'])
                self.all_comb_helper(x + 1, y - 1, curr,
                                     new_visited, directions + ['right_up'])


with open('words.txt', 'r') as file:
    all_words = {}
    for line in file:
        current = ''
        for letter in line:
            if letter == '\n':
                all_words[current] = 1
            else:
                current += letter
                if current not in all_words:
                    all_words[current] = 0

# letters = "cfmukwneskwoanse"
# s = WordHuntSolverDict(letters, all_words)
# print(s.matrix)
# start = time.time()
# s.all_comb()
# for word in sorted(s.comb.items(), key=lambda x: len(x[0])):
#     print(word)
# end = time.time()
# print(end - start)
