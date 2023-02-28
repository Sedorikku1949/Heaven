import pygame
import json

# Initialize Pygame
pygame.init()

# Set the dimensions of the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

# Create the game window
window = pygame.display.set_mode(WINDOW_SIZE)

# Load the tileset image
TILESET_IMAGE_PATH = 'natureset.png'
tileset_image = pygame.image.load(TILESET_IMAGE_PATH).convert_alpha()

# Load the map JSON
MAP_JSON_PATH = 'map.json'
with open(MAP_JSON_PATH) as map_file:
    map_data = json.load(map_file)

# Extract the tile size and map dimensions from the JSON
TILE_SIZE = 
MAP_WIDTH = map_data['width']
MAP_HEIGHT = map_data['height']

# Create a list to hold the tiles
tiles = []

# Loop through each layer in the map JSON
for layer in map_data['layers']:
    # Only process tile layers
    if layer['type'] == 'tilelayer':
        # Loop through each tile in the layer
        for i, tile in enumerate(layer['data']):
            # Skip any empty tiles
            if tile == 0:
                continue
            # Calculate the position of the tile on the screen
            x = (i % MAP_WIDTH) * TILE_SIZE
            y = (i // MAP_WIDTH) * TILE_SIZE
            # Calculate the tile index in the tileset
            tile_index = tile - 1
            # Calculate the row and column of the tile in the tileset
            tile_row = tile_index // (tileset_image.get_width() // TILE_SIZE)
            tile_col = tile_index % (tileset_image.get_width() // TILE_SIZE)
            # Create a rect to represent the tile in the tileset
            tile_rect = pygame.Rect(tile_col * TILE_SIZE, tile_row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            # Create a rect to represent the position of the tile on the screen
            screen_rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
            # Add the tile and its position to the list
            tiles.append((tileset_image, tile_rect, screen_rect))

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Draw the tiles
    for tile in tiles:
        window.blit(*tile)
    # Update the screen
    pygame.display.flip()

# Clean up
pygame.quit()

