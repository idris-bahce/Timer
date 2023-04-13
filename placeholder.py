from tkinter import *


class Placeholder:
    def __init__(self, master, placeholder='', placeholdercolor='grey', color='black', **kwargs):
        self.e = Entry(master, fg=placeholdercolor, **kwargs)
        self.e.bind('<FocusIn>', self.focus_in)
        self.e.bind('<FocusOut>', self.focus_out)
        self.e.insert(0, placeholder)
        self.placeholder = placeholder
        self.placeholdercolor = placeholdercolor
        self.color = color

    def pack(self, side=None, **kwargs):
        self.e.pack(side=side, **kwargs)

    def place(self, side=None, **kwargs):
        self.e.place(side=side, **kwargs)

    def grid(self, column=None, **kwargs):
        self.e.grid(column=column, **kwargs)

    def focus_in(self, e):
        if self.e.get() == self.placeholder:
            self.e.delete(0, END)
        self.e.configure(fg=self.color)

    def focus_out(self, e):
        if self.e.get() == '':
            self.e.configure(fg=self.placeholdercolor)
            self.e.delete(0, END)
            self.e.insert(0, self.placeholder)

    def get(self):
        return self.e.get()

    def set(self, time):
        return self.e.insert(END, string=time)
