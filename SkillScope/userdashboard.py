import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import post_resume
import search_job
import edit_profile
import matplotlib.pyplot as plt
import Setup_database


# Create the applied_jobs table if it doesn't exist
# def create_applied_jobs_table():
#     conn = sqlite3.connect('SkillScope.db')
#     cursor = conn.cursor()
#     cursor.execute('''CREATE TABLE IF NOT EXISTS applied_jobs (
#                         applied_job_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                         job_id INTEGER,
#                         user_id INTEGER,
#                         recruiter_id INTEGER,
#                         status TEXT DEFAULT 'Pending',
#                         FOREIGN KEY (job_id) REFERENCES jobs(job_id),
#                         FOREIGN KEY (user_id) REFERENCES users(user_id),
#                         FOREIGN KEY (recruiter_id) REFERENCES recruiters_details(recruiter_id)
#                     )''')
#     conn.commit()
#     conn.close()

# Function to apply for a job
def apply_for_job(job_id, user_id, recruiter_id):
    conn = sqlite3.connect('SkillScope.db')
    cursor = conn.cursor()

    # Check if the user has already applied for this job
    cursor.execute("SELECT * FROM applied_jobs WHERE job_id = ? AND user_id = ?", (job_id, user_id))
    existing_application = cursor.fetchone()

    if existing_application:
        messagebox.showinfo("Already Applied", "You have already applied for this job.")
    else:
        cursor.execute("INSERT INTO applied_jobs (job_id, user_id, recruiter_id, status) VALUES (?, ?, ?, 'Pending')",(job_id, user_id, recruiter_id))
        conn.commit()
        messagebox.showinfo("Success", "You have successfully applied for the job!")

    conn.close()

# Open Other Pages
def open_search_job(userID, root):
    root.destroy()
    search_job.search_JOB(userID)

def open_post_resume(userID, root):
    root.destroy()
    post_resume.postResume(userID)

def open_edit_profile(userID, root):
    root.destroy()
    edit_profile.edit_Profile(userID)


def view_demand_skill():
    conn = sqlite3.connect('SkillScope.db')
    cursor = conn.cursor()
    cursor.execute("select * from jobs")
    dict={}
    data=cursor.fetchall()
    for row in data:
        skills=row[6].split(',')
        for skill in skills:
            if skill.strip() in dict:
                dict[skill.strip()]+=1
            else:
                dict[skill.strip()]=1
    print(dict)
    plt.figure(figsize=(30,30))
    plt.pie(dict.values(),labels=dict.keys(),autopct='%0.2f%%',startangle=0 ,colors=plt.cm.Paired.colors)
    plt.title("Skills in Demand")
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

def view_demand_jobs():
    conn = sqlite3.connect('SkillScope.db')
    cursor = conn.cursor()
    cursor.execute("select * from jobs")
    dict={}
    data=cursor.fetchall()
    for row in data:
        skills=row[2].split(',')
        for skill in skills:
            if skill.strip() in dict:
                dict[skill.strip()]+=1
            else:
                dict[skill.strip()]=1
    print(dict)
    plt.figure(figsize=(30,30))
    plt.pie(dict.values(),labels=dict.keys(),autopct='%0.2f%%',startangle=0 ,colors=plt.cm.Paired.colors)
    plt.title("jobs in Demand")
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

def logout(root):
    confirm = messagebox.askyesno("Logout", "Are you sure you want to logout?")
    if confirm:
        root.destroy()
        import main  # Redirect to login page



