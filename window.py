
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
        self.create_widgets()

    def create_styles(self):
        self.style = ttk.Style(self)
        self.style.configure("OG.TLabel", foreground="white", background="gray", relief="raised",
                             width=100, height=80, borderwidth=4)
        self.style.configure("DS.TLabel", foreground="white", background="gray", relief="raised",
                             width=100, height=80, borderwidth=4)
        self.style.configure("Horizontal.TScale", troughcolor="#F0F0F0", background="green",
                             sliderthickness=20, borderwidth=2)
        
    def create_image_viewports(self):
        self.origin_view = Canvas(self, background="gray", relief="raised",
                                  width=600, height=400, borderwidth=4)
        self.origin_view.grid(row=0, column=0, columnspan=4, padx=20, pady=20, sticky=N+S+E+W)
        self.origin_view.grid_propagate(0)

        self.distort_view = Canvas(self, background="gray", relief="raised",
                                   width=600, height=400, borderwidth=4)
        self.distort_view.grid(row=0, column=4, columnspan=4, padx="0 20", pady=20, sticky=N+S+E+W)
        self.distort_view.grid_propagate(0)
        '''
        self.original = ttk.Label(self, style="OG.TLabel")
        self.original.grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky=N+S+E+W)
        self.original.grid_propagate(0)
        
        self.distorted = ttk.Label(self, style="DS.TLabel")
        self.distorted.grid(row=0, column=2, columnspan=2, padx="0 20", pady=20, sticky=N+S+E+W)
        self.distorted.grid_propagate(0)
        '''
        
    def create_param_controls(self):
        # Cell position sliders (x coordinate, y coordinate)
        self.x = ttk.Scale(self, orient="horizontal", style="Horizontal.TScale", length=150)
        self.y = ttk.Scale(self, orient="horizontal", style="Horizontal.TScale", length=150)

        self.x_label = ttk.Label(self, text="X Coordinate: ")
        self.y_label = ttk.Label(self, text="Y Coordinate: ")

        self.x_label.grid(row=1, column=0, columnspan=1, padx="20 0", sticky=N+S+W)
        self.x.grid(row=1, column=0, columnspan=2, padx="10 0", sticky=N+S+E)
        self.y_label.grid(row=1, column=2, columnspan=1, padx="10 0", sticky=N+S+W)
        self.y.grid(row=1, column=2, columnspan=2, padx="10 20", sticky=N+S+E)
        
        # Cell size sliders (width, height)
        self.width = ttk.Scale(self, orient="horizontal", style="Horizontal.TScale")
        self.height = ttk.Scale(self, orient="horizontal", style="Horizontal.TScale")

        self.width.grid(row=2, column=1, columnspan=1, padx="20 0", pady="10 20", sticky=N+S+W+E)
        self.height.grid(row=2, column=3, columnspan=1, padx="10 20", pady="10 20", sticky=N+S+W+E)
        
        # Padding slider (one for both x and y)

        # Row input box

        # Column input box

        # Radio button for resizing distorted image

    def create_widgets(self):
        self.create_styles() # Implement styles for widgets
        self.create_image_viewports() # Create label boxes for original and distorted image
        self.create_param_controls() # Parameter control widgets created
        

    def set_kensuke(self, k=None):
        if k is None:
            return
        self.kensuke = k
        pass

root = Tk()
ktest = Kensuke(create_image("sample_imgs/kinkakuji.jpg"), 10, 12, 20, 10, 10, 20, 20)
ktest.create_cells()
ktest.assemble_cells()
ktest.resize_distorted()

app = Application(root, ktest)
app.mainloop()
