import random
import string
import tkinter as tk
from tkinter import ttk


def Pix(scalar):
    return scalar * 16

def RandomColor():
    return '#' + ''.join(random.choice(string.digits) for _ in range(6))

class MainPane:
    def __init__(self, listener, frame):
        self.l = listener
        self.f = frame
        self.f['width'] = Pix(80)
        self.f['height'] = Pix(80)
        self.f['bg'] = RandomColor()

        tpbr = tk.Frame(self.f)
        tpbr.grid_propagate(False)
        tpbr.grid(row=0, column=0)
        self.topbar = Topbar(self.l, tpbr)

        cntl = tk.Frame(self.f, width=Pix(80), height=Pix(72))
        cntl.grid_propagate(False)
        cntl.grid(row=1, column=0)
        self.control = ControlPane(self.l, cntl)

class MirrorPane:
    def __init__(self, listener, frame):
        self.l = listener
        self.f = frame
        self.f['width'] = Pix(40)
        self.f['height'] = Pix(80)
        self.f['bg'] = RandomColor()

class Topbar:
    def __init__(self, listener, frame):
        self.l = listener
        self.f = frame
        self.f['width'] = Pix(80)
        self.f['height'] = Pix(4)
        self.f['bg'] = RandomColor()

        self.devices = ttk.Combobox(self.f, state='readonly', values=['Samsung S10', 'Windows', 'iPhone14'])
        self.devices['height'] = Pix(4)
        self.devices.grid_propagate(False)
        self.devices.grid(row=0, column=0)

class ControlPane:
    def __init__(self, listener, frame):
        self.l = listener
        self.f = frame
        self.f['width'] = Pix(80)
        self.f['height'] = Pix(76)
        self.f['bg'] = RandomColor()

        actn = tk.Frame(self.f)
        actn.grid_propagate(False)
        actn.grid(row=0, column=0)
        self.action = ActionPane(self.l, actn)

        bord = tk.Frame(self.f)
        bord.grid_propagate(False)
        bord.grid(row=0, column=1)
        self.board = BoardPane(self.l, bord)

class ActionPane:
    def __init__(self, listener, frame):
        self.l = listener
        self.f = frame
        self.f.grid_rowconfigure(0, weight=1)
        self.f.grid_columnconfigure(0, weight=1)
        self.f['width'] = Pix(40)
        self.f['height'] = Pix(76)
        self.f['bg'] = RandomColor()

        self.canvas = tk.Canvas(self.f, bg=RandomColor())
        self.canvas.grid(row=0, column=0, sticky='news')
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        self.scrollbar = tk.Scrollbar(self.f, orient="vertical", command=self.canvas.yview)
        self.scrollbar.grid(row=0, column=1, sticky='ns')
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.action_list = tk.Frame(self.canvas, bg=RandomColor())
        self.canvas.create_window((0, 0), window=self.action_list, anchor='nw')

        self.Test()

    def Test(self):
        rows = 80
        for i in range(rows):
            action = ActionItem(self.l, tk.Frame(self.action_list))
            self.Add(action)

    def Update(self, actions):
        for i, a in enumerate(actions):
            a.grid(row=i, column=0, sticky='news')
        self.actions = actions
        self.action_list.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def Add(self, action):
        if not hasattr(self, 'actions'):
            self.actions = []

        action.f.grid(row=len(self.actions), column=0, sticky='news')
        self.actions.append(action)
        self.action_list.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

class ActionItem:
    def __init__(self, listener, frame):
        self.l = listener
        self.f = frame
        self.f['width'] = Pix(40)
        self.f['height'] = Pix(6)
        self.f['bg'] = RandomColor()

class BoardPane:
    def __init__(self, listener, frame):
        self.l = listener
        self.f = frame
        self.f['width'] = Pix(40)
        self.f['height'] = Pix(76)
        self.f['bg'] = RandomColor()

        oprt = tk.Frame(self.f)
        oprt.grid_propagate(False)
        oprt.grid(row=0, column=0)
        self.operation = OperationPane(self.l, oprt)

        elem = tk.Frame(self.f)
        elem.grid_propagate(False)
        elem.grid(row=1, column=0)
        self.element = ElementPane(self.l, elem)

class OperationPane:
    def __init__(self, listener, frame):
        self.l = listener
        self.f = frame
        self.f['width'] = Pix(40)
        self.f['height'] = Pix(38)
        self.f['bg'] = RandomColor()

class ElementPane:
    def __init__(self, listener, frame):
        self.l = listener
        self.f = frame
        self.f['width'] = Pix(40)
        self.f['height'] = Pix(38)
        self.f['bg'] = RandomColor()

class Listener:
    def __init__(self, app):
        self.app = app

class Application:
    def __init__(self):
        self.f = tk.Tk()
        self.f.title("Taps To Case")
        self.f.maxsize(Pix(120), Pix(80))
        self.f.resizable(False, False)
        self.l = Listener(self)

        main = tk.Frame(self.f)
        main.grid_propagate(False)
        main.grid(row=0, column=0)
        self.main = MainPane(self.l, main)

        mirr = tk.Frame(self.f)
        main.grid_propagate(False)
        mirr.grid(row=0, column=1)
        self.mirror = MirrorPane(self.l, mirr)

    def Run(self):
        self.f.mainloop()

if __name__ == '__main__':
    app = Application()
    app.Run()
