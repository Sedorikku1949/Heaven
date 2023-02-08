import pygame
from constants import *
from menu import Menu, GameStatus
from game import Game

class GameEngine:
    """Le gestionnaire du jeux"""
    def __init__(self):
        self.status = GameStatus.MENU
        self.running = True

        self.setup()

        self.menu = Menu()
        self.game = Game()

        self.run()
    
    def setup(self):
        pygame.init()
        pygame.font.init()
        
        self.display = pygame.display.set_mode((DEFAULT_WINDOW_WIDTH, DEFAULT_WINDOW_HEIGHT), pygame.RESIZABLE) # Créer la fenêtre du jeu

        pygame.display.set_caption("Heaven")
        self.frequence = pygame.time.Clock()
    
    def draw(self):
        if self.status == GameStatus.MENU:
            self.menu.draw(self.display)
        elif self.status == GameStatus.GAME:
            self.game.draw(self.display)
        else:
            self.display.fill((0, 0, 0))

    def update(self):
        if self.status == GameStatus.MENU:
            self.menu.update(self.frequence)
        elif self.status == GameStatus.GAME:
            self.game.update(self.frequence)

    def exit(self):
        self.running = False

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()
            
            elif event.type == pygame.KEYDOWN: # Si la touche est appuyée
                if self.status == GameStatus.MENU:
                    self.menu.key_down(event, self)
            
            elif event.type == pygame.KEYUP: # Si la touche est relachée
                if self.status == GameStatus.MENU:
                    self.menu.key_up(event, self)
            
            elif event.type == pygame.MOUSEBUTTONDOWN: # Si le  bouton de la souris est appuyé
                if self.status == GameStatus.MENU:
                    self.menu.mouse_btn_down(event, self)
            
            elif event.type == pygame.MOUSEBUTTONUP: # Si le bouton de la souris est relachée 
                if self.status == GameStatus.MENU:
                    self.menu.mouse_btn_up(event, self)

            elif event.type == pygame.MOUSEMOTION: # Si la souris bouge
                if self.status == GameStatus.MENU:
                    self.menu.mouse_move(event, self)

    def run(self):
        while self.running:
            self.events()
            self.update()
            self.draw()
            pygame.display.update()

            self.frequence.tick(TICKS_PER_SECONDS)
        
        
        print("Good bye!")

engine = GameEngine()