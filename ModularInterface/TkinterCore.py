import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
import numpy as np
class Window:
    """
    A class to create a basic Tkinter window.
    """
    def __init__(self,title = "ModularInterface Window"):
        """
        Initializes the main application window and its widgets.
        """
        # Create the main window object
        self.root = tk.Tk()

        # Set the title of the window
        self.root.title(title)

        # Set the size of the window (width x height)
        self.root.geometry("400x300")

        # Create a simple label widget and add it to the window
        #self.label = tk.Label(self.root, text="Hello, Tkinter!", font=("Helvetica", 16))

        # Use the pack geometry manager to place the label in the window.
        # pady adds some vertical padding for better aesthetics.
        #self.label.pack(pady=20)
        self.root.after(2,self.ensure_no_freeze)

    def ensure_no_freeze(self):
        #print("test")
        self.root.update()
        self.root.after(2,self.ensure_no_freeze)
        

        

    def run(self):
        """
        Starts the main event loop, which listens for user interactions
        and keeps the window open until the user closes it.
        """
        self.root.mainloop()

class ImageManager:
    def __init__(self,image,photo_image,canvas,canvas_image,height = 64,width = 64):
        pass
        self.image = image
        self.photo_image = photo_image
        self.canvas = canvas
        self.image_width = width
        self.image_height = height
        self.canvas_image = canvas_image
    def set_pixel(self, x, y, color):
        """
        Changes the color of a single pixel on the image.

        Args:
            x (int): The x-coordinate of the pixel.
            y (int): The y-coordinate of the pixel.
            color (tuple): An RGB tuple, e.g., (255, 0, 0) for red.
        """
        # Check if the coordinates are within the image boundaries
        if 0 <= x < self.image_width and 0 <= y < self.image_height:
            # Modify the pixel on the PIL Image object
            self.image.putpixel((x, y), color)

            # Update the Tkinter PhotoImage to reflect the changes
            self.photo_image = ImageTk.PhotoImage(self.image)

            # Update the canvas to display the new PhotoImage
            self.canvas.itemconfig(self.canvas_image, image=self.photo_image)
        else:
            print(f"Coordinates ({x}, {y}) are out of bounds.")
    def update_image(self):
        self.photo_image = ImageTk.PhotoImage(self.image)
        self.canvas.itemconfig(self.canvas_image, image=self.photo_image)
    def fill_image(self,color):
        self.image.paste(color,(0,0,self.image_width,self.image_height))


#from PIL import Image, ImageTk, ImageDraw
def DrawImage(IM = None, positions = [],color = (0,0,255)):
    if IM == None:
        return
    
    #IM.set_pixel(0,0,color)
    data = np.array(IM.image)
    #data[1,0] = color
    #print(data,data[0,0])
    for x,y in positions:
        if x > 0 and y > 0:
            if x < IM.image_width and y < IM.image_height:
                data[x,y] = color
        #pass
        #IM.set_pixel(x,y,color)
    IM.image = Image.fromarray(data)

def AddCanvas(self,height,width):
    self.image_height = height
    self.image_width = width
    self.canvas = tk.Canvas(self.root, width=self.image_width, height=self.image_height, bg="lightgray")
    self.canvas.pack(pady=10)


def AddImage(self,height,width):

    self.image_height = height
    self.image_width = width

    self.image = Image.new("RGB", (self.image_width, self.image_height), "white")
    self.photo_image = ImageTk.PhotoImage(self.image)
    AddCanvas(self,height,width)
    self.canvas_image = self.canvas.create_image(0, 0, image=self.photo_image, anchor="nw")
    self.ImageManager = ImageManager(self.image,self.photo_image,self.canvas,self.canvas_image,self.image_height,self.image_width)

if __name__ == "__main__":
    pass
    # This block of code is executed only when the script is run directly.
    # Create an instance of our App class
    #app = App()
    #app1 = App()

    # Call the run method to display the window
    #app.run()
    #app1.run()
