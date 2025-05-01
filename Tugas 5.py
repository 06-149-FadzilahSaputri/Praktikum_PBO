#Fadzilah Saputri_123140149_PBORA

import tkinter as tk
from tkinter import messagebox
import json
import os

# Fungsi untuk menyimpan data user ke file JSON
def save_user_info(username, password):
    users = {}
    if os.path.exists("user_data.json"):
        with open("user_data.json", "r") as file:
            users = json.load(file)

    users[username] = password
    with open("user_data.json", "w") as file:
        json.dump(users, file)

# Fungsi untuk memverifikasi login
def verify_login(username, password):
    if not os.path.exists("user_data.json"):
        return False
    with open("user_data.json", "r") as file:
        users = json.load(file)
    return users.get(username) == password

# Fungsi untuk membuka halaman utama setelah login
def show_main_window():
    main_window = tk.Toplevel()
    main_window.title("Welcome!")
    main_window.geometry("300x200")
    main_window.configure(bg="#ecf0f1")

    tk.Label(main_window, text="🎉 Selamat datang!", font=("Arial", 16), bg="#ecf0f1", fg="#2c3e50").pack(pady=30)
    tk.Button(main_window, text="Keluar", bg="#e74c3c", fg="white", command=main_window.destroy).pack()

# Fungsi untuk proses register
def register_user():
    username = entry_reg_username.get()
    password = entry_reg_password.get()
    confirm = entry_confirm_password.get()

    if password != confirm:
        messagebox.showerror("Error", "Password dan konfirmasi tidak cocok!")
        return
    if not username or not password:
        messagebox.showwarning("Peringatan", "Semua field harus diisi!")
        return

    save_user_info(username, password)
    messagebox.showinfo("Sukses", "Registrasi berhasil!")
    register_frame.pack_forget()
    login_frame.pack()

# Fungsi untuk proses login
def login_user():
    username = entry_login_username.get()
    password = entry_login_password.get()

    if verify_login(username, password):
        messagebox.showinfo("Berhasil", f"Login berhasil. Selamat datang, {username}!")
        root.withdraw()
        show_main_window()
    else:
        messagebox.showerror("Gagal", "Username atau password salah!")

# GUI utama
root = tk.Tk()
root.title("Login & Register")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

# Frame login
login_frame = tk.Frame(root, bg="#dff9fb")
login_frame.pack(pady=20)

tk.Label(login_frame, text="Login", font=("Arial", 18), bg="#dff9fb", fg="#130f40").pack(pady=10)

entry_login_username = tk.Entry(login_frame, width=30, bg="#f6e58d")
entry_login_username.pack(pady=5)
entry_login_username.insert(0, "Username")

entry_login_password = tk.Entry(login_frame, width=30, bg="#f6e58d", show="*")
entry_login_password.pack(pady=5)
entry_login_password.insert(0, "Password")

tk.Button(login_frame, text="Login", bg="#7ed6df", fg="#2f3542", command=login_user).pack(pady=10)
tk.Button(login_frame, text="Belum punya akun? Daftar", command=lambda: [login_frame.pack_forget(), register_frame.pack()]).pack()

# Frame register
register_frame = tk.Frame(root, bg="#c7ecee")

tk.Label(register_frame, text="Register", font=("Arial", 18), bg="#c7ecee", fg="#2c3e50").pack(pady=10)

entry_reg_username = tk.Entry(register_frame, width=30, bg="#ffbe76")
entry_reg_username.pack(pady=5)
entry_reg_username.insert(0, "Username")

entry_reg_password = tk.Entry(register_frame, width=30, bg="#ffbe76", show="*")
entry_reg_password.pack(pady=5)
entry_reg_password.insert(0, "Password")

entry_confirm_password = tk.Entry(register_frame, width=30, bg="#ffbe76", show="*")
entry_confirm_password.pack(pady=5)
entry_confirm_password.insert(0, "Confirm Password")

tk.Button(register_frame, text="Register", bg="#badc58", fg="#130f40", command=register_user).pack(pady=10)
tk.Button(register_frame, text="Sudah punya akun? Login", command=lambda: [register_frame.pack_forget(), login_frame.pack()]).pack()

root.mainloop()
