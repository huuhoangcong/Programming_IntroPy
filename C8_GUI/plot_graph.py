from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk



class PlotChart(Tk):

    def __init__(self):
        self.function = [('sin(x)',1), ('cos(x)',2), ('sin(x)*cos(x)',3)]
        Tk.__init__(self)
        self.title("Plot chart")

        self.value = IntVar()
        self.value.set(1)
        self.first_value = IntVar(value = 0)
        
        
        self.frame1 =Frame(self)
        self.frame1.grid(row = 0, columnspan = 4)
        for function, val in self.function:
            self.option = Radiobutton(self.frame1, text = function, padx = 30, value = val, variable = self.value)
            self.option.pack(side = LEFT)
        
        self.plots = Button(self.frame1, text = "PLOT", padx = 30, command = self.plot_draw)
        self.plots.pack(side = LEFT)

        self.frame2 = Frame(self)
        self.frame2.grid(row = 1, columnspan = 4)
        self.figure = Figure(figsize = (5, 3.5))
        self.canvas = FigureCanvasTkAgg(self.figure, self.frame2)
        self.canvas.draw()
        self.canvas.get_tk_widget().configure(relief = 'groove', bd = 5)
        self.canvas.get_tk_widget().grid(row = 1, columnspan = 4)
        
        
        self.frame3 = Frame(self)
        self.frame3.grid(row = 2, columnspan = 4)
        
        self.x = IntVar(value = 1)
        self.x.trace('w', self.drawFunction)
        self.x_axis = Checkbutton(self.frame3, text = 'X', variable = self.x)
        self.x_axis.pack(side = LEFT)
        
        self.y = IntVar(value = 1)
        self.y.trace('w', self.drawFunction)
        self.y_axis = Checkbutton(self.frame3, text = 'Y', variable = self.y)
        self.y_axis.pack(side = LEFT)
       
        self.grid = IntVar(value = 1)
        self.grid.trace('w', self.drawFunction)
        self.draw_grid = Checkbutton(self.frame3, text = 'GRID', variable = self.grid)
        self.draw_grid.pack(side = LEFT)



    def drawFunction(self, *args):
        if self.first_value.get() == 1:
            if self.grid.get() == 0:
                grid_check = False
            else:
                grid_check = True
            if self.x.get() == 0:
                x_check = False
            else:
                x_check = True
            if self.y.get() == 0:
                y_check = False
            else:
                y_check = True

        figure = Figure(figsize = (5, 3.5), dpi = 100)
        x = np.arange(-2*np.pi, 2*np.pi, 0.01)
        y = [
            np.sin(x),
            np.cos(x),
            np.sin(x)*np.cos(x)
        ]
        for i in range(len(y)):
            if i == self.value.get()-1:
                a = figure.add_subplot()
                a.grid(grid_check)
                a.get_xaxis().set_visible(x_check)
                a.get_yaxis().set_visible(y_check)
                a.plot(x, y[i])

        self.canvas = FigureCanvasTkAgg(figure, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().configure(relief = 'groove', bd = 5)
        self.canvas.get_tk_widget().grid(row = 1, columnspan = 4)

    def plot_draw(self):
        self.first_value.set(1)
        self.drawFunction()

               
plotchart = PlotChart()
plotchart.mainloop()