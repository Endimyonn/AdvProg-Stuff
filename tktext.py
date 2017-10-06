import Tkinter
root = Tkinter.Tk()
root.tile = ("Thingy")
text = Tkinter.Text(root, height=5, width=20)
text.insert(Tkinter.END, "10 is 5+5")
text.pack()
root.mainloop()