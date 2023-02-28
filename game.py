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

    def draw(self, screen: pygame.Surface) -> None:
        screen.fill((0, 0, 0))

        self.map.draw(screen, self.assets, self.camera)
        self.player.draw(screen, self.assets, self.camera, self.map)
        self.ui.draw(UiDrawArguments(self.player, self.ui_assets, screen))

    def update(self, frequence: pygame.time.Clock) -> None:
        self.player.x = self.camera.x
        self.player.y = self.camera.y

        self.movements(frequence)

        self.player.update(frequence)
        self.ui.update(frequence, self.player, self.map)

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

        elif keys[pygame.K_e]:
            # TODO: trop réactif
            self.player.inventory_open = not self.player.inventory_open
