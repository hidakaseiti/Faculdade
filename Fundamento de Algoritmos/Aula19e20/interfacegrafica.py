from tkinter import * #não é preciso decorar por agora mas o site é https://docs.python.org/3/library/tkinter.html
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
ttk.Checkbutton(frm, text='Almoçou hoje?').grid(column=0, row=2)
ttk.Entry(frm).grid(column=0, row=3)
root.mainloop()