from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class PlotPicture(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.title('Plot Picture')
        self.geometry('560x360')


        self.pic = self.readPic()

        self.frame1 = Frame(self)
        self.frame1.config(relief = 'groove', bd = 5)
        self.frame1.place(x = 20, y = 20) 
        self.scrollbar = ttk.Scrollbar(self.frame1, orient = VERTICAL) 
        self.listbox = Listbox(self.frame1, font = ('Arial', 20), yscrollcommand = self.scrollbar.set, width = 10, heigh = 5)
        self.scrollbar.config(command = self.listbox.yview)
        self.scrollbar.pack(side = RIGHT, fill = Y)
        self.listbox.pack(padx = 5, pady = 5)

        for i in range(len(self.pic.keys())):
            text = 'Pic '+str(i+1)
            self.listbox.insert(END, text)

        self.listbox.bind('<<ListboxSelect>>', self.displayLabel)


        self.button = Button(self, text = 'Plot', font = ('tahoma', 15), width = 10, command = self.displayPicture)
        self.button.config(relief = 'groove', bd =5)
        self.button.place(x = 45, y = 230)


        self.frame2 = Frame(self)
        self.frame2.config(relief = 'groove', bd = 5)
        self.frame2.place(x = 230, y = 20)
        self.canvas = Canvas(self.frame2, width = 300, heigh = 300, bg = 'white')
        self.canvas.pack()
        self.label = Label(self.frame2)
        self.label.pack()


    def readPic(self):
        pic1 = Image.open('Pic/HCMUT_official_logo.png')
        pic1_rs = pic1.resize((200,200), Image.ANTIALIAS)
        convert_pic1 = ImageTk.PhotoImage(pic1_rs)
        text1 = 'Logo HCMUT official'
        
        pic2 = Image.open('Pic/Python.jpg')
        pic2_rs = pic2.resize((200,200), Image.ANTIALIAS)
        convert_pic2 = ImageTk.PhotoImage(pic2_rs)
        text2 = 'Logo Python'
        
        pic3 = Image.open('Pic/dora.jpg')
        pic3_rs = pic3.resize((200,200), Image.ANTIALIAS)
        convert_pic3 = ImageTk.PhotoImage(pic3_rs)
        text3 = 'Doraemon'

        pic4 = Image.open('Pic/Facebook.png')
        pic4_rs = pic4.resize((200,200), Image.ANTIALIAS)
        convert_pic4 = ImageTk.PhotoImage(pic4_rs)
        text4 = 'Logo Facebook'

        pic5 = Image.open('Pic/ubuntu-logo.jpg')
        pic5_rs = pic5.resize((200,200), Image.ANTIALIAS)
        convert_pic5 = ImageTk.PhotoImage(pic5_rs)
        text5 = 'Logo Ubuntu Linux'

        pic6 = Image.open('Pic/starbuck.jpg')
        pic6_rs = pic6.resize((200,200), Image.ANTIALIAS)
        convert_pic6 = ImageTk.PhotoImage(pic6_rs)
        text6 = 'Logo Starbucks'



        listPic = {
                    text1:convert_pic1,
                    text2:convert_pic2,
                    text3:convert_pic3,
                    text4:convert_pic4,
                    text5:convert_pic5,
                    text6:convert_pic6
        }

        return listPic

    def displayPicture(self):
        value = self.listbox.get(ACTIVE)
        indice = int(value[-1])-1
        text = list(self.pic.keys())

        pos = text[indice]
        self.canvas.create_image(50,50, image = self.pic[pos], anchor = NW)

    def displayLabel(self, event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            data = event.widget.get(index)
            indice = int(data[-1])-1
            text = list(self.pic.keys())
            self.label.config(text = text[indice])
        else:
            self.label.config(text = "")

plotP = PlotPicture()
plotP.mainloop()