import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def show_plot(df , plotx , ploty , kind ='bar' , title = 'DataFrame Plot' ,labelx ='X Axis' ,lebely= 'Y Axis' ):
    if kind =='pie' :
       
        fig, ax = plt.subplots()
        plt.figure(figsize=(20, 20))
        
        df.set_index(labelx)[ploty].plot(kind='pie', autopct='%1.1f%%', startangle=140)
        plt.title(title)
        window_plot = tk.Tk()
        window_plot.title('نمودار دیتافریم')
        plt.tight_layout()
        canvas = FigureCanvasTkAgg(fig, master=window_plot)
        canvas.draw()
        canvas.get_tk_widget().pack()
        return
    

    window_plot = tk.Tk()
    window_plot.geometry("800x600")
    window_plot.title('نمودار دیتافریم')
 
    # رسم نمودار بر روی دیتافریم
    fig, ax = plt.subplots(figsize=(70, 70))
   
   # plt.figure(figsize=(70, 30))
    df.plot(kind = kind , x = plotx , y= ploty ,ax=ax)
    ax.set_title('DataFrame Plot')
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')

  # تبدیل نمودار matplotlib به یک ویجت Tkinter
    canvas = FigureCanvasTkAgg(fig, master=window_plot)
    canvas.draw()
    canvas.get_tk_widget().pack()
