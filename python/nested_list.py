'''
Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.'''

python_students = [['Harsh', 20], ['Beria', 20], ['Varun', 19] , ['Kakunami', 19], ['Vikas', 21]] 
winners = []
numbers = []
min_number = min(python_students, key= lambda x:x[1])[1]
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     python_students.append([name,score])


    
remaining_scores = []

for students in python_students:
    if students[1] > min_number:
        remaining_scores.append(students)

min_number = min(remaining_scores, key= lambda x:x[1])[1]

for names in remaining_scores:
    if names[1] == min_number:
        winners.append(names[0])

winners.sort()

for names in winners:
    print(names)
