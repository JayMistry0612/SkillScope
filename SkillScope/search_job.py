import tkinter as tk
from tkinter import ttk
import sqlite3
import userdashboard
def search_JOB(userId):
    conn = sqlite3.connect('SkillScope.db')
    cursor = conn.cursor()

    cursor.execute("SELECT DISTINCT location FROM jobs")
    locations = [row[0] for row in cursor.fetchall()]
    locations.insert(0, "All")

    def search_jobs():
        selected_location = location_var.get()
        skill_query = skill_entry.get().strip()

        query = "SELECT job_id, job_position, skills_required, salary, location FROM jobs WHERE 1=1"
        params = []

        if selected_location != "All":
            query += " AND location = ?"
            params.append(selected_location)

        if skill_query:
            query += " AND skills_required LIKE ?"
            params.append(f"%{skill_query}%")

        cursor.execute(query, params)
        filtered_jobs = cursor.fetchall()

        for row in job_tree.get_children():
            job_tree.delete(row)

        for job in filtered_jobs:
            job_tree.insert("", tk.END, values=job)

    def go_back():
        search_window.destroy()
        userdashboard.user_dashboard(userId)
        

    search_window = tk.Tk()
    search_window.title("Search Jobs")
    search_window.geometry("800x500")

    filter_frame = tk.Frame(search_window)
    filter_frame.pack(pady=10)

    tk.Label(filter_frame, text="Location:").grid(row=0, column=0, padx=10)
    location_var = tk.StringVar(value="All")
    location_dropdown = ttk.Combobox(filter_frame, textvariable=location_var, values=locations, state="readonly")
    location_dropdown.grid(row=0, column=1, padx=10)

    tk.Label(filter_frame, text="Skill:").grid(row=0, column=2, padx=10)
    skill_entry = tk.Entry(filter_frame)
    skill_entry.grid(row=0, column=3, padx=10)

    search_btn = tk.Button(filter_frame, text="Search", command=search_jobs)
    search_btn.grid(row=0, column=4, padx=10)

    back_btn = tk.Button(search_window, text="Back", command=go_back)
    back_btn.pack(pady=10)

    columns = ("Job ID", "Job Title", "Skills Required", "Salary", "Location")
    job_tree = ttk.Treeview(search_window, columns=columns, show='headings')

    for col in columns:
        job_tree.heading(col, text=col)
        job_tree.column(col, width=150 if col != "Skills Required" else 250)

    job_tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    search_window.mainloop()
    conn.close()

# search_JOB(2)
