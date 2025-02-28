import sqlite3
import tkinter as tk
from tkinter import messagebox
import userdashboard

def open_user_details(user_id, username):
    # 🎨 Tkinter Setup
    details_window = tk.Tk()
    details_window.title("User Details - Skillscope")
    details_window.geometry("400x550")
    details_window.configure(bg="#2C3E50")  # Dark background color

    # 📌 Connect to SQLite & Create Table if not exists
    conn = sqlite3.connect("SkillScope.db")
    cursor = conn.cursor()
    # cursor.execute("""
    #     CREATE TABLE IF NOT EXISTS user_details (
    #         detail_id INTEGER PRIMARY KEY AUTOINCREMENT,
    #         user_id INTEGER,
    #         skills TEXT NOT NULL,
    #         top_skill TEXT NOT NULL,
    #         college_name TEXT NOT NULL,
    #         degree TEXT NOT NULL,
    #         cgpa REAL NOT NULL,
    #         expected_salary INTEGER NOT NULL,
    #         city TEXT NOT NULL,
    #         FOREIGN KEY (user_id) REFERENCES users (user_id) ON DELETE CASCADE
    #     )
    # """)
    # conn.commit()
    # conn.close()

    # 📌 Function to Save User Details
    def save_details():
        skills = entry_skills.get().strip()
        top_skill = entry_top_skill.get().strip()
        college_name = entry_college.get().strip()
        degree = entry_degree.get().strip()
        cgpa = entry_cgpa.get().strip()
        expected_salary = entry_salary.get().strip()
        city = entry_city.get().strip()

        if not (skills and top_skill and college_name and degree and cgpa and expected_salary and city):
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            conn = sqlite3.connect("SkillScope.db")
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO user_details (user_id, skills, top_skill, college_name, degree, cgpa, expected_salary, city) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (user_id, skills, top_skill, college_name, degree, float(cgpa), int(expected_salary), city))
            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "User details saved successfully!")
            details_window.destroy()
            userdashboard.user_dashboard(user_id)


        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error: {e}")

    # 🎨 UI Elements
    tk.Label(details_window, text=f"Welcome, {username}!", font=("Arial", 14, "bold"), fg="white", bg="#2C3E50").pack(pady=10)

    frame = tk.Frame(details_window, bg="#34495E", padx=20, pady=20)
    frame.pack(pady=10)

    def create_entry(label_text):
        tk.Label(frame, text=label_text, font=("Arial", 10, "bold"), fg="white", bg="#34495E").pack(anchor="w", pady=3)
        entry = tk.Entry(frame, width=30, font=("Arial", 10), bg="#ECF0F1", relief="flat")
        entry.pack(pady=2)
        return entry

    entry_skills = create_entry("Skills (comma-separated)")
    entry_top_skill = create_entry("Top Skill")
    entry_college = create_entry("College Name")
    entry_degree = create_entry("Degree")
    entry_cgpa = create_entry("CGPA")
    entry_salary = create_entry("Expected Salary")
    entry_city = create_entry("City")

    # Styled Button with Hover Effect
    def on_enter(e):
        e.widget.config(bg="#2980B9")

    def on_leave(e):
        e.widget.config(bg="#3498DB")

    save_btn = tk.Button(details_window, text="Save Details", font=("Arial", 12, "bold"),
                         bg="#3498DB", fg="white", relief="flat", width=25, command=save_details)
    save_btn.pack(pady=10)
    save_btn.bind("<Enter>", on_enter)
    save_btn.bind("<Leave>", on_leave)

    details_window.mainloop()
# open_user_details(1,'a')
