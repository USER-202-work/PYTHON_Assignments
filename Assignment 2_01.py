#1) Design a student management project using multiple Python modules instead of a single script.
#2) Design a student management project using multiple Python modules instead of a single script.
#3) Create a user-defined module containing student functions and use it in another Python file.
#4) Develop a marks processing system using a separate marks module and import it in main program.
#5) Build a report generation module using classes and connect it to main student system.
#6) Demonstrate importing modules using import, from … import, and module alias.
#7) Create a reusable module that can be used across multiple student applications.
#8) Separate attendance, marks, student data, and fee management into different modules and integrate them.
#9) Develop a case where predefined modules like math, datetime, or random are required in student management.
#10) Create a module and print its built-in properties such as __name__, __file__, and __dict__.
# Build a complete student mini-project fully modular, demonstrating importance of modular programming.

#student.py → Student data functions (create/update/list/delete)

students = {}

def add_student(name, email, standard):
    student_id = "STU" + str(len(students) + 1)
    students[student_id] = {"name": name, "email": email, "standard": standard}
    return student_id

def get_student(student_id):
    return students.get(student_id)

def list_students():
    return students

#marks.py → Marks processing (add marks, totals, results)

marks_data = {}

def add_marks(student_id, subject, score):
    if student_id not in marks_data:
        marks_data[student_id] = {}
    marks_data[student_id][subject] = score

def get_marks(student_id):
    return marks_data.get(student_id, {})

def calculate_percentage(student_id):
    subjects = marks_data.get(student_id, {})
    if not subjects:
        return 0
    total = sum(subjects.values())
    return round(total / (len(subjects) * 100) * 100, 2)

#attendance.py → Attendance management

attendance_data = {}

def mark_present(student_id, day):
    if student_id not in attendance_data:
        attendance_data[student_id] = []
    attendance_data[student_id].append(day)

def attendance_percentage(student_id, total_days):
    present_days = len(attendance_data.get(student_id, []))
    return round((present_days / total_days) * 100, 2)

#fees.py → Fee tracking and statements

fees_due = {}
fees_paid = {}

def set_due(student_id, amount):
    fees_due[student_id] = amount

def pay_fee(student_id, amount):
    if student_id not in fees_paid:
        fees_paid[student_id] = 0
    fees_paid[student_id] += amount

def balance(student_id):
    due = fees_due.get(student_id, 0)
    paid = fees_paid.get(student_id, 0)
    return due - paid
``

#report.py → Class-based report generation

import student
import marks
import attendance
import fees

def generate_report(student_id, total_days):
    s = student.get_student(student_id)
    if not s:
        return "Student not found"
    percent = marks.calculate_percentage(student_id)
    att_percent = attendance.attendance_percentage(student_id, total_days)
    fee_balance = fees.balance(student_id)

    report = f"""
    Student Report
    ID: {student_id}
    Name: {s['name']}
    Standard: {s['standard']}
    Marks: {marks.get_marks(student_id)}
    Percentage: {percent}%
    Attendance: {att_percent}%
    Fee Balance: ₹{fee_balance}
    """
    return report

#common/utils.py → Reusable utilities (IDs, grading, currency, dates)

from datetime import date, datetime
import math
import random
import string

def generate_student_id(prefix="STU"):
    yymmdd = datetime.now().strftime("%y%m%d")
    suffix = ''.join(random.choices(string.digits, k=4))
    return f"{prefix}{yymmdd}{suffix}"

def calculate_percentage(marks, max_per_subject=100):
    if not marks:
        return 0.0
    total_scored = sum(marks.values())
    total_max = max_per_subject * len(marks)
    return round((total_scored / total_max) * 100, 2)

def grade_from_percent(percent):
    if percent >= 90: return "A+"
    elif percent >= 80: return "A"
    elif percent >= 70: return "B+"
    elif percent >= 60: return "B"
    elif percent >= 50: return "C"
    elif percent >= 40: return "D"
    else: return "F"

def currency(amount, symbol="₹"):
    return f"{symbol}{amount:,.2f}"

#common/module_info.py → Print built-in module properties

def show_info(module):
    print("Module Name:", module.__name__)
    print("Module File:", getattr(module, "__file__", "N/A"))
    print("Module Dict Keys:", list(module.__dict__.keys())[:10])

#main.py → Integrates all modules and demonstrates imports + execution

import student
from marks import add_marks, calculate_percentage
import attendance as att
import fees
from report import generate_report
import module_info
import math, random
from datetime import date

# Add student
sid = student.add_student("Aarav", "aarav@example.com", "10")

# Add marks
add_marks(sid, "Math", 85)
add_marks(sid, "Science", 90)

# Attendance
for d in range(1, 11):
    if random.random() > 0.3:
        att.mark_present(sid, d)

# Fees
fees.set_due(sid, 15000)
fees.pay_fee(sid, 5000)

# Show report
print(generate_report(sid, total_days=15))

# Use math & datetime
print("Square root of 100:", math.sqrt(100))
print("Today's date:", date.today())

# Show module info
module_info.show_info(student)
