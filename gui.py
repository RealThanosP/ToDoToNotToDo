import tkinter as tk
from tkinter import ttk
import sys

class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x500")

        self.frame = tk.Frame(self.root)
        self.frame.pack()

        



if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

