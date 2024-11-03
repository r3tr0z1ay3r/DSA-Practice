"""
Problem:
    Given a list of arrival times of students and student threshold k, 
    with arrival time indication <= 0 being on time and > 0 being late

    If there are less than k students in the class during class time return  "YES"
    If ther are atleast k students in the class during class time return "NO"

Intiution:
    By maintaing count of students, we can identify if the class can begin or not 
    during the start of class

Approach:
    We loop through the elements of the arrival time after we intialize an count variable
    Every time we encounter an negative number we increase the count by 1

    At the end of the loop if the count variable is greater than the threshold, we return "NO"
    else we return "YES"
"""

def angryProfessor(k, a):
    student_count = 0
    for arrival in a:
        if arrival <= 0:
            student_count += 1
    if student_count >= k:
        return "NO"
    else:
        return "YES"