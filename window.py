
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
        pass
        
    def create_image_viewports(self):
        pass

    def create_param_controls(self):
        pass

    def create_widgets(self):
        img_original = self.kensuke.image
        img_distorted = self.kensuke.distorted
        
        tkorigin = ImageTk.PhotoImage(img_original)
        tkdistort = ImageTk.PhotoImage(img_distorted)
        
        # Implement styles for widgets
        self.originalStyle = ttk.Style(self)
        self.originalStyle.configure("OG.TLabel", foreground="white", background="gray", relief="raised",
                                     borderwidth=4, image=tkorigin)
        self.originalStyle.image = tkorigin

        self.distortedStyle = ttk.Style(self)
        self.distortedStyle.configure("DS.TLabel", foreground="white", background="gray", relief="raised",
                                      borderwidth=4, image=tkdistort)
        self.distortedStyle.image = tkdistort

        self.scaleStyle = ttk.Style(self)
        self.scaleStyle.configure("Horizontal.TScale", troughcolor="#F0F0F0", background="green",
                                  sliderthickness=20, borderwidth=2) 

        # Create label boxes for original and distorted image
        self.original = ttk.Label(self, style="OG.TLabel")
        self.original.grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky=N+S+E+W)
        self.original.grid_propagate(0)

        self.distorted = ttk.Label(self, style="DS.TLabel")
        self.distorted.grid(row=0, column=2, columnspan=2, padx="0 20", pady=20, sticky=N+S+E+W)
        self.distorted.grid_propagate(0)
        
        # Cell position sliders (x coordinate, y coordinate)

        self.x = ttk.Scale(self, orient="horizontal", style="Horizontal.TScale")
        self.y = ttk.Scale(self, orient="horizontal", style="Horizontal.TScale")

        self.x.grid(row=1, column=0, columnspan=1, padx="20 0", sticky=N+S+E+W)
        self.y.grid(row=1, column=1, columnspan=1, padx="10 20", sticky=N+S+E+W)
        
        # Cell size sliders (width, height)

        self.width = ttk.Scale(self, orient="horizontal", style="Horizontal.TScale")
        self.height = ttk.Scale(self, orient="horizontal", style="Horizontal.TScale")

        self.width.grid(row=2, column=0, columnspan=1, padx="20 0", pady="10 20", sticky=N+S+W+E)
        self.height.grid(row=2, column=1, columnspan=1, padx="10 20", pady="10 20", sticky=N+S+W+E)
        
        # Padding slider (one for both x and y)

        # Row input box

        # Column input box

        # Radio button for resizing distorted image

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
