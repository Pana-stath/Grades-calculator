print('Labs and quizzes(values over 6 will be set to 6):')
print('Labs:')
Completed_labs = float(input("Enter the number of labs completed(20%): "))
if Completed_labs > 6:
    Completed_labs = 6
else:
    Completed_labs
print('Quizzes:')
Completed_quizzes = float(input("Enter the number of quizzes completed(15%): "))
if Completed_quizzes > 6:
    Completed_quizzes = 6
else:
    Completed_quizzes
print('Please input a grade within 0 to 100 for all the following:')
print('Assignments(16% total):')
Ass_1 = float(input("Enter the grade for Assignment 1(4%): "))
Ass_2 = float(input("Enter the grade for Assignment 2(4%): "))
Ass_3 = float(input("Enter the grade for Assignment 3(4%): "))
Ass_4 = float(input("Enter the grade for Assignment 4(4%): "))
print('Midterms(25% total):')
Midterm_1 = float(input('Enter the grade for Midterm 1(12.5%): '))
Midterm_2 = float(input('Enter the grade for Midterm 2(12.5%): '))
print('Final:')
Final_exam = float(input('Enter the grade for Final Exam(18%): '))
print('Midterm and Final Preparation')
Midterm_and_Final_Prep = float(input('Enter the grade for Midterms and Final Preparation(6%): '))
Grade = ((((Completed_labs / 6) * 100) * 0.2) + (((Completed_quizzes / 6) * 100) * 0.15) + (Ass_1 * 0.04) + (Ass_2 * 0.04) + (Ass_3 * 0.04) + (Ass_4 * 0.04) + (Midterm_1 * 0.125) + (Midterm_2 * 0.125) + (Final_exam * 0.18) + (Midterm_and_Final_Prep * 0.06))
print('Your grade is: ' + str(Grade))
if Grade >= 60:
    print('Student has passed')
else:
    print('Student has failed')
