#!/usr/bin/env python
# coding: utf-8

# In[1]:


def students():
    return ["Rahul", "Priya", "Karthik", "Sneha", "Arjun", "Meena", "Ravi", "Anjali", "Vikram", "Divya"]

def student_id():
    return ["STU001", "STU002", "STU003", "STU004", "STU005", "STU006", "STU007", "STU008", "STU009", "STU010"]


def subjects():
    return ["Math", "Science", "English", "History", "Computer"]

def stu_marks():
    marks = {
        "Rahul": {"Math": 85, "Science": 78, "English": 92, "History": 74, "Computer": 88},
        "Priya": {"Math": 90, "Science": 82, "English": 95, "History": 80, "Computer": 91},
        "Karthik": {"Math": 76, "Science": 88, "English": 80, "History": 70, "Computer": 85},
        "Sneha": {"Math": 92, "Science": 90, "English": 88, "History": 85, "Computer": 94},
        "Arjun": {"Math": 70, "Science": 65, "English": 72, "History": 68, "Computer": 75},
        "Meena": {"Math": 88, "Science": 92, "English": 85, "History": 90, "Computer": 87},
        "Ravi": {"Math": 60, "Science": 70, "English": 65, "History": 72, "Computer": 68},
        "Anjali": {"Math": 95, "Science": 98, "English": 92, "History": 94, "Computer": 96},
        "Vikram": {"Math": 82, "Science": 78, "English": 80, "History": 75, "Computer": 85},
        "Divya": {"Math": 88, "Science": 85, "English": 90, "History": 87, "Computer": 89}
    }
    return marks


marks = stu_marks()


def calculate_total(student):
    return sum(marks[student].values())


def calculate_average(student):
    total = calculate_total(student)
    return total / len(marks[student])


def Grades(student):
    total = calculate_total(student)
    if total > 440:
        return "A"
    elif total > 400:
        return "B"
    elif total > 350:
        return "C"
    elif total > 300:
        return "D"
    elif total > 200:
        return "E"
    else:
        return "Fail"


# In[ ]:




