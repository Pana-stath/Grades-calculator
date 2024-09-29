print('Labs and quizzes(values over 6 will be set to 6):')
Completed_labs = float(input("Enter the number of labs completed: "))
if Completed_labs > 6:
    Completed_labs = 6
else:
    Completed_labs
Completed_quizzes = float(input("Enter the number of quizzes completed: "))
if Completed_quizzes > 6:
    Completed_quizzes = 6
else:
    Completed_quizzes
print('Please input a grade within 0 to 100 for all the following:')
Ass_1 = float(input("Enter grade for Assignment 1: "))
Ass_2 = float(input("Enter grade for Assignment 2: "))
Ass_3 = float(input("Enter grade for Assignment 3: "))
Ass_4 = float(input("Enter grade for Assignment 4: "))
Midterm_1 = float(input('Enter grade for Midterm 1: '))
Midterm_2 = float(input('Enter grade for Midterm 2: '))
Final_exam = float(input('Enter grade for Final Exam: '))
Midterm_and_Final_Prep = float(input('Enter grade for Midterms and Final Preparation: '))
Grade = ((((Completed_labs / 6) * 100) * 0.2) + (((Completed_quizzes / 6) * 100) * 0.15) + (Ass_1 * 0.04) + (Ass_2 * 0.04) + (Ass_3 * 0.04) + (Ass_4 * 0.04) + (Midterm_1 * 0.125) + (Midterm_2 * 0.125) + (Final_exam * 0.18) + (Midterm_and_Final_Prep * 0.06))
print('Your grade is: ' + str(Grade))
