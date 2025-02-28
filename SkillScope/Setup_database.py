import sqlite3

conn=sqlite3.connect('SkillScope.db')
cursor=conn.cursor()

# Delete existing data
# cursor.executescript("""
#     DELETE FROM recruiters_details;
#     DELETE FROM jobs;
#     DELETE FROM user_details;
#     DELETE FROM users;
#     DELETE FROM sqlite_sequence WHERE name='recruiters_details';
#     DELETE FROM sqlite_sequence WHERE name='jobs';
#     DELETE FROM sqlite_sequence WHERE name='user_details';
#     DELETE FROM sqlite_sequence WHERE name='users';

# """)


#usertable
cursor.execute(

    """
CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                phone_no TEXT NOT NULL UNIQUE,
                type TEXT NOT NULL
            );

"""
)

# recruiter details table
cursor.execute('''
        CREATE TABLE IF NOT EXISTS recruiters_details (
            recruiter_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            company_name TEXT NOT NULL,
            position TEXT NOT NULL,
            location TEXT NOT NULL,
            company_email TEXT NOT NULL UNIQUE,
            FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
        )
    ''')



    # user details table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_details (
        detail_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        skills TEXT NOT NULL,
        top_skill TEXT NOT NULL,
        college_name TEXT NOT NULL,
        degree TEXT NOT NULL,
        cgpa REAL NOT NULL,
        expected_salary INTEGER NOT NULL,
        city TEXT NOT NULL,
        resume_content TEXT DEFAULT NULL,  -- New column added
        FOREIGN KEY (user_id) REFERENCES users (user_id) ON DELETE CASCADE
    )
