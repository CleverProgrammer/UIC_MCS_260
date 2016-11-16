from tkinter import Tk, Canvas, messagebox

window = Tk()
canvas = Canvas(window, width=1024, height=768, bg='blue')
canvas.pack()


def say_hello(event):
    x = str(event.x)
    y = str(event.y)
    print(x, y)
    messagebox.showinfo(message='hello')


canvas.bind('<Button-1>', say_hello)
print(dir(canvas))

if __name__ == '__main__':
    window.mainloop()
