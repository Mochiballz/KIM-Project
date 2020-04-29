import sys
import math

from PIL import Image, ImageTk

'''
 Kensuke Koike Editor: Manipulate images in a collage-like style, using smaller rectangular cutouts of
 a source image to create new distorted works of art! Current use of this application only allows the
 user to take a spaced grid sample of a file and stitch its neighboring parts together, resizing it to
 match the proportions of the original image.

'''

# Base class for containing the image manipulation variables
# The 'image' parameter must take a PIL image, NOT a string filename
class Kensuke(object):
    # Constructor
    def __init__(self, image, rows=None, cols=None, p=2, x=0, y=0, w=2, h=2):
        self.image = image
        self.distorted = None
        self.cells = []
        
        self.rows = rows
        self.cols = cols
        self.padding = p

        # Starting coordinates (x,y) & cell width/height for each cutout
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def create_gridbox(self):
        grid_w = (self.cols * self.w) + ((self.cols - 1) * self.padding) + self.x
        grid_h = (self.rows * self.h) + ((self.rows - 1) * self.padding) + self.y
        gridbox = (self.x, self.y, grid_w, grid_h)
        return gridbox
    
    # Function will create image cells based on instance's parameters
    def create_cells(self):
        if self.rows and self.cols: # Checks if rows or cols are empty
            
            if len(self.cells) > 0:
                self.cells = [] # Creates new cell grid
            for i in range(self.rows):
                row = []
                for j in range(self.cols):
                    
                    left  = self.x + (j * self.w) + (j * self.padding)
                    upper = self.y + (i * self.h) + (i * self.padding)
                    right = left + self.w
                    lower = upper + self.h
                    
                    box = (left, upper, right, lower)
                    cell = self.image.crop(box)
                    row.append(cell)
                        
                self.cells.append(row)
                    
        else:
            print("Your rows and/or columns are not defined")

    # Collages all cells into new image, defining it in the instance's 'distorted' variable
    # Constructs cells in default 'lower resolution' grid pattern
    def assemble_cells(self):
        width = len(self.cells[0]) * self.w
        height = len(self.cells) * self.h
        size = (width, height)
        
        self.distorted = Image.new("RGB", size)

        for i in range(len(self.cells)):
            for j in range(len(self.cells[0])):
                
                left  = j * self.w
                upper = i * self.h
                right = left + self.w
                lower = upper + self.h

                box = (left, upper, right, lower)
                self.distorted.paste(self.cells[i][j], box)

    def resize_distorted(self, mode=0):
        image_dim = self.image.size
        distort_dim = self.distorted.size
        if mode == 0:
            self.distorted = self.distorted.resize(image_dim)
        pass

    # Checks if cell grid will fit within original image dimensions --> (should be placed before distortion)
    def inside_image_dim(self):
        image_dim = self.image.size
        grid_dim = self.create_gridbox()
        return (image_dim[0] <= grid_dim[0] and image_dim[1] <= grid_dim[1]) and (image_dim[2] >= grid_dim[2] and image_dim[3] >= grid_dim[3])
                

# Returns a PIL image variable
def create_image(filename):
    try:
        image = Image.open(filename)
        return image
    except Exception as e:
        print(e)

    


