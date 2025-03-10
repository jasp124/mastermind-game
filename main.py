import pygame, os
from settings import *
from rest import *
from random import *
from datetime import date

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()

    def new(self):
        self.board = Board()
        self.colour = None

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.draw()

    def draw(self):
        self.screen.fill(BGCOLOUR)
        self.board.draw(self.screen)
        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = event.pos
                self.colour = self.board.select_colour(mx, my, self.colour)
                if self.colour is not None:
                    self.board.place_pin(mx, my, self.colour)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.board.check_row():
                        clues_colour_list = self.board.check_clues()
                        self.board.set_clues(clues_colour_list)
                        if self.check_win(clues_colour_list):
                            
                            print("You Won!")
                            update_or_create_file("results.txt", True)
                            

                            self.board.reveal_code()
                            self.end_screen()
                        elif not self.board.next_round():
                            print("Game Over!")
                            
                            update_or_create_file("results.txt", False)
                           
                            self.board.reveal_code()
                            self.end_screen()

    def check_win(self, colour_list):
        return len(colour_list) == 4 and all(colour == RED for colour in colour_list)

    def end_screen(self):
        while True:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.playing = False
                    return

            self.draw()



def update_or_create_file(self, win):
    
    filename="results.txt"
    day = date.today()
    if os.path.exists(filename):
        with open(filename, 'a') as file:
            if win == True:
                file.write("WON "+ str(day) + '\n')
            else:
                file.write("LOSS " +str(day)+ '\n')
            print(f"Result added to the file called {filename}")
    else:
        with open(filename, 'w') as file:
            if win == True:
                file.write("WON " + str(day)+ '\n')
            else:
                file.write("LOSS " + day+str(day)+ '\n')
            print(f"New file created and result added to the file called {filename}")




game = Game()
while True:
    game.new()
    game.run()
