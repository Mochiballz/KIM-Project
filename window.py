
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from kensuke import *

class Application(ttk.Frame):
    def __init__(self, master=None, k=None):
        super().__init__(master)
        self.master = master
        self.kensuke = k
        self.grid()
        self["relief"] = "raised"
        self["borderwidth"] = 3
        self.create_widgets()
        self.draw_canvases()
        
    def create_viewports(self):
        # Default values
        WIDTH = 600
        HEIGHT = 400
        BG_COLOR = "#F0F0F0"
        RELIEF = "sunken"
        BW = 3
        
        # Canvas creation for images (styling placed upon creation)
        self.origin_view = Canvas(self, width=WIDTH, height=HEIGHT, background=BG_COLOR,
                                  relief=RELIEF, borderwidth=BW)
        self.origin_view.grid(row=0, column=0, columnspan=4, padx=20, pady=20, sticky=N+S+E+W)
        self.origin_view.grid_propagate(0)

        self.distort_view = Canvas(self, width=WIDTH, height=HEIGHT, background=BG_COLOR,
                                   relief=RELIEF, borderwidth=BW)
        self.distort_view.grid(row=0, column=4, columnspan=4, padx="0 20", pady=20, sticky=N+S+E+W)
        self.distort_view.grid_propagate(0)
        
    def create_controls(self):
        # Default values
        SCALE_LENGTH = 160
        MAX_X = 100
        MAX_Y = 100
        MAX_W = 50
        MAX_H = 50
        
        # Sliders for the top left position of cell array (x, y) w/ labels
        self.x = ttk.Scale(self, orient="horizontal", style="Horizontal.TScale", length=SCALE_LENGTH,
                           from_=0, to=MAX_X)
        self.y = ttk.Scale(self, orient="horizontal", style="Horizontal.TScale", length=SCALE_LENGTH,
                           from_=0, to=MAX_Y)

        self.x_label = ttk.Label(self, text="X Coordinate: ")
        self.y_label = ttk.Label(self, text="Y Coordinate: ")

        self.x_label.grid(row=1, column=0, columnspan=1, padx="20 0", sticky=N+S+W)
        self.x.grid(row=1, column=0, columnspan=2, padx="10 20", sticky=N+S+E)
        self.y_label.grid(row=1, column=2, columnspan=1, padx="0 0", sticky=N+S+W)
        self.y.grid(row=1, column=2, columnspan=2, padx="10 20", sticky=N+S+E)
        
        # Cell size sliders (width, height)
        self.width = ttk.Scale(self, orient="horizontal", style="Horizontal.TScale", length=SCALE_LENGTH,
                               from_=1, to=MAX_W)
        self.height = ttk.Scale(self, orient="horizontal", style="Horizontal.TScale", length=SCALE_LENGTH,
                                from_=1, to=MAX_H)
        
        self.w_label = ttk.Label(self, text="Cell Width: ")
        self.h_label = ttk.Label(self, text="Cell Height: ")

        self.w_label.grid(row=2, column=0, columnspan=1, padx="20 0", pady="10 20", sticky=N+S+W)
        self.width.grid(row=2, column=0, columnspan=2, padx="10 20", pady="10 20", sticky=N+S+E)
        self.h_label.grid(row=2, column=2, columnspan=1, padx="0 0", pady="10 20", sticky=N+S+W)
        self.height.grid(row=2, column=2, columnspan=2, padx="10 20", pady="10 20", sticky=N+S+E)
        
        # Padding slider (one for both x and y)

        # Row input box

        # Column input box

        # Radio button for resizing distorted image

        self.set_control_values()

        # Implement update function when widget's state is changed
        self.x.configure(command=self.update)
        self.y.configure(command=self.update)
        self.width.configure(command=self.update)
        self.height.configure(command=self.update)

    def create_styles(self):
        self.style = ttk.Style(self)
        self.style.configure("Horizontal.TScale", troughcolor="#F0F0F0", background="green",
                             sliderthickness=20, borderwidth=2)

    def create_widgets(self):
        self.create_styles() # Implement styles for widgets
        self.create_viewports() # Create canvases for original and distorted image
        self.create_controls() # Parameter control widgets created

    def draw_canvases(self):
        if self.kensuke is None:
            print("None")
            return

        # -- Original image canvas --
        origin_obj_ids = self.origin_view.find_all()
        if len(origin_obj_ids) > 0:
            for i in origin_obj_ids: self.origin_view.delete(i)

        # Canvas resize
        image_dim = self.kensuke.image.size
        if image_dim[0] > int(self.origin_view["width"]):
            self.origin_view["width"] = image_dim[0]

        # Original image draw
        tkimage = ImageTk.PhotoImage(self.kensuke.image)
        self.origin_view.create_image(0, 0, anchor=NW, image=tkimage)
        self.origin_view.image = tkimage

        self.draw_grid()

        # -- Distorted image canvas --
        distort_obj_ids = self.distort_view.find_all()
        if len(distort_obj_ids) > 0:
            for i in distort_obj_ids: self.distort_view.delete(i)

        # Canvas resize
        distort_dim = self.kensuke.distorted.size
        if distort_dim[0] > int(self.distort_view["width"]):
            self.distort_view["width"] = distort_dim[0]

        # Distorted image draw
        tkdistort = ImageTk.PhotoImage(self.kensuke.distorted)
        self.distort_view.create_image(0, 0, anchor=NW, image=tkdistort)
        self.distort_view.image = tkdistort

    def draw_grid(self):
        for i in range(self.kensuke.rows):
            for j in range(self.kensuke.cols):
                temp = self.kensuke
                x0 = temp.x + (j * temp.w) + (j * temp.padding)
                y0 = temp.y + (i * temp.h) + (i * temp.padding)
                x1 = x0 + temp.w
                y1 = y0 + temp.h

                self.origin_view.create_rectangle(x0, y0, x1, y1, outline="cyan")

    def set_control_values(self):
        temp = self.kensuke
        self.x["value"] = temp.x
        self.y["value"] = temp.y
        self.width["value"] = temp.w
        self.height["value"] = temp.h

    def set_kensuke(self, k=None):
        if k is None:
            return
        self.kensuke = k

    def update(self, value):
        # Grabbing values from all scales
        self.kensuke.x = self.x.get()
        self.kensuke.y = self.y.get()
        self.kensuke.w = int(self.width.get())
        self.kensuke.h = int(self.height.get())

        # Create new cells and assemble them
        self.kensuke.create_cells()
        self.kensuke.assemble_cells()

        # Redraw viewports
        self.draw_canvases()
        

root = Tk()
ktest = Kensuke(create_image("sample_imgs/husky_puppy.jpg"), 10, 12, 20, 10, 10, 20, 20)
ktest.create_cells()
ktest.assemble_cells()

app = Application(root, ktest)
app.mainloop()
