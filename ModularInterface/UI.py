



def ActivateCore(core = "tk"):
    if core == "tk":
        import ModularInterface.TkinterCore

        
        ModularInterface.Core = ModularInterface.TkinterCore


def FillImage(IM = None,color = (0,0,0)):
    if IM == None:
        return
    IM.fill_image(color)
    """
    for x in range(0,IM.image_width):
        for y in range(0,IM.image_height):
            IM.set_pixel(x,y,color)
    """

"""
from PIL import Image, ImageTk, ImageDraw
def DrawImage(IM = None, positions = [],color = (0,0,255)):
    if IM == None:
        return
    
    #IM.set_pixel(0,0,color)
    data = np.array(IM.image)
    #data[1,0] = color
    #print(data,data[0,0])
    for x,y in positions:
        data[x,y] = color
        #pass
        #IM.set_pixel(x,y,color)
    IM.image = Image.fromarray(data)
"""
