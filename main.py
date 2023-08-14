import tkinter as tk
from tkinter import messagebox

def tmbah():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Amaran", "Please enter a task.")

def delete():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        task_list.delete(selected_task_index)
    else:
        messagebox.showwarning("Amaran", "Sila pilih tugasan untuk dipadamkan.")

def clr():
    task_list.delete(0, tk.END)

def addbtnhover(e):
    add_button.config(bg="#45B39D")

def lepasaddbtn(e):
    add_button.config(bg="#4CAF50")

def deletebtnhover(e):
    delete_button.config(bg="#D94335")

def lepasdeletebtn(e):
    delete_button.config(bg="#FF5733")

def clrbtnhver(e):
    clear_button.config(bg="#E8A613")

def lepasclrbtn(e):
    clear_button.config(bg="#FFC300")

def closefunction():
    unfinished_tasks = task_list.size()
    if unfinished_tasks > 0:
        msg = "Anda masih mempunyai {} tugasan yang belum selesai. Sila selesaikan semua tugasan sebelum menutup.".format(unfinished_tasks)
        messagebox.showwarning("Tugas yang Belum Selesai", msg)
    else:
        confirm = messagebox.askyesno("Tutup Aplikasi", "Adakah anda pasti mahu menutup aplikasi?")
        if confirm:
            root.destroy()

root = tk.Tk()
root.title("Senarai yang hendak dibuat")
root.protocol("WM_DELETE_WINDOW", closefunction)

root.configure(bg="#EFEFEF")

task_entry = tk.Entry(root, width=40, font=("Helvetica", 12))
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Tambah Tugasan", command=tmbah, bg="#4CAF50", fg="black", font=("Helvetica", 10, "bold"))
add_button.pack()
add_button.bind("<Enter>", addbtnhover)
add_button.bind("<Leave>", lepasaddbtn)

delete_button = tk.Button(root, text="Padam Tugasan", command=delete, bg="#FF5733", fg="black", font=("Helvetica", 10, "bold"))
delete_button.pack()
delete_button.bind("<Enter>", deletebtnhover)
delete_button.bind("<Leave>", lepasdeletebtn)

clear_button = tk.Button(root, text="Kosongkan Semua Tugasan", command=clr, bg="#FFC300", fg="black", font=("Helvetica", 10, "bold"))
clear_button.pack()
clear_button.bind("<Enter>", clrbtnhver)
clear_button.bind("<Leave>", lepasclrbtn)

task_list = tk.Listbox(root, width=40, height=10, font=("Helvetica", 12))
task_list.pack()

root.mainloop()