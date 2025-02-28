import re
import sqlite3
import tkinter as tk
from tkinter import messagebox
from user_details import open_user_details
from login import Login
from recruiters_details import open_recruiter_details
import Setup_database

# 📌 Function to open the Login Page
def Signup(usertype):
    def open_login_page():
        root.destroy()  # Close the current Sign-up page
        Login(usertype)  # Open the Login page

    # 📌 Connect to SQLite Database
    def connect_db():
        conn = sqlite3.connect("SkillScope.db")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                phone_no TEXT NOT NULL UNIQUE,
                type TEXT NOT NULL
            )
        """)
        conn.commit()
        return conn

    # 📧 Email Validation
    def is_valid_email(email):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(pattern, email)

    # 🔑 Password Validation
    def is_valid_password(password):
        return len(password) >= 8 and not password.islower() and not password.isupper()

    # 🎯 Register User
    def register_user():
        username = entry_username.get().strip()
        password = entry_password.get().strip()
        email = entry_email.get().strip()
        phone_no = entry_phone.get().strip()

        if not username or not password or not email or not phone_no or not usertype:
            messagebox.showerror("Error", "All fields are required!")
            return

        if not is_valid_email(email):
            messagebox.showerror("Error", "Invalid email format!")
            return

        if not is_valid_password(password):
            messagebox.showerror("Error", "Password must have at least 8 characters with uppercase & lowercase letters.")
            return

        if not phone_no.isdigit() or len(phone_no) > 15:
            messagebox.showerror("Error", "Invalid phone number!")
            return

        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password, email, phone_no, type) VALUES (?, ?, ?, ?, ?)", 
                        (username, password, email, phone_no, usertype))
            conn.commit()

            # Fetch the User ID of the newly registered user
            cursor.execute("SELECT user_id FROM users WHERE username = ?", (username,))
            user_id = cursor.fetchone()[0]

            conn.close()

            messagebox.showinfo("Success", f"{usertype} registered successfully!")
            root.destroy()  # Close registration window

            if usertype == 'user':
                open_user_details(user_id, username)  # Open user details page
            else:
                open_recruiter_details(user_id, username)  # Open recruiter details page

        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username, Email, or Phone number already exists!")

    # 🎨 Tkinter Registration Page with Enhanced UI
    root = tk.Tk()
    root.title("Signup - Skillscope")
    root.geometry("400x450")
    root.configure(bg="#2C3E50")  # Dark background color

    tk.Label(root, text="Signup", font=("Arial", 18, "bold"), fg="white", bg="#2C3E50").pack(pady=10)

    frame = tk.Frame(root, bg="#34495E", padx=20, pady=20)
    frame.pack(pady=10)

    def create_entry(label_text):
        tk.Label(frame, text=label_text, font=("Arial", 10, "bold"), fg="white", bg="#34495E").pack(anchor="w", pady=3)
        entry = tk.Entry(frame, width=30, font=("Arial", 10), bg="#ECF0F1", relief="flat")
        entry.pack(pady=2)
        return entry

    entry_username = create_entry("Username")
    entry_password = create_entry("Password")
    entry_password.config(show="*")  # Password masking
    entry_email = create_entry("Email")
    entry_phone = create_entry("Phone No")

    # Styled Button
    def on_enter(e):
        e.widget.config(bg="#2980B9")

    def on_leave(e):
        e.widget.config(bg="#3498DB")

    register_btn = tk.Button(root, text=f"Register as {usertype}", font=("Arial", 12, "bold"),
                             bg="#3498DB", fg="white", relief="flat", width=25, command=register_user)
    register_btn.pack(pady=10)
    register_btn.bind("<Enter>", on_enter)
    register_btn.bind("<Leave>", on_leave)

    login_btn = tk.Button(root, text="Already Have an Account?", font=("Arial", 10, "bold"),
                          bg="#95A5A6", fg="white", relief="flat", width=25, command=open_login_page)
    login_btn.pack(pady=5)

    root.mainloop()
