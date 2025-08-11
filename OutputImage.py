from PIL import Image, ImageTk, ImageDraw
import numpy as np

def DrawImage(positions = [],color = (0,255,0)):
    width = 1024
    height = 1024
    im = Image.new(mode="RGB", size=(width, height))
    #IM.set_pixel(0,0,color)
    data = np.array(im)
    #data[1,0] = color
    #print(data,data[0,0])
    positions = list(positions)
    if len(positions) == 0:
        return im
    x1,y1 = positions[0]
    for x,y in positions:
        if x > 0 and y > 0:
            if x < width and y < height:
                
                #data[x,y] = color
                draw_line(x,y,x1,y1,data,color)
                x1 = x
                y1 = y
        #pass
        #IM.set_pixel(x,y,color)
    im = Image.fromarray(data)
    return im


def draw_line(x1, y1, x2, y2, data, color):
    """
    Draws a line on the image data array using Bresenham's algorithm.
    """
    dx = abs(x2 - x1)
    dy = -abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx + dy  # error_from_start
    e2 = 0

    while True:
        # Check boundaries before drawing to prevent errors
        if 0 <= x1 < data.shape[0] and 0 <= y1 < data.shape[1]:
            data[y1, x1] = color
        
        if x1 == x2 and y1 == y2:
            break
        
        e2 = 2 * err
        if e2 >= dy:
            err += dy
            x1 += sx
        if e2 <= dx:
            err += dx
            y1 += sy
