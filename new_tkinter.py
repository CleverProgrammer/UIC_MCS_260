import week_2.project_1
from tkinter import Tk, Button, Label, Entry


class TorchelliApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.entry = Entry(self)
        self.entry2 = Entry(self)
        self.entry3 = Entry(self)

        self.label1 = Label(self, text="Area")
        self.label2 = Label(self, text="Area")
        self.label3 = Label(self, text="Area")

        self.label1.pack()
        self.entry.pack()

        self.label2.pack()
        self.entry2.pack()

        self.label3.pack()
        self.entry3.pack()

        self.button = Button(self, text="Calculate Now!", command=self.on_button)
        self.button.pack()

    def on_button(self):
        e1 = self.entry.get()
        e2 = self.entry2.get()
        e3 = self.entry3.get()
        print(e1, e2, e3)


app = TorchelliApp()
app.mainloop()
