import sqlite3
import tkinter as tk
from tkinter import messagebox

def open_recruiter_details(user_id, username):
    # 🎨 Tkinter Setup
    recruiter_window = tk.Tk()
    recruiter_window.title("Recruiter Details - Skillscope")
    recruiter_window.geometry("400x450")
    recruiter_window.configure(bg="#2C3E50")  # Dark background color

    # 📌 Connect to SQLite & Create Table if not exists
    conn = sqlite3.connect("SkillScope.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS recruiters_details (
            recruiter_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            company_name TEXT NOT NULL,
            position TEXT NOT NULL,
            location TEXT NOT NULL,
            company_email TEXT NOT NULL UNIQUE,
            FOREIGN KEY (user_id) REFERENCES users (user_id) ON DELETE CASCADE
        )
    """)
    conn.commit()
    conn.close()

    # 📌 Function to Save Recruiter Details
    def save_recruiter_details():
        company_name = entry_company.get().strip()
        position = entry_position.get().strip()
        location = entry_location.get().strip()
        company_email = entry_email.get().strip()

        if not (company_name and position and location and company_email):
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            conn = sqlite3.connect("SkillScope.db")
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO recruiters_details (user_id, company_name, position, location, company_email) 
                VALUES (?, ?, ?, ?, ?)
            """, (user_id, company_name, position, location, company_email))
            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Recruiter details saved successfully!")
            recruiter_window.destroy()

        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Company email already exists!")

    # 🎨 UI Elements
    tk.Label(recruiter_window, text=f"Welcome, {username}!", font=("Arial", 14, "bold"), fg="white", bg="#2C3E50").pack(pady=10)

    frame = tk.Frame(recruiter_window, bg="#34495E", padx=20, pady=20)
    frame.pack(pady=10)

    def create_entry(label_text):
        tk.Label(frame, text=label_text, font=("Arial", 10, "bold"), fg="white", bg="#34495E").pack(anchor="w", pady=3)
        entry = tk.Entry(frame, width=30, font=("Arial", 10), bg="#ECF0F1", relief="flat")
        entry.pack(pady=2)
        return entry

    entry_company = create_entry("Company Name")
    entry_position = create_entry("Position")
    entry_location = create_entry("Location")
    entry_email = create_entry("Company Email")

    # Styled Button with Hover Effect
    def on_enter(e):
        e.widget.config(bg="#2980B9")

    def on_leave(e):
        e.widget.config(bg="#3498DB")

    save_btn = tk.Button(recruiter_window, text="Save Details", font=("Arial", 12, "bold"),
                         bg="#3498DB", fg="white", relief="flat", width=25, command=save_recruiter_details)
    save_btn.pack(pady=10)
    save_btn.bind("<Enter>", on_enter)
    save_btn.bind("<Leave>", on_leave)

    recruiter_window.mainloop()
# open_recruiter_details(1,'a')
