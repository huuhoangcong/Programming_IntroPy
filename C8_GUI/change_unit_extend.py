from tkinter import *


class ChangeUnit(Tk):
    
    def __init__(self):        
        self.units = {
                      "Weight":      ["g", "kg", "lb", "ton"],
                      "Length":      ["mm", "cm", "m", "km", "inch", "foot", "mile"], 
                      "Area":        ["mm^2", "cm^2", "m^2", "km^2", "in^2", "ft^2", "mile^2"],
                      "Volume":      ["cm^3", "m^3", "in^3", "ml", "l", "gal"] ,
                      "Temperature": ["C", "F", "K"],
                      "Speed":       ["mm/s", "m/s", "km/s", "mph"],
                      "Pressure":    ["bar", "Pa", "kPa", "MPa", "atm"],
                      "Power":       ["W", "kW", "MW", "hp"]
                     }

        Tk.__init__(self)
        self.title("Change Unit")
        self.chooseType_Of_Unit = StringVar()
        self.chooseUnit = StringVar()
        self.chooseUnit_change = StringVar()
        
        self.chooseType_Of_Unit.trace('w', self.update_options)

        self.option1 = OptionMenu(self, self.chooseType_Of_Unit, *self.units.keys())
        self.option1.grid(row = 0, columnspan = 3)

        self.option2 = OptionMenu(self, self.chooseUnit, '')
        self.option2.grid(row = 2, column = 0)
        self.option3 = OptionMenu(self, self.chooseUnit_change, '')
        self.option3.grid(row = 2, column = 2)
        
        self.chooseType_Of_Unit.set("Choose Type of Unit")
        self.chooseUnit.set("Choose unit")
        self.chooseUnit_change.set("Choose unit")
        
        self.entry1 = Entry(self, justify = CENTER, bd = 2)
        self.entry1.grid(row = 1, column = 0)

        self.e2 = StringVar()
        self.entry2 = Entry(self, justify = CENTER, bd = 2, textvariable = self.e2)
        self.entry2.grid(row = 1, column = 2)

        self.button = Button(self, text = "=", width = 10, command = self.change)
        self.button.grid(row = 1, column = 1)


    def update_options(self, *arg):
        unit = self.units[self.chooseType_Of_Unit.get()]
        self.chooseUnit.set("Choose unit")
        self.chooseUnit_change.set("Choose unit")

        menu1 = self.option2['menu']
        menu2 = self.option3['menu']

        menu1.delete(0, 'end')
        menu2.delete(0, 'end')

        for i in unit:
            menu1.add_command(label = i, command = lambda position = i: self.chooseUnit.set(position))
            menu2.add_command(label = i, command = lambda position = i: self.chooseUnit_change.set(position))
        
    
    
    def change(self, *arg):

        const = [
            [1, 1e-3, 0.0022046, 1.10231131e-6],
            [1, 0.1, 1e-3, 1e-6, 0.03937, 0.003281, 6.213712e-7],
            [1, 0.1**2, (1e-3)**2, (1e-6)**2, 0.03937**2, 0.003281**2, (6.213712e-7)**2],
            [1, 1e-6, 0.03937**3, 1, 0.001, 0.00026417],
            [],
            [1, 0.001, 1e-6, 0.00223693629],
            [1, 100000, 100, 0.1, 0.986923267],
            [1, 1000, 1e+6, 0.00134102209],
        ]

        value = float(self.entry1.get())
        t_un = self.chooseType_Of_Unit.get()
        un = self.chooseUnit.get()
        un_c = self.chooseUnit_change.get()
        keys = list(self.units.keys())

        for i in range(len(keys)):
            if t_un == keys[i]:
                pos = i
                break

        u = self.units.get(self.chooseType_Of_Unit.get())
        dv = const[pos]
        if dv == []:
            if un == 'C':
                if un_c == 'F':
                    result = self.CtoF()
                elif un_c == 'K':
                    result = float(self.entry1.get())+273
                else:
                    result = float(self.entry1.get())
            elif un == 'F':
                if un_c == 'C':
                    result = self.FtoC()
                elif un_c == 'K':
                    result = self.FtoC()+273
                else:
                    result = float(self.entry1.get())
            else:
                if un_c == 'C':
                    result = float(self.entry1.get())-273
                elif un_c == 'F':
                    result = self.CtoF(float(self.entry1.get())-273)
                else:
                    result = float(self.entry1.get())

        else:
            for i in range(len(u)):
                if u[i] == un:
                    indice = i
                elif u[i] == un_c:
                    indice_c = i                

            result = round((value/dv[indice])*dv[indice_c],3)

        self.e2.set(result)

    def CtoF(self):
        value = float(self.entry1.get())
        return (value*9/5)+32

    def FtoC(self):
        value = float(self.entry1.get())
        return (value-32)*5/9



change = ChangeUnit()
change.mainloop()