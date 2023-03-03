from menu import GameStatus
from mod.ui import *
from mod.entities import *
from mod.map import *
from mod.camera import *
from mod.save import convert_tiled_to_map, open_file


#
#
#       GAME
#
#


class Game:
    def __init__(self, screen: pygame.Surface) -> None:
        map_json = open_file("map.json")
        self.map = convert_tiled_to_map(map_json, screen)  # Map()
        self.camera = Camera()
        self.assets = GameAssets()
        self.assets.load_images()
        self.ui_assets = UiAssets()

        # resizing window
        self.map.zone_decals = screen.get_size()
        self.map.DEFAULT_ZONE_DECALSs = screen.get_size()

        # TEST

        """

        self.map.add_layer(0)
        self.map.insert_tile(0, (0, 0), Tile("test_grass"))
        self.map.insert_tile(0, (-CASE_SIZE*1.5, 0), Tile("rock1"))
        self.map.insert_tile(0, (CASE_SIZE, 2 * CASE_SIZE), Tile("rock2"))

        self.map.add_entity(0, SpriteType.SPIRIT, Spirit(CASE_SIZE * 2, CASE_SIZE))

        """

        # Blep
        self.player = Player()

        self.player.inventory.add_item(Wood())

        print(self.player.inventory)

        self.ui = UI()

        # Menu affiché quand on appuie sur [ECHAP]
        self.is_escaped = True
        self.ESC_FONT = pygame.font.Font("./RetroGaming.ttf", 40)
        self.PAUSE_ESC_FONT = pygame.font.Font("./RetroGaming.ttf", 25)
        self.esc_menu_ctg = 0
        self.space_between = 75
        self.key_cooldown = 0

    def draw_esc_menu(self, screen: pygame.Surface, fps: int) -> None:
        if not self.is_escaped: return;

        # On rajoute un fond légèrement noir
        back_surface = pygame.Surface(screen.get_size())
        back_surface.set_alpha(191) # 75% opaque

        back_surface.fill((0,0,0))

        screen.blit(back_surface, (0,0))

        # On dessine les catégories
        # Catégories:
        # - Retour en jeu
        # - Options
        # - Contrôles
        # - Quitter la partie
        # - Quitter le jeux

        (screen_width, screen_height) = screen.get_size()

        # [PAUSE]
        pause_top_text = self.PAUSE_ESC_FONT.render("[PAUSE]", True, (240, 240, 240))
        screen.blit(pause_top_text, (floor((screen_width // 2) - (pause_top_text.get_width() // 2)), floor(self.space_between)))

        
        # Retour en jeu
        if self.esc_menu_ctg == 0:
            retrun_in_game = self.ESC_FONT.render("Retour en jeu", True, (240, 0, 0))
            screen.blit(retrun_in_game, (floor(screen_width // 2) - (retrun_in_game.get_width() // 2), floor(screen_height // 2) - self.space_between * 2.5))
        else:
            retrun_in_game = self.ESC_FONT.render("Retour en jeu", True, (255, 255, 255))
            screen.blit(retrun_in_game, (floor(screen_width // 2) - (retrun_in_game.get_width() // 2), floor(screen_height // 2) - self.space_between * 2.5))

        # Options
        if self.esc_menu_ctg == 1:
            opt_ctg = self.ESC_FONT.render("Options", True, (240, 0, 0))
            screen.blit(opt_ctg, (floor(screen_width // 2) - (opt_ctg.get_width() // 2), floor(screen_height // 2) - self.space_between * 1.5))
        else:
            opt_ctg = self.ESC_FONT.render("Options", True, (255, 255, 255))
            screen.blit(opt_ctg, (floor(screen_width // 2) - (opt_ctg.get_width() // 2), floor(screen_height // 2) - self.space_between * 1.5))

        
        # Contrôles
        if self.esc_menu_ctg == 2:
            cntrl_ctg = self.ESC_FONT.render("Contrôles", True, (240, 0, 0))
            screen.blit(cntrl_ctg, (floor(screen_width // 2) - (cntrl_ctg.get_width() // 2), floor(screen_height // 2) - self.space_between * 0.5))
        else:
            cntrl_ctg = self.ESC_FONT.render("Contrôles", True, (255, 255, 255))
            screen.blit(cntrl_ctg, (floor(screen_width // 2) - (cntrl_ctg.get_width() // 2), floor(screen_height // 2) - self.space_between * 0.5))
        

        # Quitter la partie
        if self.esc_menu_ctg == 3:
            opt_ctg = self.ESC_FONT.render("Quitter la partie", True, (240, 0, 0))
            screen.blit(opt_ctg, (floor(screen_width // 2) - (opt_ctg.get_width() // 2), floor(screen_height // 2) + self.space_between * 0.5))
        else:
            opt_ctg = self.ESC_FONT.render("Quitter la partie", True, (255, 255, 255))
            screen.blit(opt_ctg, (floor(screen_width // 2) - (opt_ctg.get_width() // 2), floor(screen_height // 2) + self.space_between * 0.5))
            
        # Quitter le jeux
        if self.esc_menu_ctg == 4:
            opt_ctg = self.ESC_FONT.render("Quitter le jeux", True, (240, 0, 0))
            screen.blit(opt_ctg, (floor(screen_width // 2) - (opt_ctg.get_width() // 2), floor(screen_height // 2) + self.space_between * 1.5))
        else:
            opt_ctg = self.ESC_FONT.render("Quitter le jeux", True, (255, 255, 255))
            screen.blit(opt_ctg, (floor(screen_width // 2) - (opt_ctg.get_width() // 2), floor(screen_height // 2) + self.space_between * 1.5))
       



    def draw(self, screen: pygame.Surface, fps: int) -> None:
        screen.fill((0, 0, 0))

        self.map.draw(screen, self.assets, self.camera)
        self.player.draw(screen, self.assets, self.camera, self.map)
        self.ui.draw(UiDrawArguments(self.player, self.ui_assets, screen))

        self.draw_esc_menu(screen, fps)

    def update(self, frequence: pygame.time.Clock) -> None:
        self.player.x = self.camera.x
        self.player.y = self.camera.y

        if not self.is_escaped: self.movements(frequence)

        self.player.update(frequence)
        self.ui.update(frequence, self.player, self.map)

        
        keys = pygame.key.get_pressed()
        if self.key_cooldown <= 0:
            self.key_cooldown = 4
            if keys[pygame.K_UP] or keys[pygame.K_z]:
                self.esc_menu_ctg = ((self.esc_menu_ctg - 1 ) % 5)
            elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                self.esc_menu_ctg = ((self.esc_menu_ctg + 1) % 5)
        elif self.key_cooldown > 0:
            self.key_cooldown -= 1

    def key_down(self, event: pygame.event.Event, engine) -> None:
        if event.key == pygame.K_ESCAPE:
            self.is_escaped = not self.is_escaped
        elif (event.key == pygame.K_e) and (not self.is_escaped):
            self.player.inventory_open = not self.player.inventory_open
        
        elif ((event.key == pygame.K_UP) or (event.key == pygame.K_z)) and self.is_escaped:
            self.key_cooldown = 4
            self.esc_menu_ctg = ((self.esc_menu_ctg - 1 ) % 5)
        elif ((event.key == pygame.K_DOWN) or (event.key == pygame.K_s)) and self.is_escaped:
            self.key_cooldown = 4
            self.esc_menu_ctg = ((self.esc_menu_ctg + 1) % 5)
        
        elif ((event.key == pygame.K_SPACE) or (event.key == pygame.K_RETURN)) and self.is_escaped:
            if self.esc_menu_ctg == 4:
                # Quitter le jeu
                engine.running = False
            elif self.esc_menu_ctg == 3:
                # Retour au menu
                engine.status = GameStatus.MENU
                self.esc_menu_ctg = False
                self.player.inventory_open = False
            elif self.esc_menu_ctg == 0:
                # retour en jeux
                self.is_escaped = not self.is_escaped

    def movements(self, frequence: pygame.time.Clock) -> None:
        keys = pygame.key.get_pressed()

        # On vérifie chaque touche (z, q, s, d) pour connaitre le mouvement précis
        if keys[pygame.K_z] and (
                (not (keys[pygame.K_q] or keys[pygame.K_d])) or (keys[pygame.K_q] and keys[pygame.K_d])):
            # move only up                (x,                 y)
            self.player.move(Movement.UP, (0, self.camera.speed), self.camera, frequence.get_fps())
        elif keys[pygame.K_z] and keys[pygame.K_q] and (not keys[pygame.K_d]):
            # move up left
            self.player.move(Movement.UP_LEFT, (self.camera.speed // PLAYER_DIAGONAL_COEFF, self.camera.speed // PLAYER_DIAGONAL_COEFF), self.camera, frequence.get_fps())
        elif keys[pygame.K_z] and (not keys[pygame.K_q]) and keys[pygame.K_d]:
            # move up right
            self.player.move(Movement.UP_RIGHT, (-self.camera.speed // PLAYER_DIAGONAL_COEFF, self.camera.speed // PLAYER_DIAGONAL_COEFF), self.camera, frequence.get_fps())
        elif keys[pygame.K_q] and not (keys[pygame.K_z] or keys[pygame.K_s]):
            # move only left
            self.player.move(Movement.LEFT, (self.camera.speed, 0), self.camera, frequence.get_fps())
        elif keys[pygame.K_d] and not (keys[pygame.K_z] or keys[pygame.K_s]):
            # move only right
            self.player.move(Movement.RIGHT, (-self.camera.speed, 0), self.camera, frequence.get_fps())
        elif keys[pygame.K_s] and (
                (not (keys[pygame.K_q] or keys[pygame.K_d])) or (keys[pygame.K_q] and keys[pygame.K_d])):
            # move only bottom
            self.player.move(Movement.BOTTOM, (0, -self.camera.speed), self.camera, frequence.get_fps())
        elif keys[pygame.K_s] and keys[pygame.K_q] and (not keys[pygame.K_d]):
            # move bottom left
            self.player.move(Movement.BOTTOM_LEFT, (self.camera.speed // PLAYER_DIAGONAL_COEFF, -self.camera.speed // PLAYER_DIAGONAL_COEFF), self.camera, frequence.get_fps())
        elif keys[pygame.K_s] and (not keys[pygame.K_q]) and keys[pygame.K_d]:
            # move bottom right
            self.player.move(Movement.BOTTOM_RIGHT, (-self.camera.speed // PLAYER_DIAGONAL_COEFF, -self.camera.speed // PLAYER_DIAGONAL_COEFF), self.camera, frequence.get_fps())