import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk
import Setup_database


# def setup_database():
#     conn = sqlite3.connect("SkillScope.db")
#     cursor = conn.cursor()
    
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS recruiters_details (
#             recruiter_id INTEGER PRIMARY KEY AUTOINCREMENT,
#             user_id INTEGER,
#             company_name TEXT NOT NULL,
#             position TEXT NOT NULL,
#             location TEXT NOT NULL,
#             company_email TEXT NOT NULL UNIQUE,
#             FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
#         )
#     ''')
    
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS jobs (
#             job_id INTEGER PRIMARY KEY AUTOINCREMENT,
#             recruiter_id INTEGER,
#             job_position TEXT NOT NULL,
#             location TEXT NOT NULL,
#             job_type TEXT NOT NULL,
#             salary INTEGER NOT NULL,
#             skills_required TEXT NOT NULL,
#             total_positions INTEGER NOT NULL,
#             FOREIGN KEY (recruiter_id) REFERENCES recruiters_details(recruiter_id) ON DELETE CASCADE
#         )
#     ''')
    
#     conn.commit()
#     conn.close()



# to post the jib
def post_job(recruiter_id):
    def save_job():
        job_position = entry_position.get().strip()
        location = entry_location.get().strip()
        job_type = combo_type.get()
        salary = entry_salary.get().strip()
        skills = entry_skills.get().strip()
        total_positions = entry_total.get().strip()

        if not (job_position and location and job_type and salary and skills and total_positions):
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            conn = sqlite3.connect("SkillScope.db")
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO jobs (recruiter_id, job_position, location, job_type, salary, skills_required, total_positions)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (recruiter_id, job_position, location, job_type, int(salary), skills, int(total_positions)))
            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Job posted successfully!")
            job_frame.destroy()
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error: {e}")

    job_frame = tk.Toplevel()
    job_frame.title("Post a Job")
    job_frame.geometry("400x500")

    tk.Label(job_frame, text="Post a Job", font=("Arial", 14, "bold")).pack(pady=10)
    
    tk.Label(job_frame, text="Job Position").pack()
    entry_position = tk.Entry(job_frame)
    entry_position.pack()
    
    tk.Label(job_frame, text="Location").pack()
    entry_location = tk.Entry(job_frame)
    entry_location.pack()
    
    tk.Label(job_frame, text="Job Type").pack()
    combo_type = ttk.Combobox(job_frame, values=["Remote", "Hybrid", "On-site"])
    combo_type.pack()
    
    tk.Label(job_frame, text="Salary").pack()
    entry_salary = tk.Entry(job_frame)
    entry_salary.pack()
    
    tk.Label(job_frame, text="Skills Required").pack()
    entry_skills = tk.Entry(job_frame)
    entry_skills.pack()
    
    tk.Label(job_frame, text="Total Positions").pack()
    entry_total = tk.Entry(job_frame)
    entry_total.pack()
    
    tk.Button(job_frame, text="Post Job", command=save_job).pack(pady=20)



# to edit the jobs
def edit_job(job_id, recruiter_id, parent_window):
    """ Function to edit a specific job listing """
    def update_job():
        new_position = entry_position.get().strip()
        new_location = entry_location.get().strip()
        new_type = combo_job_type.get().strip()
        new_salary = entry_salary.get().strip()
        new_skills = entry_skills.get().strip()
        new_total_positions = entry_total_positions.get().strip()

        if not (new_position and new_location and new_type and new_salary and new_skills and new_total_positions):
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            conn = sqlite3.connect("SkillScope.db")
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE jobs SET job_position = ?, location = ?, job_type = ?, salary = ?, skills_required = ?, total_positions = ?
                WHERE job_id = ? AND recruiter_id = ?
            """, (new_position, new_location, new_type, new_salary, new_skills, new_total_positions, job_id, recruiter_id))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Job updated successfully!")
            edit_window.destroy()
            parent_window.destroy()  # Refresh main recruiter dashboard
            # recruiter_dashboard(recruiter_id, "Tech Corp")
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error: {e}")

    # Create edit job window
    edit_window = tk.Toplevel()
    edit_window.title("Edit Job")
    edit_window.geometry("400x400")

    # Fetch job details
    conn = sqlite3.connect("SkillScope.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM jobs WHERE job_id = ? AND recruiter_id = ?", (job_id, recruiter_id))
    job = cursor.fetchone()
    conn.close()

    if not job:
        messagebox.showerror("Error", "Job not found!")
        return

    tk.Label(edit_window, text="Edit Job", font=("Arial", 14, "bold")).pack(pady=10)
    
    tk.Label(edit_window, text="Job Position").pack()
    entry_position = tk.Entry(edit_window)
    entry_position.insert(0, job[2])  # Job Position
    entry_position.pack()

    tk.Label(edit_window, text="Location").pack()
    entry_location = tk.Entry(edit_window)
    entry_location.insert(0, job[3])  # Location
    entry_location.pack()

    tk.Label(edit_window, text="Job Type").pack()
    combo_job_type = ttk.Combobox(edit_window, values=["Remote", "Hybrid", "On-site"])
    combo_job_type.set(job[4])  # Job Type
    combo_job_type.pack()

    tk.Label(edit_window, text="Salary").pack()
    entry_salary = tk.Entry(edit_window)
    entry_salary.insert(0, job[5])  # Salary
    entry_salary.pack()

    tk.Label(edit_window, text="Skills Required").pack()
    entry_skills = tk.Entry(edit_window)
    entry_skills.insert(0, job[6])  # Skills Required
    entry_skills.pack()

    tk.Label(edit_window, text="Total Positions").pack()
    entry_total_positions = tk.Entry(edit_window)
    entry_total_positions.insert(0, job[7])  # Total Positions
    entry_total_positions.pack()

    tk.Button(edit_window, text="Update Job", command=update_job).pack(pady=20)
#  to load the job
def load_job_page(recruiter_id):
     job_window = tk.Toplevel()
     job_window.title("Manage Jobs")
     job_window.geometry("700x400")

     conn = sqlite3.connect("SkillScope.db")
     cursor = conn.cursor()
     cursor.execute("SELECT job_id,job_position , location,job_type,salary,skills_required,total_positions FROM jobs WHERE recruiter_id = ?", (recruiter_id,))
     jobs = cursor.fetchall()
     conn.close()

     tree = ttk.Treeview(job_window, columns=("ID", "Position", "Location", "Type", "Salary", "Skills", "Total"), show="headings")
     tree.heading("ID", text="Job ID")
     tree.heading("Position", text="Job Position")
     tree.heading("Location", text="Location")
     tree.heading("Type", text="Job Type")
     tree.heading("Salary", text="Salary")
     tree.heading("Skills", text="Skills Required")
     tree.heading("Total", text="Total Positions")
     tree.pack(fill=tk.BOTH, expand=True)

     for job in jobs:
        tree.insert("", tk.END, values=job)

     def edit_selected_job():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a job to edit!")
            return
            
        job_data = tree.item(selected_item)["values"]
        job_id = job_data[0]
        edit_job(job_id, recruiter_id, job_window)

     tk.Button(job_window, text="Edit Selected Job", command=edit_selected_job).pack(pady=10)

def view_job_applicant(recruiterId, recruiter_dashboard):
    view_job = tk.Toplevel()
    view_job.title("Job Applicants")
    view_job.geometry("700x400")

    conn = sqlite3.connect("SkillScope.db")
    cursor = conn.cursor()

    # Fetch job applications related to the recruiter
    cursor.execute("SELECT job_id, user_id FROM applied_jobs WHERE recruiter_id=? and status='Pending' ", (recruiterId,))
    data = cursor.fetchall()

    job_ids = [row[0] for row in data]
    user_ids = [row[1] for row in data]

    job_names = []
    user_details = []

    # Get job names
    for id in job_ids:
        cursor.execute("SELECT job_position FROM jobs WHERE job_id=?", (id,))
        job_names.append(cursor.fetchone()[0])  # Fetch job name

    # Get user details
    for id in user_ids:
        cursor.execute("SELECT username, email, phone_no FROM users WHERE user_id=?", (id,))
        cursor.execute("Select u.username,ud.skills,u.email,u.phone_no from users u join user_details ud on u.user_id=ud.user_id where u.user_id=? ",(1,))
        user_details.append(cursor.fetchone())  # Fetch user info

    conn.close()

    # Create Treeview
    tree = ttk.Treeview(view_job, columns=("JobName", "ApplicantName","Skills", "Email", "PhoneNo"), show="headings")
    tree.heading("JobName", text="Job Position")
    tree.heading("ApplicantName", text="Applicant Name")
    tree.heading("Skills", text="Skills")
    tree.heading("Email", text="Email")
    tree.heading("PhoneNo", text="Phone No")
    tree.pack(fill=tk.BOTH, expand=True)

    # Insert fetched data into the table
    for i in range(len(job_names)):
        tree.insert("", tk.END, values=(job_names[i], user_details[i][0], user_details[i][1], user_details[i][2], user_details[i][3]))


    # pending 
    def more_skilled_graph():
        print()
    # Function to handle accept/reject action
    def update_application_status(status):
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select an applicant first!")
            return

        # Get selected row values
        selected_values = tree.item(selected_item)["values"]
        job_name = selected_values[0]
        applicant_name = selected_values[1]

        # Get corresponding job_id & user_id
        conn = sqlite3.connect("SkillScope.db")
        cursor = conn.cursor()
        
        cursor.execute("SELECT job_id FROM jobs WHERE job_position=?", (job_name,))
        job_id = cursor.fetchone()[0]
        
        cursor.execute("SELECT user_id FROM users WHERE username=?", (applicant_name,))
        user_id = cursor.fetchone()[0]

        # Check if the status is already set
        cursor.execute("SELECT status FROM applied_jobs WHERE job_id=? AND user_id=?", (job_id, user_id))
        existing_status = cursor.fetchone()
        print(existing_status)

        if existing_status and existing_status[0] != 'Pending':
            messagebox.showwarning("Warning", f"Application already {existing_status[0]}!")
            conn.close()
            return

        # Update the status in the database
        cursor.execute("UPDATE applied_jobs SET status=? WHERE job_id=? AND user_id=?", (status, job_id, user_id))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", f"Application {status}!")
        tree.delete(selected_item)  # Remove row from the Treeview

    # Function to go back to the recruiter dashboard
    def go_back():
        view_job.destroy()  # Close the current window
        recruiter_dashboard(recruiterId)  # Open recruiter dashboard again

    # Button Frame
    button_frame = tk.Frame(view_job)
    button_frame.pack(pady=10)
    graph_button = tk.Button(button_frame, text="Check More Skilled", command=lambda: more_skilled_graph(), bg="black", fg="white")
    graph_button.grid(row=0, column=0, padx=5)
    accept_button = tk.Button(button_frame, text="Accept", command=lambda: update_application_status("Accepted"), bg="green", fg="white")
    accept_button.grid(row=0, column=1, padx=5)

    reject_button = tk.Button(button_frame, text="Reject", command=lambda: update_application_status("Rejected"), bg="red", fg="white")
    reject_button.grid(row=0, column=2, padx=5)


    back_button = tk.Button(button_frame, text="Back", command=go_back, bg="gray", fg="white")
    back_button.grid(row=0, column=3, padx=5)

def search_Applicants():
    search_window = tk.Toplevel()
    search_window.title("Search Applicants")
    search_window.geometry("600x400")

    tk.Label(search_window, text="Search Applicant by Name:", font=("Arial", 12, "bold")).pack(pady=10)
    
    entry_search = tk.Entry(search_window, width=30)
    entry_search.pack(pady=5)

    def fetch_applicant_details():
        applicant_name = entry_search.get().strip()

        if not applicant_name:
            messagebox.showerror("Error", "Please enter an applicant name!")
            return

        conn = sqlite3.connect("SkillScope.db")
        cursor = conn.cursor()

        # Query to fetch applicant details
        cursor.execute('''
            SELECT u.user_id, u.username, u.email, u.phone_no, d.skills, d.top_skill, 
                   d.college_name, d.degree, d.cgpa, d.expected_salary, d.city
            FROM users as u
            JOIN user_details as d ON u.user_id = d.user_id
            WHERE u.username LIKE ?
        ''', (f"%{applicant_name}%",))

        data = cursor.fetchall()
        print(data)
        conn.close()

        # Clear the previous search results
        for row in tree.get_children():
            tree.delete(row)

        if not data:
            messagebox.showinfo("No Results", "No applicant found with that name!")
            return

        # Insert data into the table
        for row in data:
            tree.insert("", "end", values=row)

    # Search Button
    tk.Button(search_window, text="Search", command=fetch_applicant_details, bg="blue", fg="white").pack(pady=5)

    # Table to display applicant details
    columns = ("User ID", "Username", "Email", "Phone", "Skills", "Top Skill", "College", "Degree", "CGPA", "expected_Salary", "City")
    
    tree = ttk.Treeview(search_window, columns=columns, show="headings", height=8)
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    tree.pack(pady=10, fill="both", expand=True)

    search_window.mainloop()



# Recruiter Dashboard UI
def recruiter_dashboard(recruiter_id, company_name):
    root = tk.Tk()
    root.title("Recruiter Dashboard")
    root.geometry("800x500")
    root.configure(bg="white")

    # Sidebar Frame
    menu_frame = tk.Frame(root, bg="#2C3E50", width=230, height=500)
    menu_frame.pack(side=tk.LEFT, fill=tk.Y)

    # Company Name & Dashboard Title
    tk.Label(menu_frame, text=f"{company_name}\nRecruiter Dashboard", fg="white", bg="#2C3E50",
             font=("Arial", 14, "bold"), justify="center").pack(pady=20)

    # Button Hover Effects
    def on_enter(e, button):
        button.config(bg="#1A252F", fg="white")

    def on_leave(e, button):
        button.config(bg="#34495E", fg="white")

    # Sidebar Buttons
    def create_sidebar_button(text, command):
        btn = tk.Button(menu_frame, text=text, font=("Arial", 12), bg="#34495E", fg="white", activebackground="#1A252F",
                        bd=0, relief="ridge", padx=10, pady=5, command=command)
        btn.pack(pady=10, fill=tk.X)
        btn.bind("<Enter>", lambda e: on_enter(e, btn))
        btn.bind("<Leave>", lambda e: on_leave(e, btn))
        return btn

    create_sidebar_button("📌 Post a Job", lambda: post_job(recruiter_id))
    create_sidebar_button("📋 Manage Jobs", lambda: load_job_page(recruiter_id))
    create_sidebar_button("🔎 Search Applicants", lambda: search_Applicants())
    create_sidebar_button("🔎 view job Applicants", lambda: view_job_applicant(recruiter_id,root))
    create_sidebar_button("🚪 Logout", lambda: logout(root))

    # Main Content Area
    content_frame = tk.Frame(root, bg="white")
    content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    # Dashboard Title
    tk.Label(content_frame, text="Welcome to the Recruiter Dashboard!", font=("Arial", 16, "bold"), bg="white",
             fg="#2C3E50").pack(pady=20)

    root.mainloop()

# Logout Function
def logout(root):
    root.destroy()
    import main  # Assuming 'main' is your login page



# Test the UI (Replace with actual recruiter ID & company name)
# recruiter_dashboard(7, "CyberSecurity Inc")


# setup_database()
# recruiter_dashboard(1, "CyberSecurity Inc")
