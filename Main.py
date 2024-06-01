import tkinter as tk
from tkinter import ttk
import pandas as pd
from tkinter import filedialog , messagebox
from dataframe_app import display_frame ,search_team , display_dataframe_small
from ShowPlot import show_plot
global_data = pd.DataFrame()

team_name = ''
name_file = ''

def save_file():
    path  = filedialog.asksaveasfilename(defaultextension =".csv" , filetypes = [("CSV File" , "*.csv")])
    return path

    
def get_team_name():
    global team_name
    team_name = name_team_enty.get()
    
def get_name_file():
    global name_file 
    name_file = name_file_enty.get()
    return name_file
def read_csv_file(types = 'read'):
    global file_path
    if types == 'write':
        file_path = file_path = filedialog.askdirectory()
        if file_path:
         print(file_path)
        return file_path
    global global_data
    path = filedialog.askopenfilename(filetypes = [("CSV files" , "*.csv")])
    if path:
        try:
            global_data = pd.read_csv(path)
            print("Data Frame:")
            print(global_data)
        except FileNotFoundError:
            messagebox.showinfo("Error", "File not found.")
def save_excel(data , name_file='defult') :
   
     try:  
      path_file= save_file()
      print(path_file)
      data.to_csv(path_file, index=False)
      messagebox.showinfo( "Info" , "File Saved" )
     except Exception:
      messagebox.showinfo("Not Saved" , "Error") 
      
def name_team( df,name , best = False , count = 10):
    goals = df[df['team'] == name].groupby('scorer').size().reset_index(name = 'count_goals')
    sort_goals = goals.sort_values(by = 'count_goals' , ascending =False)
    if best:
     return sort_goals.head(1)
    else:
     return sort_goals.head(count)
def winner_team():
    goal_count = global_data.groupby('team').size().reset_index(name ='win')
    sort_goal_team=goal_count.sort_values(by ='win' , ascending = False)
    res = sort_goal_team.head(20) 
    return res
            
def Action1():
    get_team_name()
    data_new = name_team(global_data, team_name)
    display_frame(data_new , tile='گلزنان تیم ' , Func_plot=True  ,kind = 'bar' ,plotx='scorer' , ploty='count_goals' )    
def Action2():
    display_frame(global_data, 'نمایش دیتا فریم')  
def Action3():
      get_team_name()
      res_Ac = winner_team()
      display_dataframe_small(res_Ac, treeview)  
def Action4():
    res_Ac = winner_team()
    get_name_file()
    save_excel(res_Ac , name_file)
def Action5():
    res_Ac = winner_team()
    show_plot(res_Ac, 'team', 'win',kind= 'bar')
   
    # GUI
root  = tk.Tk()
root.title('Analyze Football')

main_frame = tk.Frame(root , padx= 20 ,pady=20)
main_frame.pack()

label_name_team = tk.Label(main_frame , text = "تیم ملی")
label_name_team.grid(row=0, column=0, padx=5, pady=5)

team = tk.StringVar()
name_team_enty = tk.Entry(main_frame , textvariable= team)
name_team_enty.grid(row=0, column=1, padx=5, pady=50 )

btn_name_team = tk.Button(main_frame, text="باز کردن دیتاست فوتبال", command=read_csv_file)
btn_name_team.grid(row=1, columnspan=2, padx=5, pady=5)

frame_btn = tk.Frame(root , padx= 20 ,pady=20)
frame_btn.pack()

btn_name_team1 = tk.Button(frame_btn, text="امار گل", command=Action1)
btn_name_team1.grid(row= 0 , column= 0  ,padx=(10,5) , pady=5)

btn_name_team2 = tk.Button(frame_btn, text="نمایش دیتا فریم ", command=Action2)
btn_name_team2.grid( row= 0 , column= 1 , padx=(10,5) , pady=5 )

btn_name_team3 = tk.Button(frame_btn, text="آمار برد", command=Action3)
btn_name_team3.grid( row= 0 , column= 2 , padx=(10,5) , pady=5 )

frame_tree = tk.Frame(root)
frame_tree.pack()

#tree viwe
treeview = ttk.Treeview(frame_tree)
treeview.pack(padx=10, pady=10)
treeview["columns"] = ("Team Name", "Wins")
treeview["show"] = "headings"
    
treeview.heading("Team Name", text="نام تیم")
treeview.heading("Wins", text="تعداد برد")

frame_tree_combo = tk.Frame(frame_tree)
frame_tree_combo.pack()

btn_save = tk.Button(frame_tree_combo , text = 'ذخیره' ,command = Action4) 
btn_save.grid( row= 1 , column= 2 , padx=(10,5) , pady=5 )

btn_show = tk.Button(frame_tree_combo   , text = 'نمایش نمودار' ,command = Action5) 
btn_show.grid( row= 1 , column= 1 , padx=(10,5) , pady=5 )

# name_file = tk.StringVar()
# name_file_enty = tk.Entry(frame_tree_combo , textvariable= name_file)
# name_file_enty.grid(row=1, column=3, padx=5, pady=5 )

# label_name_file = tk.Label(frame_tree_combo,text = 'name file')
# label_name_file.grid(row=1, column=4, padx=5, pady=5 )

root.mainloop()