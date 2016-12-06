from week_2.project_1 import project_1 as Project_1
from tkinter import Tk, Button, Label, Entry


class TorchelliApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.entry = Entry(self)
        self.entry2 = Entry(self)
        self.entry3 = Entry(self)

        self.label1 = Label(self, text="a")
        self.label2 = Label(self, text="A")
        self.label3 = Label(self, text="H")

        self.label1.pack()
        self.entry.pack()

        self.label2.pack()
        self.entry2.pack()

        self.label3.pack()
        self.entry3.pack()

        self.button = Button(self, text="Calculate Now!", command=self.on_button)
        self.button.pack()

    def on_button(self):
        a = float(self.entry.get())
        A = float(self.entry2.get())
        H = float(self.entry3.get())
        print(a, A, H)
        drain_time_secs = Project_1.drain_time_secs(a, A, H)
        print(Project_1.calculate(drain_time_secs))



app = TorchelliApp()
app.mainloop()
