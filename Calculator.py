from tkinter import *

class Calculator(Frame):
    def __init__(self):
        Frame.__init__(self, bg = "blue")
        self.option_add("*font", "arial 25 bold")
        self.pack(expand = YES, fill = BOTH )
        self.master.title("Mja Calculator")

        display = StringVar()
        obj = Entry(self, relief = RIDGE, textvariable = display, justify = "right",
                    bd = 20, bg = "powder blue", width = 20)
        obj.pack(side = TOP, expand = YES, fill = BOTH)

        clear_button = Button(self, text = 'C', bg = 'white', bd = 2,
                              command = lambda stored = display: stored.set("") )
        clear_button.pack(side = TOP, expand = YES, fill = BOTH)

        for exp in ("987/", "456*", "123-", "0.+"):
            frame = Frame(self, bd = 1.5, bg = 'silver')
            frame.pack(side = TOP, expand = YES, fill = BOTH)
            for char in exp:
                butt = Button(frame, text = char, bg = 'white',
                              command =  lambda stored = display, ch = char: stored.set(stored.get()+ch))
                butt.pack(side = LEFT, expand = YES, fill = BOTH)



Calculator().mainloop()
