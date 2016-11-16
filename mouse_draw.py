# L-30 MCS 260 Mon 28 Mar 2016 : mousedraw.py

"""
To illustrate the binding of mouse events
to canvas, we consider filling squares on
a grid on canvas via the mouse.
"""

from tkinter import Tk, Canvas, StringVar, Label


class FillSquares(object):
    """
    Filling squares on canvas with mouse clicks.
    """

    def bind_mouse_events(self):
        """
        binds mouse events to the canvas
        """
        self.cnv.bind("<Button-1>", self.button_pressed)
        self.cnv.bind("<ButtonRelease-1>", self.button_released)
        self.cnv.bind("<Enter>", self.entered_window)
        self.cnv.bind("<Leave>", self.exited_window)
        self.cnv.bind("<B1-Motion>", self.mouse_dragged)

    def __init__(self, wdw, r, c):
        """
        the mouse is bound to the canvas
        a label displays mouse position
        """
        wdw.title("mark with mouse")
        self.mag = 10  # magnification factor
        self.rows = r  # number of rows on canvas
        self.cols = c  # number of columns on canvas
        self.cnv = Canvas(wdw, width=self.mag * self.cols + 2 * self.mag,
                          height=self.mag * self.rows + 2 * self.mag,
                          bg='white')
        self.cnv.grid(row=1, column=0, columnspan=3)
        # to display mouse position :
        self.mouse_position = StringVar()
        self.mouse_position.set("put mouse inside box to draw")
        self.position_label = Label(wdw, textvariable=self.mouse_position)
        self.position_label.grid(row=2, column=0, columnspan=3)
        # bind mouse events
        self.bind_mouse_events()
        self.filled = []
        for _ in range(r):
            self.filled.append([False for _ in range(c)])

    def draw_rectangle(self, xpt, ypt):
        """
        Draws a green rectangle on canvas,
        with coordinates given at (xpt, ypt) by mouse.
        """
        xp0 = ypt - ypt % self.mag
        yp0 = xpt - xpt % self.mag
        xp1 = xp0 + self.mag
        yp1 = yp0 + self.mag
        i = xp0 // self.mag - 1
        j = yp0 // self.mag - 1
        name = '(' + str(i) + ',' + str(j) + ')'
        if not self.filled[i][j]:
            self.cnv.create_rectangle(yp0, xp0, yp1, xp1, \
                                      fill="green", tags=name)
            self.filled[i][j] = True
        else:
            self.cnv.delete(name)
            self.filled[i][j] = False

    def button_pressed(self, event):
        """
        Display coordinates of button press.
        """
        self.mouse_position.set("currently at [ " + \
                                str(event.x) + ", " + str(event.y) + " ]" + \
                                " release to fill, or drag")

    def button_released(self, event):
        """
        display coordinates of button release
        """
        self.mouse_position.set("drawn at [ " + \
                                str(event.x) + ", " + str(event.y) + " ]" + \
                                " redo to clear")
        self.draw_rectangle(event.x, event.y)

    def entered_window(self, event):
        """
        Display message that mouse entered window.
        """
        self.mouse_position.set("press mouse to give coordinates")

    def exited_window(self, event):
        """
        Display message that mouse exited window.
        """
        self.mouse_position.set("put mouse inside box to draw")

    def mouse_dragged(self, event):
        """
        Display coordinates of moving mouse.
        """
        self.mouse_position.set("dragging at [ " + \
                                str(event.x) + ", " + str(event.y) + " ]" + \
                                " release to draw")


def main():
    """
    Defines the dimensions and launches the GUI.
    """
    top = Tk()
    rows = 20
    columns = 30
    FillSquares(top, rows, columns)
    top.mainloop()


if __name__ == "__main__":
    main()
