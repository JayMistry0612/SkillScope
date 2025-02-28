import sqlite3
import tkinter as tk
from tkinter import messagebox
import signup_gui
import recruiter_dashboard
import userdashboard

def Login(usertype):
    # 📌 Connect to SQLite Database
    def connect_db():
        return sqlite3.connect("SkillScope.db")

    # 📌 Open Signup Page
    def signup_page():
        login_window.destroy()
        signup_gui.Signup(usertype)

    # 🔑 Login Function
    def login_user():
        username = entry_username.get().strip()
        password = entry_password.get().strip()

        if not username or not password:
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = ? AND password = ? AND type = ?", 
                           (username, password, usertype))
            user = cursor.fetchone()
            print(user)
            user_id=user[0]


            if user:
                if usertype=='recruiter':
                    messagebox.showinfo("Success", "Login Successful!")
                    cursor.execute("SELECT recruiter_id,company_name FROM recruiters_details WHERE user_id = ?",(user_id,))
                    recrutier_data=cursor.fetchone()
                    print(recrutier_data,'reder')
                    recruitier_id=recrutier_data[0]
                    recruitier_compnay_name=recrutier_data[1]
                    login_window.destroy()
                    recruiter_dashboard.recruiter_dashboard(recruitier_id,recruitier_compnay_name)
                    conn.close()
                else:
                    login_window.destroy()
                    userdashboard.user_dashboard(user_id)
            else:
                messagebox.showerror("Error", "User not registered or incorrect password!")

        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error: {e}")

    # 🎨 Tkinter Login Page with Enhanced UI
    login_window = tk.Tk()
    login_window.title("Login - Skillscope")
    login_window.geometry("350x300")
    login_window.configure(bg="#2C3E50")  # Dark background color

    tk.Label(login_window, text="Login", font=("Arial", 18, "bold"), fg="white", bg="#2C3E50").pack(pady=10)

    frame = tk.Frame(login_window, bg="#34495E", padx=20, pady=20)
    frame.pack(pady=10)

    def create_entry(label_text):
        tk.Label(frame, text=label_text, font=("Arial", 10, "bold"), fg="white", bg="#34495E").pack(anchor="w", pady=3)
        entry = tk.Entry(frame, width=30, font=("Arial", 10), bg="#ECF0F1", relief="flat")
        entry.pack(pady=2)
        return entry

    entry_username = create_entry("Username")
    entry_password = create_entry("Password")
    entry_password.config(show="*")  # Hide password input

    # Styled Button
    def on_enter(e):
        e.widget.config(bg="#2980B9")

    def on_leave(e):
        e.widget.config(bg="#3498DB")

    login_btn = tk.Button(login_window, text="Login", font=("Arial", 12, "bold"),
                          bg="#3498DB", fg="white", relief="flat", width=25, command=login_user)
    login_btn.pack(pady=10)
    login_btn.bind("<Enter>", on_enter)
    login_btn.bind("<Leave>", on_leave)

    signup_btn = tk.Button(login_window, text="Don't have an Account?", font=("Arial", 10, "bold"),
                           bg="#95A5A6", fg="white", relief="flat", width=25, command=signup_page)
    signup_btn.pack(pady=5)

    login_window.mainloop()
# Login(73)
