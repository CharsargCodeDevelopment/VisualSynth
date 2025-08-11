import pygame
import sys
import numpy as np

# A class to act as a container for our window and images
class Window:
    def __init__(self, title="ModularInterface Window", width=400, height=300):
        # Pygame initialization
        pygame.init()
        self.screen_width = width
        self.screen_height = height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption(title)

        self.running = True
        self.clock = pygame.time.Clock()
        self.ImageManager = None
        self.image_position = (0, 0) # Top-left position to draw the image

    def run(self):
        """
        Starts the main event loop.
        """
        while self.running:
            # Event handling loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Fill the screen to clear it before drawing the new frame
            self.screen.fill((100, 100, 100)) # Light gray background

            # If an image manager exists, blit its surface to the screen
            if self.ImageManager:
                self.screen.blit(self.ImageManager.image_surface, self.image_position)

            # Update the entire screen
            pygame.display.flip()

            # Cap the frame rate
            self.clock.tick(60)

        pygame.quit()
        sys.exit()
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        #pygame.event.wait()

        
        
        pygame.display.flip()
        #self.clock.tick(60)

class ImageManager:
    def __init__(self, image_surface, width=64, height=64,screen = None):
        self.image_surface = image_surface
        self.image_width = width
        self.image_height = height
        self.screen = screen

    def set_pixel(self, x, y, color):
        """
        Changes the color of a single pixel on the image surface.
        """
        if 0 <= x < self.image_width and 0 <= y < self.image_height:
            self.image_surface.set_at((x, y), color)
        else:
            print(f"Coordinates ({x}, {y}) are out of bounds.")
    
    def update_image(self):
        if self.image_surface:
            self.screen.blit(self.image_surface, self.image_position)
        """
        In Pygame, the surface is already updated, so we don't need to do
        anything here. The main loop will handle blitting it to the screen.
        """
        pass

    def fill_image(self, color):
        """
        Fills the entire image surface with a solid color.
        """
        self.image_surface.fill(color)


def DrawImage(IM, positions, color=(0, 0, 255)):
    """
    Port of the original DrawImage function using Pygame's PixelArray.
    This is a more efficient way to draw multiple pixels at once.
    """
    if IM is None:
        return
    
    # Use PixelArray for fast pixel access
    # This locks the surface and provides a 2D array-like object
    pixel_array = pygame.PixelArray(IM.image_surface)
    
    for x, y in positions:
        
        if 0 <= x < IM.image_width and 0 <= y < IM.image_height:
            
            pixel_array[x, y] = color
    
    # Unlock the surface and free the PixelArray object
    del pixel_array

def AddCanvas(self, height, width):
    # This function is not needed in Pygame. The main screen serves this purpose.
    # We will instead create the image surface in AddImage.
    pass

def AddImage(self, height, width, position=(0,0)):
    """
    Port of the original AddImage.
    Creates a Pygame Surface and a PygameImageManager.
    """
    self.image_height = height
    self.image_width = width
    
    # Create the Pygame Surface (equivalent of PIL.Image)
    image_surface = pygame.Surface((self.image_width, self.image_height))
    image_surface.fill((255, 255, 255)) # Fill with white
    
    # Create the PygameImageManager
    self.ImageManager = ImageManager(image_surface, self.image_width, self.image_height,self.screen)
    self.image_position = position
    self.ImageManager.image_position = position


# Example usage with the ported classes and functions
if __name__ == "__main__":
    # Create an instance of our PygameWindow class
    app = Window()
    
    # Create an image inside the window
    # The AddImage function now takes a position argument for drawing
    AddImage(app, height=64, width=64, position=(50, 50))

    app.ImageManager.fill_image((255,0,0))
    # Use the ported DrawImage function
    points_to_draw = [(10, 10), (11, 11), (12, 12), (13, 13)]
    DrawImage(app.ImageManager, positions=points_to_draw, color=(0, 0, 255))
    
    # Call the run method to start the Pygame loop
    app.run()
