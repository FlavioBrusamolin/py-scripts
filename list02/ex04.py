student = {
    'name': input("Enter student's name: "),
    'grade': float(input("Enter student's grade: "))
}

student['situation'] = 'AP' if student['grade'] >= 60 else 'RP'

print(f'Student data: {student}')
