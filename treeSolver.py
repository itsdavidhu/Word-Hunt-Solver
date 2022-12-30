import time


class Tree:

    def __init__(self, root):
        self.root = root
        self.subtrees = []
        self.word_finished = False


def create_word_tree(tree, lst):
    for word in lst:
        curr = tree
        for letter in word:
            in_child = False
            for subtree in curr.subtrees:
                if subtree.root == letter:
                    curr = subtree
                    in_child = True
                    break
            if not in_child:
                new_node = Tree(letter)
                curr.subtrees.append(new_node)
                curr = new_node
        curr.word_finished = True


def in_tree(tree, word):
    curr = tree
    for letter in word:
        in_child = False
        for subtree in curr.subtrees:
            if subtree.root == letter:
                curr = subtree
                in_child = True
                break
        if not in_child:
            return False
    return True


class WordHuntSolver:

    def __init__(self, board_letters: str, words: Tree):
        self.matrix = []
        self.comb = {}
        self.words = words
        for i in range(0, 13, 4):
            self.matrix.append([j for j in board_letters[i:i + 4]])

    def all_comb(self) -> None:
        for i in range(4):
            for j in range(4):
                self.all_comb_helper(j, i, self.matrix[i][j], [(j, i)],
                                     self.words)

    def all_comb_helper(self, x, y, curr, visited, tree) -> None:
        if 0 <= x <= 3 and 0 <= y <= 3 and in_tree(self.words, curr):
            curr_tree = tree
            for subtree in curr_tree.subtrees:
                if subtree.root == curr[-1]:
                    curr_tree = subtree
                    break
            if curr_tree.word_finished and curr not in self.comb:
                self.comb[curr] = visited
            if 0 <= x <= 3 and 0 <= y - 1 <= 3 and (x, y - 1) not in visited:
                self.all_comb_helper(x, y - 1, curr + self.matrix[y - 1][x],
                                     visited + [(x, y - 1)], curr_tree)
            if 0 <= x <= 3 and 0 <= y + 1 <= 3 and (x, y + 1) not in visited:
                self.all_comb_helper(x, y + 1, curr + self.matrix[y + 1][x],
                                     visited + [(x, y + 1)], curr_tree)
            if 0 <= x - 1 <= 3 and 0 <= y <= 3 and (x - 1, y) not in visited:
                self.all_comb_helper(x - 1, y, curr + self.matrix[y][x - 1],
                                     visited + [(x - 1, y)], curr_tree)
            if 0 <= x + 1 <= 3 and 0 <= y <= 3 and (x + 1, y) not in visited:
                self.all_comb_helper(x + 1, y, curr + self.matrix[y][x + 1],
                                     visited + [(x + 1, y)], curr_tree)
            if 0 <= x - 1 <= 3 and 0 <= y - 1 <= 3 and \
                    (x - 1, y - 1) not in visited:
                self.all_comb_helper(x - 1, y - 1, curr +
                                     self.matrix[y - 1][x - 1],
                                     visited + [(x - 1, y - 1)], curr_tree)
            if 0 <= x - 1 <= 3 and 0 <= y + 1 <= 3 and \
                    (x - 1, y + 1) not in visited:
                self.all_comb_helper(x - 1, y + 1, curr +
                                     self.matrix[y + 1][x - 1],
                                     visited + [(x - 1, y + 1)], curr_tree)
            if 0 <= x + 1 <= 3 and 0 <= y + 1 <= 3 and \
                    (x + 1, y + 1) not in visited:
                self.all_comb_helper(x + 1, y + 1, curr +
                                     self.matrix[y + 1][x + 1],
                                     visited + [(x + 1, y + 1)], curr_tree)
            if 0 <= x + 1 <= 3 and 0 <= y - 1 <= 3 and \
                    (x + 1, y - 1) not in visited:
                self.all_comb_helper(x + 1, y - 1, curr +
                                     self.matrix[y - 1][x + 1],
                                     visited + [(x + 1, y - 1)], curr_tree)


with open('words.txt', 'r') as file:
    all_words = []
    for line in file:
        all_words.append(line.strip())


t = Tree(None)
create_word_tree(t, all_words)
letters = "cfmukwneskwoanse"
s = WordHuntSolver(letters, t)
start = time.time()
s.all_comb()
for w in sorted(s.comb.items(), key=lambda x: len(x[0])):
    print(w)
end = time.time()
print(end - start)