""")





# job table

cursor.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            job_id INTEGER PRIMARY KEY AUTOINCREMENT,
            recruiter_id INTEGER,
            job_position TEXT NOT NULL,
            location TEXT NOT NULL,
            job_type TEXT NOT NULL,
            salary INTEGER NOT NULL,
            skills_required TEXT NOT NULL,
            total_positions INTEGER NOT NULL,
            FOREIGN KEY (recruiter_id) REFERENCES recruiters_details(recruiter_id) ON DELETE CASCADE
        )
    ''')


# applied job table

cursor.execute('''CREATE TABLE IF NOT EXISTS applied_jobs (
                        applied_job_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        job_id INTEGER,
                        user_id INTEGER,
                        recruiter_id INTEGER,
                        status TEXT DEFAULT 'Pending',
                        FOREIGN KEY (job_id) REFERENCES jobs(job_id),
                        FOREIGN KEY (user_id) REFERENCES users(user_id),
                        FOREIGN KEY (recruiter_id) REFERENCES recruiters_details(recruiter_id)
                    )''')




# # insertinf the data

# # --------------------------------run one time and comment the insert query for all the tables----------------------------------------


# cursor.execute(

#     '''
# INSERT INTO users (username, password, email, phone_no, type) VALUES
# -- Job Seekers (15)
# ('rahul_sharma', 'pass123', 'rahul.sharma@gmail.com', '9876543210', 'user'),
# ('neha_verma', 'pass123', 'neha.verma@gmail.com', '9876543211', 'user'),
# ('arjun_mehta', 'pass123', 'arjun.mehta@gmail.com', '9876543212', 'user'),
# ('priya_singh', 'pass123', 'priya.singh@gmail.com', '9876543213', 'user'),
# ('rohit_kumar', 'pass123', 'rohit.kumar@gmail.com', '9876543214', 'user'),
# ('deepika_patil', 'pass123', 'deepika.patil@gmail.com', '9876543215', 'user'),
# ('vikram_gupta', 'pass123', 'vikram.gupta@gmail.com', '9876543216', 'user'),
# ('sneha_rastogi', 'pass123', 'sneha.rastogi@gmail.com', '9876543217', 'user'),
# ('manish_jain', 'pass123', 'manish.jain@gmail.com', '9876543218', 'user'),
# ('richa_bose', 'pass123', 'richa.bose@gmail.com', '9876543219', 'user'),
# ('amit_chopra', 'pass123', 'amit.chopra@gmail.com', '9876543220', 'user'),
# ('swati_mishra', 'pass123', 'swati.mishra@gmail.com', '9876543221', 'user'),
# ('karan_yadav', 'pass123', 'karan.yadav@gmail.com', '9876543222', 'user'),
# ('ananya_sen', 'pass123', 'ananya.sen@gmail.com', '9876543223', 'user'),
# ('harshit_pandey', 'pass123', 'harshit.pandey@gmail.com', '9876543224', 'user'),

# -- Recruiters (5)
# ('tcs_hr', 'pass123', 'tcs.hr@gmail.com', '9876543225', 'recruiter'),
# ('infosys_hr', 'pass123', 'infosys.hr@gmail.com', '9876543226', 'recruiter'),
# ('wipro_hr', 'pass123', 'wipro.hr@gmail.com', '9876543227', 'recruiter'),
# ('hcl_hr', 'pass123', 'hcl.hr@gmail.com', '9876543228', 'recruiter'),
# ('amazon_hr', 'pass123', 'amazon.hr@gmail.com', '9876543229', 'recruiter');

# '''
# )


# cursor.execute(
#     '''
# INSERT INTO user_details (user_id, skills, top_skill, college_name, degree, cgpa, expected_salary, city) VALUES
# (1, 'Java, Spring Boot, SQL', 'Java', 'IIT Bombay', 'B.Tech', 8.5, 900000, 'Bangalore'),
# (2, 'Python, Machine Learning, TensorFlow', 'Machine Learning', 'IIT Delhi', 'M.Tech', 9.0, 1200000, 'Delhi'),
# (3, 'React, JavaScript, CSS', 'React.js', 'NIT Trichy', 'B.Tech', 8.0, 850000, 'Hyderabad'),
# (4, 'Node.js, MongoDB, Express.js', 'Node.js', 'IIIT Hyderabad', 'M.Tech', 8.8, 950000, 'Hyderabad'),
# (5, 'C++, Data Structures, Algorithms', 'C++', 'IIT Kharagpur', 'B.Tech', 9.2, 1100000, 'Mumbai'),
# (6, 'Cybersecurity, Ethical Hacking', 'Cybersecurity', 'Delhi University', 'B.Sc', 7.8, 1000000, 'Delhi'),
# (7, 'AWS, Cloud Computing, DevOps', 'AWS', 'IISc Bangalore', 'M.Tech', 9.0, 1300000, 'Bangalore'),
# (8, 'UI/UX, Figma, Adobe XD', 'UI/UX Design', 'NIFT Mumbai', 'B.Des', 7.5, 750000, 'Mumbai'),
# (9, 'Embedded Systems, Microcontrollers', 'Embedded Systems', 'IIT Madras', 'B.Tech', 8.4, 900000, 'Chennai'),
# (10, 'Game Development, Unity, Unreal Engine', 'Unity', 'BITS Pilani', 'B.Tech', 8.7, 950000, 'Pune'),
# (11, 'Blockchain, Solidity, Ethereum', 'Blockchain', 'IIM Bangalore', 'MBA', 8.6, 1200000, 'Bangalore'),
# (12, 'SQL, MySQL, PostgreSQL', 'Database Management', 'IIT Roorkee', 'B.Tech', 8.3, 1000000, 'Delhi'),
# (13, 'Artificial Intelligence, Deep Learning', 'AI', 'IIT Kanpur', 'M.Tech', 9.1, 1400000, 'Hyderabad'),
# (14, 'Technical Support, Networking', 'Networking', 'Delhi University', 'BCA', 7.9, 800000, 'Noida'),
# (15, 'RPA, UiPath, Automation Anywhere', 'RPA', 'Jadavpur University', 'B.Tech', 8.2, 950000, 'Kolkata');

# '''
# )

# cursor.execute(
#     '''
# INSERT INTO recruiters_details (user_id, company_name, position, location, company_email) VALUES
# (16, 'TCS', 'HR Manager', 'Bangalore', 'tcs.hr@gmail.com'),
# (17, 'Infosys', 'HR Manager', 'Pune', 'infosys.hr@gmail.com'),
# (18, 'Wipro', 'HR Manager', 'Hyderabad', 'wipro.hr@gmail.com'),
# (19, 'HCL', 'HR Manager', 'Chennai', 'hcl.hr@gmail.com'),
# (20, 'Amazon India', 'HR Manager', 'Mumbai', 'amazon.hr@gmail.com');

# '''
# )

# cursor.execute(
#     '''
# INSERT INTO jobs (recruiter_id, job_position, location, job_type, salary, skills_required, total_positions) VALUES
# -- Jobs by TCS (Recruiter ID = 1)
# (1, 'Software Engineer', 'Bangalore', 'Full-Time', 900000, 'Java, Spring Boot', 5),
# (1, 'Data Scientist', 'Pune', 'Full-Time', 1200000, 'Python, Machine Learning', 3),
# (1, 'UI/UX Designer', 'Mumbai', 'Full-Time', 750000, 'Figma, Adobe XD, CSS', 2),

# -- Jobs by Infosys (Recruiter ID = 2)
# (2, 'Frontend Developer', 'Mumbai', 'Full-Time', 800000, 'React, JavaScript, CSS', 4),
# (2, 'Backend Developer', 'Hyderabad', 'Full-Time', 850000, 'Node.js, MongoDB, Express.js', 3),
# (2, 'DevOps Engineer', 'Chennai', 'Full-Time', 950000, 'Docker, Kubernetes, AWS', 2),

# -- Jobs by Wipro (Recruiter ID = 3)
# (3, 'Cybersecurity Analyst', 'Delhi', 'Full-Time', 1100000, 'Ethical Hacking, Cybersecurity', 2),
# (3, 'AI Engineer', 'Bangalore', 'Full-Time', 1300000, 'Deep Learning, TensorFlow, Python', 3),
# (3, 'Cloud Engineer', 'Hyderabad', 'Full-Time', 1000000, 'AWS, Azure, Google Cloud', 4),

# -- Jobs by HCL (Recruiter ID = 4)
# (4, 'Software Tester', 'Mumbai', 'Full-Time', 700000, 'Selenium, Test Automation', 5),
# (4, 'Full Stack Developer', 'Delhi', 'Full-Time', 950000, 'MERN Stack, JavaScript, Node.js', 3),

# -- Jobs by Amazon India (Recruiter ID = 5)
# (5, 'Blockchain Developer', 'Bangalore', 'Full-Time', 1200000, 'Ethereum, Solidity, Hyperledger', 2),
# (5, 'Technical Support Engineer', 'Noida', 'Full-Time', 650000, 'Networking, Troubleshooting, Linux', 4),
# (5, 'Salesforce Developer', 'Gurgaon', 'Full-Time', 1100000, 'Salesforce, Apex, Lightning', 3),
# (5, 'Product Manager', 'Mumbai', 'Full-Time', 1400000, 'Agile, Scrum, Product Roadmap', 1);

# '''
# )
conn.commit()



# ------------------------------ do not run this code--------------
# # cursor.execute("Select * from jobs")
# cursor.execute("SELECT skills FROM user_details WHERE user_id = ?", (1,))
# result = cursor.fetchone()
# print(result)
# top_skills = [skill.strip() for skill in result[0].split(',')] if result else []
# print(top_skills)
# query='''SELECT jobs.job_id, jobs.job_position, jobs.skills_required, jobs.salary, jobs.location, recruiters_details.recruiter_id
#                FROM jobs
#                JOIN recruiters_details ON jobs.job_id = recruiters_details.recruiter_id'''
# cursor.execute('''SELECT jobs.job_id, jobs.job_position, jobs.skills_required, jobs.salary, jobs.location, recruiters_details.recruiter_id
#                FROM jobs
#                JOIN recruiters_details ON jobs.recruiter_id = recruiters_details.recruiter_id''')
# print(cursor.fetchall())

# params = []
# if top_skills:
#     conditions = ["jobs.skills_required LIKE ?" for _ in top_skills]
#     query += " WHERE " + " OR ".join(conditions)
#     params = [f"%{skill}%" for skill in top_skills]
# print(query,'query')
# cursor.execute(query, params)
# jobs = cursor.fetchall()
# print(jobs)