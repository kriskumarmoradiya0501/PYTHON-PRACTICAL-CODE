# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 13:33:48 2024

@author: ADMIN
"""

students = {
    '22BCA001': {
        'name': 'Mayur Patel',
        'subjects': {
            'Math': 55,
            'Physics': 90,
            'Chemistry': 45,
            'Biology': 90,
            'English': 55
        }
    },
    '22BCA002': {
        'name': 'Harsha Mehta',
        'subjects': {
            'Math': 85,
            'Physics': 72,
            'Chemistry': 65,
            'Biology': 58,
            'English': 77
        }
    },
    '22BCA003': {
        'name': 'Ramesh Singh',
        'subjects': {
            'Math': 48,
            'Physics': 55,
            'Chemistry': 60,
            'Biology': 52,
            'English': 50
        }
    },
    '22BCA004': {
        'name': 'Suresh Sharma',
        'subjects': {
            'Math': 60,
            'Physics': 80,
            'Chemistry': 85,
            'Biology': 75,
            'English': 95
        }
    },
    '22BCA005': {
        'name': 'Jayesh Gupta',
        'subjects': {
            'Math': 90,
            'Physics': 88,
            'Chemistry': 92,
            'Biology': 94,
            'English': 78
        }
    }
}

id = input("Enter student id ")

if id in students:
    student = students[id]
    name = student['name']
    subjects = student['subjects']
    
    print("Student ID: ",id," Student Name: ",name)
    print("-" * 105)
    print(f"{'Subjet name':<40}{'obtan Mark':<30}{'Grade'}")
    
    total_marks = 0
    total_subjects = len(subjects)
    failed = False
    
    for subject, marks in subjects.items():
        if marks > 80:
            grade = 'AA'
        elif marks >= 70:
            grade = 'AB'
        elif marks >= 60:
            grade = 'BB'
        elif marks >= 50:
            grade = 'CC'
        else:
            grade = 'FF'
            failed = True
        
        total_marks += marks
        print(f"{subject:<40}{marks:<30}{grade}")
    
    print("-" * 105)
    
    percentage = total_marks / total_subjects
    if percentage > 80:
        overall_grade = 'AA'
    elif percentage >= 70:
        overall_grade = 'AB'
    elif percentage >= 60:
        overall_grade = 'BB'
    elif percentage >= 50:
        overall_grade = 'CC'
    else:
        overall_grade = 'FF'
    
    if failed:
        overall_grade = 'FF'
    
    print("Overall Result: ")
    print(f"Total Marks: {total_marks} \t | Percentage: {percentage:.2f}% \t | Grade: {overall_grade}")

else:
    print("Student ID not found.")
