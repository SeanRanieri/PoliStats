from tkinter import *
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)
data = pd.read_csv('data.csv')
data.head()

# Some of this code was taken from this video: https://www.youtube.com/watch?v=0WafQCaok6g


# To show sample scatterplot, uncomment this block of code
# xcol = 'Alabama_CountyPopulation'
# ycol = 'Alabama_dem'
# data[xcol] = data[xcol].astype(str)
# fig, ax = plt.subplots()
# ax.scatter(data[xcol], data[ycol], marker = '.')
# ax.set_xlabel('County Population')
# ax.set_ylabel('% Democratic Votes')
# plt.show()

root = Tk()
root.title('PoliStats')
root.geometry('800x600')

title = Label(root, font=('Ariel', 24), text='Most Important Factors')
title.pack()

mainframe = Frame(root)
mainframe.pack(fill=BOTH, expand=1)

canvas = Canvas(mainframe)
canvas.pack(side=LEFT, fill=BOTH, expand=1)

scrollbar = ttk.Scrollbar(mainframe, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

secondary_frame = Frame(canvas)

canvas.create_window((0, 0), window=secondary_frame, anchor='nw')

factors = ['\r\rHousehold Income\r\r', '\r\rPoverty Rate\r\r', '\r\rPopulation\r\r', '\r\rVoter Turnout\r\r',
           '\r\rMedian Age\r\r', '\r\rWhite Percentage\r\r', '\r\rBlack Percentage\r\r', '\r\rAsian Percentage\r\r',
           '\r\rHispanic Percentage\r\r', '\r\rCrime Rate\r\r', '\r\rHigh School Diploma Rate\r\r',
           '\r\rBachelor\'s Degree Rate\r\r', '\r\rMaster\'s Degree Rate\r\r', '\r\rPopulation Growth Rate\r\r',
           '\r\rPopulation Density\r\r']

for factor in factors:
    Button(secondary_frame, text=factor).pack()

root.mainloop()