import sqlite3

conn = sqlite3.connect('SkillScope.db')  # Connect to your database
cursor = conn.cursor()

# # Delete existing data
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

# conn.commit()








# new data---------------------------------------------

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
# conn.commit()

# conn.close()
# cursor.execute("select * from users")
# cursor.execute("select * from user_details")
# data=cursor.fetchall()
# print(data)


# import matplotlib.pyplot as plt
# cursor.execute("select * from jobs")
# dict={}
# data=cursor.fetchall()
# for row in data:
#     skills=row[6].split(',')
#     for skill in skills:
#         if skill.strip() in dict:
#             dict[skill.strip()]+=1
#         else:
#             dict[skill.strip()]=1
# print(dict)
# plt.figure(figsize=(30,30))
# plt.pie(dict.values(),labels=dict.keys(),autopct='%0.2f%%')
# # plt.legend(loc='upper right')
# plt.title("Most demading skills in market")
# plt.show()

# print(data[0][2].split(',')[1])

# cursor.execute("INSERT INTO applied_jobs (job_id, user_id, recruiter_id, status) VALUES (?, ?, ?,?)",('1','15' , '1','Pending',))
# conn.commit()
# cursor.execute("select * from applied_jobs where recruiter_id=1")
# cursor.execute("Select u.username,ud.skills,u.email,u.phone_no from users u join user_details ud on u.user_id=ud.user_id where u.user_id=? ",(1,))

# data=cursor.fetchall()
# print(data)
# job_id=data[0][0]
# user_id=data[0][1]
# print(job_id,user_id)
# cursor.execute('select job_position from jobs where job_id=?',(job_id,))
# job_postion=cursor.fetchone()
# # print(cursor.fetchone())
# cursor.execute('select username,email,phone_no from users where user_id=?',(user_id,))
# # print(cursor.fetchone())
# user_details=cursor.fetchone()
# print(job_postion+user_details)
# print(data)