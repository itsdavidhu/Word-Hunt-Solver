import pygame
from settings import *
from mainSolver import *


class Visualizer:
    def __init__(self, words: dict[str, int]) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.running = True
        self.font_name = pygame.font.match_font(font_name)
        self.word_bank = words
        self.text = ""
        self.all_words = None
        self.solver = None
        self.all_word_comb = {}

    def show_start_screen(self) -> None:
        self.screen.fill(black)
        self.draw_text(title, 48, white, width / 2, height / 4)
        self.draw_text("Enter 16 letters for a 4x4 board", 22, white, width / 2, height / 2)
        self.input()

    def input(self) -> None:
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    elif event.key == pygame.K_RETURN:
                        if len(self.text) < 16:
                            self.draw_text("Not enough letters", 22, white, width / 2, height * 4/5)
                        else:
                            waiting = False
                    else:
                        self.text += event.unicode
            input_rect = pygame.Rect(185, 400, 230, 32)
            pygame.draw.rect(self.screen, white, input_rect)
            base_font = pygame.font.Font(None, 32)
            text_surface = base_font.render(self.text, True, black)
            self.screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
            pygame.display.flip()
            self.clock.tick(fps)

    def new(self) -> None:
        if self.running:
            self.solver = WordHuntSolverDict(self.text, self.word_bank)
            self.solver.all_comb()
            for i in sorted(self.solver.comb, key=len, reverse=True):
                self.all_word_comb[i] = self.solver.comb[i]
            self.all_words = list(self.all_word_comb.keys())
            word_num = 0
            while word_num < len(self.all_words) and self.running:
                self.screen.fill(black)
                self.draw_map()
                pygame.display.flip()
                self.draw_words(word_num)
                word_num += 1
                self.clock.tick(fps)

    def end(self) -> None:
        while self.running:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if width/3 <= mouse[0] <= width/3+200 and height * 2/3 <= mouse[1] <= height * 2/3 + 60:
                        self.running = False
                    if width/3 <= mouse[0] <= width/3+200 and height / 3 <= mouse[1] <= height / 3 + 60:
                        self.text = ""
                        self.all_words = None
                        self.solver = None
                        self.all_word_comb = {}
                        self.run()
            self.screen.fill(black)
            if width/3 <= mouse[0] <= width/3+200 and height / 3 <= mouse[1] <= height / 3 + 60:
                pygame.draw.rect(self.screen, green, [width/3, height / 3, 200, 60])
            else:
                pygame.draw.rect(self.screen, color_dark, [width/3, height / 3, 200, 60])
            if width/3 <= mouse[0] <= width/3+200 and height * 2/3 <= mouse[1] <= height * 2/3 + 60:
                pygame.draw.rect(self.screen, green, [width/3, height * 2/3, 200, 60])
            else:
                pygame.draw.rect(self.screen, color_dark, [width/3, height * 2/3, 200, 60])
            self.draw_text("Restart", 48, white, width / 2, height / 3)
            self.draw_text("Quit", 48, white, width / 2, height * 2/3)
            pygame.display.flip()

    def run(self) -> None:
        self.show_start_screen()
        self.new()
        self.end()

    def draw_map(self) -> None:
        self.draw_text(self.text[0], 48, white, 125, 75)
        self.draw_text(self.text[1], 48, white, 250, 75)
        self.draw_text(self.text[2], 48, white, 375, 75)
        self.draw_text(self.text[3], 48, white, 500, 75)
        self.draw_text(self.text[4], 48, white, 125, 200)
        self.draw_text(self.text[5], 48, white, 250, 200)
        self.draw_text(self.text[6], 48, white, 375, 200)
        self.draw_text(self.text[7], 48, white, 500, 200)
        self.draw_text(self.text[8], 48, white, 125, 325)
        self.draw_text(self.text[9], 48, white, 250, 325)
        self.draw_text(self.text[10], 48, white, 375, 325)
        self.draw_text(self.text[11], 48, white, 500, 325)
        self.draw_text(self.text[12], 48, white, 125, 450)
        self.draw_text(self.text[13], 48, white, 250, 450)
        self.draw_text(self.text[14], 48, white, 375, 450)
        self.draw_text(self.text[15], 48, white, 500, 450)

    def draw_words(self, word_num: int) -> None:
        curr_word = self.all_words[word_num]
        for i in range(len(self.all_word_comb[curr_word][1])):
            location = self.all_word_comb[curr_word][0][i]
            num_x, num_y = 125 * location[0], 125 * location[1]
            if self.all_word_comb[curr_word][1][i] == 'right':
                arrow = ((150 + num_x, 100 + num_y), (150 + num_x, 110 + num_y), (190 + num_x, 110 + num_y), (190 + num_x, 120 + num_y), (225 + num_x, 105 + num_y), (190 + num_x, 90 + num_y), (190 + num_x, 100 + num_y))
                pygame.draw.polygon(self.screen, white, arrow)
            elif self.all_word_comb[curr_word][1][i] == 'left':
                arrow = ((100 + num_x, 100 + num_y), (100 + num_x, 110 + num_y), (60 + num_x, 110 + num_y), (60 + num_x, 120 + num_y), (25 + num_x, 105 + num_y), (60 + num_x, 90 + num_y), (60 + num_x, 100 + num_y))
                pygame.draw.polygon(self.screen, white, arrow)
            elif self.all_word_comb[curr_word][1][i] == 'up':
                arrow = ((120 + num_x, 80 + num_y), (130 + num_x, 80 + num_y), (130 + num_x, 50 + num_y), (140 + num_x, 50 + num_y), (125 + num_x, 25 + num_y), (110 + num_x, 50 + num_y), (120 + num_x, 50 + num_y))
                pygame.draw.polygon(self.screen, white, arrow)
            elif self.all_word_comb[curr_word][1][i] == 'down':
                arrow = ((120 + num_x, 145 + num_y), (130 + num_x, 145 + num_y), (130 + num_x, 175 + num_y), (140 + num_x, 175 + num_y), (125 + num_x, 200 + num_y), (110 + num_x, 175 + num_y), (120 + num_x, 175 + num_y))
                pygame.draw.polygon(self.screen, white, arrow)
            elif self.all_word_comb[curr_word][1][i] == 'left_up':
                arrow = ((95 + num_x, 85 + num_y), (105 + num_x, 75 + num_y), (40 + num_x, 10 + num_y), (50 + num_x, num_y), (20 + num_x, num_y), (20 + num_x, 30 + num_y), (30 + num_x, 20 + num_y))
                pygame.draw.polygon(self.screen, white, arrow)
            elif self.all_word_comb[curr_word][1][i] == 'left_down':
                arrow = ((105 + num_x, 135 + num_y), (95 + num_x, 125 + num_y), (30 + num_x, 190 + num_y), (20 + num_x, 180 + num_y), (20 + num_x, 210 + num_y), (50 + num_x, 210 + num_y), (40 + num_x, 200 + num_y))
                pygame.draw.polygon(self.screen, white, arrow)
            elif self.all_word_comb[curr_word][1][i] == 'right_up':
                arrow = ((145 + num_x, 75 + num_y), (155 + num_x, 85 + num_y), (220 + num_x, 20 + num_y), (230 + num_x, 30 + num_y), (230 + num_x, num_y), (200 + num_x, num_y), (210 + num_x, 10 + num_y))
                pygame.draw.polygon(self.screen, white, arrow)
            elif self.all_word_comb[curr_word][1][i] == 'right_down':
                arrow = ((155 + num_x, 125 + num_y), (145 + num_x, 135 + num_y), (210 + num_x, 200 + num_y), (200 + num_x, 210 + num_y), (230 + num_x, 210 + num_y), (230 + num_x, 180 + num_y), (220 + num_x, 190 + num_y))
                pygame.draw.polygon(self.screen, white, arrow)
            self.draw_text('The word is: %s' % curr_word, 48, white, 250, 525)
        pygame.display.flip()
        self.events()

    def events(self) -> None:
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        waiting = False
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running = False

    def draw_text(self, text, size, color, x, y) -> None:
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)


g = Visualizer(all_words)
g.run()
