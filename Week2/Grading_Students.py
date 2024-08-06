import math
### Output type-1: using modulo ###
def gradingStudents(grades):
    # Write your code here
    arr_grades = []
    for grade in grades:
        grade_diff_5 = grade % 5
        round_gap = 5 - grade_diff_5
        if grade < 38 or round_gap >= 3:
            arr_grades.append(grade)
        elif round_gap < 3:
            round_grade = grade + round_gap
            arr_grades.append(round_grade)
        else:
            return -1
    return arr_grades

### Output type-2: using .ceil() function ###
def gradingStudents(grades):
    arr_grades = []    
    for grade in grades:
        if grade >= 38 and math.ceil(grade / 5) * 5 - grade < 3:
            grade = math.ceil(grade / 5) * 5
        arr_grades.append(grade)
        
    return arr_grades
