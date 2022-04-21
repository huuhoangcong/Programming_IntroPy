from tkinter import *



def changeLengthUnit():
    length = float(E1.get())
    LU = lengthUnit.get()
    LU_c = lengthUnit_change.get()
    u = ["mm", "cm", "m", "km", "inch", "foot", "mile", "yard"]
    mm = [1, 0.1, 1e-3, 1e-6, 0.03937, 0.003281, 6.213712e-7, 0.00109361]

    for i in range(len(u)):
        if u[i] == LU:
            indice = i
        if u[i] == LU_c:
            indice_c = i

    result = round((length/mm[indice])*mm[indice_c],3)

    E2.set(result)


root = Tk()
root.resizable(height = False, width = False)
root.title("Change length unit")

def Center(root):
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x1 = (root.winfo_screenwidth()//2)-(width//2)
    y1 = (root.winfo_screenheight()//2)-(height//2)
    root.geometry('{}x{}+{}+{}'.format(width,height,x1,y1))

    
Label(root, text = "Length",
            justify = CENTER).grid(row = 0, columnspan = 3)

E1 = Entry(root, justify = CENTER,
                 width = 20,
                 bd = 2)

E1.grid(row = 1, column = 0)

E2 = StringVar()
Entry(root, justify = CENTER,
            width = 20,
            bd = 2,
            textvariable = E2).grid(row = 1, column = 2)


Button(root, text = "=",
             width = 10,
             command = changeLengthUnit).grid(row = 1, column = 1)


lengthUnit = StringVar()
lengthUnit.set("Choose unit")
lengthUnit_change = StringVar()
lengthUnit_change.set("Choose unit")


drop1 = OptionMenu(root, lengthUnit, "mm", "cm", "m", "km", "inch", "foot", "mile", "yard")
drop1.grid(row = 2, column = 0)

drop2 = OptionMenu(root, lengthUnit_change, "mm", "cm", "m", "km", "inch", "foot", "mile", "yard")
drop2.grid(row = 2, column = 2)

Center(root)
root.mainloop()