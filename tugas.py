import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.style = ttk.Style(theme='solar')
        
        self.frame = ttk.Frame(self.root, padding=20)
        self.frame.pack(fill=BOTH, expand=True)
        
        self.title_label = ttk.Label(self.frame, text="To-Do List", font=("Helvetica", 18))
        self.title_label.pack(pady=10)
        
        self.task_entry = ttk.Entry(self.frame, width=50)
        self.task_entry.pack(pady=10)
        
        self.add_button = ttk.Button(self.frame, text="Add Task", bootstyle=SUCCESS, command=self.add_task)
        self.add_button.pack(pady=10)
        
        self.task_listbox = tk.Listbox(self.frame, height=10, width=50)
        self.task_listbox.pack(pady=10)
        
        self.remove_button = ttk.Button(self.frame, text="Remove Selected", bootstyle=DANGER, command=self.remove_task)
        self.remove_button.pack(pady=10)
        
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(END, task)
            self.task_entry.delete(0, END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")
            
    def remove_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to remove.")

if __name__ == "__main__":
    root = ttk.Window(themename="solar")
    app = ToDoApp(root)
    root.mainloop()