def user_dashboard(user_id):
    # create_applied_jobs_table()  # Ensure table exists

    # Connect to database
    conn = sqlite3.connect('SkillScope.db')
    cursor = conn.cursor()

    # Fetch user's top skills
    cursor.execute("SELECT skills FROM user_details WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    top_skills = [skill.strip() for skill in result[0].split(',')] if result else []

    # Fetch matching jobs based on user's skills
    query = '''SELECT jobs.job_id, jobs.job_position, jobs.skills_required, jobs.salary, jobs.location, recruiters_details.recruiter_id,recruiters_details.company_name
               FROM jobs
               JOIN recruiters_details ON jobs.recruiter_id = recruiters_details.recruiter_id'''
    
    params = []
    if top_skills:
        conditions = ["jobs.skills_required LIKE ?" for _ in top_skills]
        query += " WHERE " + " OR ".join(conditions)
        params = [f"%{skill}%" for skill in top_skills]

    cursor.execute(query, params)
    jobs = cursor.fetchall()
    # conn.close()

    # Initialize UI Window
    root = tk.Tk()
    root.title("User Dashboard")
    root.geometry("1000x600")
    root.configure(bg="#F8F9FA")

    # Sidebar Frame (Left Panel)
    left_frame = tk.Frame(root, width=230, bg="#2C3E50", height=600)
    left_frame.pack(side=tk.LEFT, fill=tk.Y)

    # Sidebar Title
    tk.Label(left_frame, text="User Dashboard", fg="white", bg="#2C3E50",
             font=("Arial", 14, "bold"), pady=15).pack()

    # Sidebar Button Function with Hover Effects
    def create_sidebar_button(text, command):
        btn = tk.Button(left_frame, text=text, font=("Arial", 12), bg="#34495E", fg="white",
                        activebackground="#1A252F", bd=0, relief="ridge", padx=10, pady=7, command=command)
        btn.pack(pady=10, fill=tk.X)
        btn.bind("<Enter>", lambda e: btn.config(bg="#1A252F", fg="white"))
        btn.bind("<Leave>", lambda e: btn.config(bg="#34495E", fg="white"))
        return btn

    create_sidebar_button("🔎 Search Job", lambda: open_search_job(user_id, root))
    create_sidebar_button("📄 Post Resume", lambda: open_post_resume(user_id, root))
    create_sidebar_button("📊 view demanding skills", lambda: view_demand_skill())
    create_sidebar_button("📊 view demanding Jobs", lambda: view_demand_jobs())
    create_sidebar_button("📝 Edit Profile", lambda: open_edit_profile(user_id, root))
    create_sidebar_button("🚪 Logout", lambda: logout(root))

    # Right-Side Main Dashboard Content
    content_frame = tk.Frame(root, bg="white", padx=20, pady=20)
    content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    # Dashboard Title
    tk.Label(content_frame, text="🏆 Recommended Jobs", font=("Arial", 18, "bold"),
             bg="white", fg="#2C3E50").pack(pady=10)

    # Jobs Table (Treeview)
    tree_frame = tk.Frame(content_frame, bg="white", padx=10, pady=10)
    tree_frame.pack(fill=tk.BOTH, expand=True)

    columns = ("Company name", "Job Title", "Skills Required", "Salary", "Location", "Apply")
    tree = ttk.Treeview(tree_frame, columns=columns, show='headings')

    # Add Headings
    for col in columns[:-1]:  # Exclude Apply Button from Heading
        tree.heading(col, text=col)
        tree.column(col, width=150 if col != "Skills Required" else 250)

    # Style Table
    style = ttk.Style()
    style.configure("Treeview", font=("Arial", 10), rowheight=30, background="#ECF0F1")
    style.configure("Treeview.Heading", font=("Arial", 12, "bold"), background="#34495E", foreground="black")

    # Insert Jobs into Table
    for job in jobs:
        job_id, job_position, skills_required, salary, location, recruiter_id,recruiter_company_name= job
        tree.insert("", tk.END, values=(recruiter_company_name, job_position, skills_required, salary, location))

    tree.pack(fill=tk.BOTH, expand=True)

    # Frame for Apply Buttons
    button_frame = tk.Frame(content_frame, bg="white")
    button_frame.pack(fill=tk.X, padx=10, pady=10)

    # Function to get selected job and apply
    def apply_selected_job():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("No Selection", "Please select a job to apply.")
            return
        # print(selected_item[0])
        job_details = job
        print(job)
        job_id = job[0]
        cursor.execute("select recruiter_id from jobs where job_id=?",(job_id,))
        _id=cursor.fetchone()
        recruiter_id = _id[0]  # Recruiter ID is at index 5
        apply_for_job(job_id, user_id, recruiter_id)

    # Apply Button
    apply_btn = tk.Button(button_frame, text="Apply for Selected Job", font=("Arial", 12), bg="#28A745",
                          fg="white", padx=10, pady=5, command=apply_selected_job)
    apply_btn.pack(pady=10)

    # Start Tkinter Loop
    root.mainloop()

# Call the function with a user_id to test
# user_dashboard(1)
