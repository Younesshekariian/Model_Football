import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt  
from ShowPlot import show_plot  
def showPlot():
    show_plot()
def display_frame(df , tile = 'view Data'  , Func_plot= False , kind = None, plotx = None , ploty = None  ,lblx = None , lbly =None
                  ):
    new_window = tk.Toplevel()
    new_window.title(tile)
    
    frame = tk.Frame(new_window)
    frame.pack(fill="both", expand=True)
    
 
    treeview = ttk.Treeview(frame , columns=df.columns , show= "headings")
    treeview["column"] = list(df.columns)
    treeview["show"] = "headings"
    
    for col in df.columns:
        treeview.heading(col ,text = col)
    for index , row in df.iterrows() :
        treeview.insert("" , "end" ,values=row.tolist() )
    treeview.pack(fill="both", expand=True)

    frame_plot = tk.Frame(new_window)
    frame_plot.pack()
    def Func_plot_show():
        show_plot(df, plotx=plotx, ploty = ploty, kind = kind )  
    if Func_plot:
        btn_plot = tk.Button(frame_plot , text="Show Plot" ,command= Func_plot_show )
        btn_plot.pack()

def search_team(df,team_name, tree):

    
    #ورودی تکست باکس تیم و یک تری ویو و دیتا فریم         
     
    
    if not team_name:
        messagebox.showerror("خطا", "لطفاً نام تیم را وارد کنید.")
        return
    
    # عمل جست وجو       
    result = df[df['team'].str.contains(team_name, case=False)]
    
    for row in tree.get_children():
        tree.delete(row)
    
    if result.empty:
        messagebox.showinfo("نتیجه", "هیچ تیمی با این نام یافت نشد.")
    else:
        for index, row in result.iterrows():
            tree.insert("", "end", values=(row['team'], row['score']))
            
def display_dataframe_small(df, treeview):
    treeview.delete(*treeview.get_children())  
    # پاک کردن تمام ردیف‌های موجود در Treeview     
    
    treeview["column"] = list(df.columns)
    treeview["show"] = "headings"
    
    for column in treeview["columns"]:
        treeview.heading(column, text=column)
    
    for index, row in df.iterrows():
        treeview.insert("", "end", values=list(row))